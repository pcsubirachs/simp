# using bitcoinlib
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet

# Step 1
#get mnemonic randomly
# from bitcoinlib
mnem = Mnemonic().generate(strength=256, add_checksum=True)
print(mnem)

# Step 2
#derive btc addresses deterministically
#w = Wallet.create('simp', keys=mnem, network='bitcoin')
w = Wallet('simp')
simp_mnem = Wallet.mnemonic()
print(simp_mnem)

x = 10
for i in range(0, x):
    key = w.get_key(i)
    address = key.address
    print(address)

#key1 = w.get_key()
#key2 = w.get_key(1)
#addr1 = key1.address
#addr2 = key2.address
#print(addr1, addr2)
#
#
#addr_list = w.addresslist()[0]
#print(addr_list)