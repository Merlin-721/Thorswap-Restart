
import asyncio
from uniswap import Uniswap
from trader import THORTrader, FTXTrader
from xchainpy_util.asset import Asset
from multiprocessing import Process
from logger import get_logger, logging
import time
import requests

from account import DEBUGGING

from oracle import thornode_log
from trader import FTX_TRADER_log
from account import account_log
arb_log = get_logger("ARB", level=logging.DEBUG)

# def thor_run_handler(params):
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(thor_run(**params))
#     loop.close()


class ThorRestartMultiLoop:
	def __init__(self, base_asset, final_asset, network, hosts):
		# self.base_str = base_asset
		self.base_asset = Asset.from_str(base_asset)
		# self.final_str = final_asset
		self.final_asset = Asset.from_str(final_asset)
		self.ftx_symb = 'USD'
		self.ftx = FTXTrader()

		address = "YOUR ADDRESS"          # or None if you're not going to make transactions
		private_key = "YOUR PRIVATE KEY"  # or None if you're not going to make transactions
		version = 2                       # specify which version of Uniswap to use
		provider = "WEB3 PROVIDER URL"    # can also be set through the environment variable `PROVIDER`
		self.uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

		self.thor = THORTrader(network=network, host=IPs)
		self.statements()

		# Get addresses
		self.base_address = self.thor.account.get_address(asset=base_asset)
		self.final_address = self.thor.account.get_address(asset=final_asset)

	async def statements(self):
		await self.thor.account.statement()

	def get_halted(self,chain):
		if DEBUGGING:
			is_halted = False
		else:
			mimir = requests.get('https://thornode.thorchain.info/thorchain/mimir').json()
			is_halted = True if mimir[f'mimir//HALT{chain}TRADING'] != 0 else False
		thornode_log.info(f"Base asset chain {chain} halted: {is_halted}")
		return is_halted
	
	async def get_arb_mult(self,thor_est_out):
		book = await self.ftx.account.fetch_order_book(f"{self.base_asset.symbol}/{self.ftx_symb}")
		bids = await self.ftx.get_book(book['bids'], 5, in_amount)
		# arb value is implied thor price / ftx price
		ftx_price = bids[0][0]
		arb_mult = (thor_est_out/in_amount) / float(ftx_price)
		FTX_TRADER_log.info(f"Base asset {self.base_asset} FTX price: {ftx_price}")
		arb_log.info(f"{self.base_asset.symbol}/{self.final_asset.symbol} arb multiple: {arb_mult}")
		return arb_mult

	async def main_loop(self, in_amount, req_profit_mult=1.02, sleep_time=0.5):
		base_balance = await self.thor.account.get_balance(asset=self.base_asset)
		thornode_log.info(f"Base asset {self.base_asset.symbol} balance: {base_balance}")

		while True:
			time.sleep(sleep_time)
			# Check if base or final are halted
			base_is_halted = self.get_halted(self.base_asset.chain)
			final_is_halted = self.get_halted(self.final_asset.chain)

			while not base_is_halted and not final_is_halted:
				# No longer halted
				thornode_log.warning(f"Base asset chain {self.base_asset.chain} status: {base_is_halted}")
				thornode_log.warning(f"Target asset chain {self.final_asset.chain} status: {final_is_halted}")
				# Estimate thorswap
				thor_est_out = self.thor.estimate_swap_output(in_amount=in_amount, in_asset=self.base_asset,
															out_asset=self.final_asset)
				arb_mult = await self.get_arb_mult(thor_est_out)
				# if profitable
				if arb_mult > req_profit_mult:
					if base_balance < in_amount:
						# Do uniswap
						try:
							base_balance = await self.thor.account.get_balance(asset=self.base_asset)
							assert base_balance > in_amount
						except AssertionError:
							account_log.warning(f"Swap: {in_amount} greater than base balance: {base_balance}")
							return
						# recheck profitability due to time delay of swap

					# perform thorswap
					arb_log.info(f"Arbitrage opportunity found! {arb_mult}x")
					arb_log.info(f"Swapping {in_amount} {self.base_asset.symbol} for est. {thor_est_out} {self.final_asset.symbol}")
					execute = await self.thor.swap(in_amount=in_amount, in_asset=self.base_asset, 
											out_asset=self.final_asset, dest_addr=self.final_address, wait=False)
				
					if not execute:
						arb_log.error("Swap failed")
					else:
						arb_log.warning("Swap successful!!")

				else:
					continue
				uni_est_out = self.uniswap # estimate uniswap output
				in_amount = uni_est_out
				base_balance = await self.thor.account.get_balance(asset=self.base_asset)







if __name__ == '__main__':

	if DEBUGGING:
		network = 'MCTN'
		IPs = ["44.238.90.227"]
		final_asset = 'BNB.BUSD-74E' 
	else:
		network = 'MCCN'
		IPs = ["136.244.65.26","159.65.212.234", "174.138.105.79"]
		final_asset = 'BNB.BUSD-BD1' # starting asset

	base_asset = 'ETH.ETH'
	in_amount = 0.01 # input amount
	sleep_time = 0.4

	# thor_runner = Process(target=thor_run_handler({'network': network, 'IPs': IPs, 'final_asset': final_asset, 'base_asset': base_asset,
	# 			 'in_amount': in_amount, 'sleep_time':sleep_time}))
	# thor_runner.start()