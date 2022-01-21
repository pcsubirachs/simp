# using bitcoinlib
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.encoding import to_hexstring

# Step 1
#get mnemonic randomly
# from bitcoinlib
mnem = Mnemonic().generate(strength=256, add_checksum=True)
print(mnem)
print("HEXSTRING: ", to_hexstring(Mnemonic().to_seed(mnem)))

# Step 2
#derive btc addresses deterministically
#w = Wallet.create('simp', keys=mnem, network='bitcoin')
w = Wallet('simp')
#simp_mnem = Wallet.mnemonic()
#print(simp_mnem)

# for loop to generate x amount of addresses
x = 10
# for i in range from 0 to x
for i in range(0, x):
    # generate a key for the w Wallet
    key = w.get_key(i)
    # generate an address from that key
    address = key.address
    # print the addres
    print(address)
    # wallet info
    #print(w.info())


# getting one key at a time
#key1 = w.get_key()
#key2 = w.get_key(1)
#addr1 = key1.address
#addr2 = key2.address
#print(addr1, addr2)
#

# getting any address from the list
addr_list = w.addresslist()[9]
print('repeat: ', addr_list)

# get wallet info
#print("WALLET INFO", w.addresslist()[9].info()) # Shows wallet information, keys, transactions and UTXO's



# implement python-bitcoinlib by peter todd here
