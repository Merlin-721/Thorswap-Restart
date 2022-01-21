import asyncio
from trader import THORTrader, FTXTrader
from xchainpy_util.asset import Asset
from multiprocessing import Process
from logger import get_logger, logging
import time
import requests

from account import DEBUGGING

ftx = FTXTrader()
from oracle import thornode_log
from trader import FTX_TRADER_log
arb_log = get_logger("ARB", level=logging.DEBUG)

def thor_run_handler(params):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(thor_run(**params))
    loop.close()

def get_halted(chain):
	if DEBUGGING:
		is_halted = False
	else:
		mimir = requests.get('https://thornode.thorchain.info/thorchain/mimir').json()
		is_halted = True if mimir[f'mimir//HALT{chain}TRADING'] != 0 else False
	thornode_log.info(f"Base asset chain {chain} halted: {is_halted}")
	return is_halted

async def thor_run(network, IPs, final_asset, base_asset, in_amount, sleep_time=0.5):
	base_str = base_asset
	base_asset = Asset.from_str(base_asset)
	final_str = final_asset
	final_asset = Asset.from_str(final_asset)

	ftx_symb = 'USD'

	# gas price strategy is slow af
	# NOTE commented out gas price strat in account.py
	thor = THORTrader(network=network, host=IPs)

	# Get and display balances
	await thor.account.statement()
	base_balance = await thor.account.get_balance(asset=base_asset)
	assert base_balance != None, "Base balance is 'None'"
	# assert base_balance > in_amount, f"Insufficient {base_str} balance"
	thornode_log.info(f"Base asset {base_str} balance: {base_balance}")

	# Get addresses
	base_address = thor.account.get_address(asset=base_asset)
	final_address = thor.account.get_address(asset=final_asset)

	# Check if chains halted
	base_is_halted, final_is_halted = True, True
	while base_is_halted or final_is_halted:
		time.sleep(sleep_time)
		print()
		# Calculate output with fees 
		thor_est_out, tx_fee = thor.estimate_swap_output(in_amount=in_amount, in_asset=base_asset,
													out_asset=final_asset)
		if base_asset == 'BNB.BUSD-74E' or base_asset == 'BNB.BUSD-BD1':
			in_ftx_price = 1
		else:
			in_book = await ftx.account.fetch_order_book(f"{base_asset.symbol}/{ftx_symb}")
			in_ftx_price = await ftx.get_book(in_book['bids'], 5, in_amount)
			in_ftx_price = in_ftx_price[0][0]
		if final_asset == 'BNB.BUSD-74E' or final_asset == 'BNB.BUSD-BD1':
			out_ftx_price = 1
		else:
			out_book = await ftx.account.fetch_order_book(f"{final_asset.symbol}/{ftx_symb}")
			out_ftx_price = await ftx.get_book(out_book['bids'], 5, thor_est_out)
			out_ftx_price = out_ftx_price[0][0]

		# fee_dollars = in_ftx_price * tx_fee
		# starting value in dollars
		start_val = in_ftx_price * in_amount
		# end value in dollars
		end_val = out_ftx_price * thor_est_out - tx_fee
		arb_mult = end_val / start_val
		FTX_TRADER_log.info(f"Base asset {base_asset} FTX price: {in_ftx_price}")
		FTX_TRADER_log.info(f"Final asset {final_asset} FTX price: {out_ftx_price}")
		FTX_TRADER_log.info(f"Start value: {start_val}, End value: {end_val}")
		arb_log.info(f"{base_str}/{final_str} arb mul with tx fee: {arb_mult}")

		# Check base
		base_is_halted = get_halted(base_asset.chain)
		# Check final
		final_is_halted = get_halted(final_asset.chain)

	# No longer halted
	thornode_log.warning(f"Base asset chain {base_asset.chain} status: {base_is_halted}")
	thornode_log.warning(f"Target asset chain {final_asset.chain} status: {final_is_halted}")

	# greater than 5% opportunity
	if arb_mult >= 1.05 or DEBUGGING:
		arb_log.info(f"Arbitrage opportunity found! {arb_mult:.2f}x")
		arb_log.info(f"Swapping {in_amount} {base_str} for est. {thor_est_out} {final_str}")
		assert base_balance > in_amount + tx_fee, f"Insufficient balance {base_balance} needed for {in_amount+tx_fee} swap"
		execute = await thor.swap(in_amount=in_amount, in_asset=base_asset, 
								out_asset=final_asset, dest_addr=final_address, wait=False)
	
		if not execute:
			arb_log.error("Swap failed")
		else:
			arb_log.warning("Swap successful!!")

	await thor.account.eth.purge_client()
	await ftx.account.close()
	

if __name__ == '__main__':

	if DEBUGGING:
		network = 'MCTN'
		IPs = ["44.238.90.227"]
		# final_asset = 'BNB.BUSD-74E' 
		final_asset = 'ETH.ETH' # starting asset
	else:
		network = 'MCCN'
		IPs = ["136.244.65.26","159.65.212.234", "174.138.105.79"]
		final_asset = 'ETH.ETH' # starting asset
		# final_asset = 'BNB.BUSD-BD1' # starting asset

	# base_asset = 'ETH.ETH'
	# base_asset = 'BNB.BUSD-74E' 
	base_asset = 'BNB.BUSD-BD1' 
	# base_asset = 'THOR.RUNE'
	in_amount = 10000 # input amount
	sleep_time = 0.4

	thor_runner = Process(target=thor_run_handler({'network': network, 'IPs': IPs, 'final_asset': final_asset, 'base_asset': base_asset,
				 'in_amount': in_amount, 'sleep_time':sleep_time}))
	thor_runner.start()


# TODO in priority order:
	# Calc profit with gas
	# Add BUSD > ETH swap on other exchange
