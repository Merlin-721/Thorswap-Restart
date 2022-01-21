def swap_out(x, Y, X):
	y = (x * Y * X) / (x + X)**2
	return y

def rebalance(x, y, Y, X):
	Y = Y - y
	X = X + x
	return X, Y

eth_external_price = 3500
rune_external_price = 8.6

# x is start asset (ETH)
x = 450 # ETH in amount
X = 755.21 # ETH depth

# y is end asset (RUNE)
Y = 1359780.40 # RUNE depth

# out amount
y = swap_out(x, Y, X)

Xnew, Ynew = rebalance(x, y, Y, X)
imp_price = (Y/X)*rune_external_price
target_price = 0.48*imp_price

print(f"Target price: {target_price}")
print(f"Initial implied price: {imp_price}")
print(f"Get {y:.2f} RUNE for {x} ETH")
print("New pool balances:")
print(f"ETH: {Xnew:.2f}, RUNE: {Ynew:.2f}")
print(f"End implied price: {(Ynew/Xnew)*rune_external_price}")
