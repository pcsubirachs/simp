# create a wallet from bitcoinlib
from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.mnemonic import Mnemonic

# create wallet

#passphrase = Mnemonic().generate()
#print(passphrase)
#w = Wallet.create("Wallet_sdflnflrnf", keys=passphrase, network='testnet')
#keyz_plz = w.get_key(wif='tprv8kfHYHiXjZ3GcipYwmb26xZdgH9f1CHpo4XgMANbC2zo4cdFLDTSeLKoch8QQpfCrd2)YWvyZdpnD6jomXV5fr8DB161JFpKvEn3UQgmi7Ry'
#print(keyz_plz)

############
# use wallet
############

# grab the wif private key from the output, place into main_key_object to keep it
w = Wallet(wallet="Wallet_sdflnflrnf",main_key_object='tprv8kfHYHiXjZ3GcipYwmb26xZdgH9f1CHpo4XgMANbC2zo4cdFLDTSeLKoch8QQpfCrd2)YWvyZdpnD6jomXV5fr8DB161JFpKvEn3UQgmi7Ry')
keyz_plz = w.get_key()
#print(keyz_plz)

# get fresh address
addr = keyz_plz.address
print(addr)