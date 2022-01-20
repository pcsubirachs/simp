# using bitcoinlib
from bitcoinlib.mnemonic import Mnemonic

# Step 1
#get mnemonic randomly
# from bitcoinlib
mnem = Mnemonic().generate(strength=256, add_checksum=True)
print(mnem)

# from peter todd python-bitcoinlib
# import testnet on Bitcoin
# ‘mainnet’, ‘testnet’, and ‘regtest’ are the available chains from which you can select
import bitcoin
#bitcoin.SelectParams('testnet')

import bitcoin.rpc
 
proxy = bitcoin.rpc.Proxy()
print(proxy.getnewaddress())

# Step 2
#derive btc addresses deterministically