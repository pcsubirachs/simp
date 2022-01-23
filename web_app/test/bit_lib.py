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
utxos = wallet.get_unspents()
print("utxo's: ", utxos)
tx_hist = wallet.get_transactions()
print('transaction history: ', tx_hist)

# create a transaction, then broadcast it
#create_tx = wallet.create_transaction([('tb1q2nf9knx0fsdp4glpyxntuxa8slpjjsyhm8ccyh', 0.00004924, 'btc')])
create_send = wallet.send([('tb1q2nf9knx0fsdp4glpyxntuxa8slpjjsyhm8ccyh', 0.00004924, 'btc')])
print("creating tx: ", create_send)


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

# import from seed

#print('')
#print('################')
#print('#### IMPORT ####')
#print('################')
#print('')
##key = Key.from_der(\xa3\x14|d\xd7)7\xf8s\xac\x96\xf2\x04\x87\xea\x94<vx8'\xb0\t\xe8Y#\xb5\x8e\xb4^=\xc7e\x82\x06[\n'!\xfaP\xcd\x01\xa7\xa0\xa3\xeb\x84Q\xd6\xca,f\xe8\x11\x9f2\xc6\x93L\xa0\t,\xd6)
##print(key)
#key = Key.from_hex('ebc33ff442c26015204c41b035728e2d5372d3846369f45eb241cc7881fd81a4d81469bc2dcb0a2e36584375c0d1a8f97e757b716a631cb6135a12b4b7c0a367')
#print(key.address)