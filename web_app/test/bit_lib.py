from bit import *

######################
#### TESTNET ONLY ####
######################

# reuse wallet by place wif into PrivateKeyTestnet

print('')
print('################')
print('## OLD WALLET ##')
print('################')
print('')
wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
print('privkey: ', wallet)
wif = wallet.to_wif()
print('wif: ', wif)
address = wallet.segwit_address
print('address: ', address)
btc_balance = wallet.get_balance('btc')
print('btc balance: ', btc_balance)
usd_balance = wallet.balance_as('usd')

# create new wallet

print('')
print('################')
print('## NEW WALLET ##')
print('################')
print('')
wallet_new = PrivateKeyTestnet()
print('privkey: ', wallet_new)
wif = wallet_new.to_wif()
print('wif: ', wif)
address = wallet_new.segwit_address
print('address: ', address)
btc_balance = wallet_new.get_balance('btc')
print('btc balance: ', btc_balance)
usd_balance = wallet_new.balance_as('usd')