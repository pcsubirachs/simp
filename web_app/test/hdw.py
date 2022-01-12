from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.keys import HDKey

### 
# CLASS IMPLEMENTATION
###

x = 0
address_list = []

class HD_Wallet:

    def __init__(self):
        "Initialize attributes to describe a wallet."
        self.mnem_24 = Mnemonic().generate(strength=256, add_checksum=True)
        self.hd_key = HDKey().from_passphrase(self.mnem_24, password='', network='bitcoin', key_type='bip32', compressed=True, encoding=None, witness_type='legacy', multisig=False)
        self.child_public = self.hd_key.child_public(0)
        self.address = self.child_public.address()
        # get balance not working
        #self.balance = self.child_public.balance()

    def new_address(self):
        """ CALL TO CREATE NEW CHILD ADDRESS DERIVED FROM  """
        global x
        x += 1
        #print(x)

        for i in range(0, x):
            address = self.hd_key.child_public(i).address()
            #print(address)
            address_list.append(address)

        return str(address_list[-1:]).replace('[','').replace(']','').replace("'","")

# INITIALIZE USER
u_1 = HD_Wallet()

# PRINT STATEMENTS
print(" ")
print("##################")
print("    SEED PHRASE   ")
print("##################")
print(" ")
print(u_1.mnem_24)
print(" ")
print("##################")
print("WALLETS FROM CLASS")
print("##################")
print(" ")
print("USER 1 CHILD ADDRESS 1: ", u_1.new_address())
print("USER 1 CHILD ADDRESS 2: ", u_1.new_address())
print("USER 1 CHILD ADDRESS 3: ", u_1.new_address())


# GET BALANCE
print(" ")
print("##################")
print("   ~ BALANCE ~    ")
print("##################")
print(" ")

#print(u_1.balance)


# SEND/SIGN TRANSACTION
print(" ")
print("##################")
print(" ~ TRANSACTIONS ~ ")
print("##################")
print(" ")

# not working
#print(u_1.balance)

from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import HDKey

# figure out how to put in regtest mode?

t = Transaction()
prev_hash = '9c81f44c29ff0226f835cd0a8a2f2a7eca6db52a711f8211b566fd15d3e0e8d4'
t.add_input(prev_hash, output_n=0)
k = HDKey()
print(k)
print(t.add_output(100000, k.address()))
print(t.info())

##########################
# USING THE HDWALLET CLASS
##########################

print(" ")
print("##################")
print(" ~HDWALLET CLASS~ ")
print("   ~ON TESTNET~   ")
print("##################")
print(" ")

from bitcoinlib.wallets import *

if wallet_delete_if_exists('nicky-test-wallet'): 
    pass

w = Wallet.create('nicky-test-wallet')
print(w.info())

print("NICKY TEST WALLET: ", w.accounts())



# testnet wallet

w = wallet_create_or_open('bitcoinlib-testnet1', network='testnet', witness_type='segwit')
wk = w.new_key()
print("Deposit to address %s to get started" % wk.address)


# sent faucet funds to testnet wallet from
# https://bitcoinfaucet.uo1.net/

# The utxos_update() method only checks for new unspent outputs for existing keys. 
# Two other methods to receive transaction information for your wallet are the transactions_update() and scan() method. 
# Transactions_update retrieves all transactions from the service providers for your wallet's key: incoming and outgoing.

# now lets check the balance
w = wallet_create_or_open('bitcoinlib-testnet1', network='testnet', witness_type='segwit')
n_utxos = w.utxos_update()
if n_utxos:
    print("Found new unspent outputs (UTXO's), we are ready to create a transaction")
w.info()


# Now we have a wallet with coins and can create a transaction and send some coins. 
# The send_to() method creates a transactions and then broadcasts the signed transactions to the network.

w = wallet_create_or_open('bitcoinlib-testnet1', network='testnet', witness_type='segwit')
t = w.send_to('tb1qprqnf4dqwuphxs9xqpzkjdgled6eeptn389nec', 4000, fee=1000)
t.info()

# successfully pushed transaction to network

# When you run this code you should receive a transaction ID and t.pushed equals True. 
# You can also create an outgoing transactions with the HDWallet.send() method. 
# To spent all available UTXO's and empty a wallet the sweep() method is used.








#####
# EMBIT CODE EXAMPLE
###

#from ubinascii import hexlify
#from bitcoin import bip32, bip39, script
## NETWORKS contains all constants for HD keys and addresses
#from bitcoin.networks import NETWORKS
## we will use testnet:
#network = NETWORKS["test"]
#
#entropy = b'\x64\xd3\xe4\xa0\xa3\x87\xe2\x80\x21\xdf\x55\xa5\x1d\x45\x4d\xcf'
#
#recovery_phrase = bip39.mnemonic_from_bytes(entropy)
#print("Your recovery phrase:\n%s\n" % recovery_phrase)
#
## uncomment this line to make invalid mnemonic:
## recovery_phrase += " satoshi"
#
## you can check if recovery phrase is valid or not:
#if not bip39.mnemonic_is_valid(recovery_phrase):
#    raise ValueError("Meh... Typo in the recovery?")
#
## convert mnemonic and password to bip-32 seed
#seed = bip39.mnemonic_to_seed(recovery_phrase, password="mysecurepassword")
#print("Seed:", hexlify(seed).decode("ascii"))
#
## create HDKey from 64-byte seed
#root_key = bip32.HDKey.from_seed(seed)
## generate an account child key:
## purpose: 84h - BIP-84
## coin type: 1h - Testnet
## account: 0h - first account
#account = root_key.derive("m/84h/1h/0h")
## convert HD private key to HD public key
#account_pub = account.to_public()
## for Bitcoin Core: pure BIP-32 serialization
#print("\nYour xpub:", account_pub.to_base58(version=NETWORKS["test"]["xpub"]))
## for Electrum and others who cares about SLIP-0132
## used for bip-84 by many wallets
#print("\nYour zpub:", account_pub.to_base58(version=NETWORKS["test"]["zpub"]))
#
#print("\nLegacy addresses:")
#xpub_bip44 = root_key.derive("m/44h/1h/0h").to_public()
#print("Legacy xpub:", xpub_bip44.to_base58(version=network["xpub"]))
#for i in range(5):
#    # m/0/i is used for receiving addresses and m/1/i for change addresses
#    pub = xpub_bip44.derive("m/0/%d" % i)
#    # get p2pkh script
#    sc = script.p2pkh(pub)
#    print("Address %i: %s" % (i, sc.address(network)))
#    
#print("\nSegwit addresses:")
#xpub_bip84 = root_key.derive("m/84h/1h/0h").to_public()
#print("Segwit zpub:", xpub_bip84.to_base58(version=network["zpub"]))
#for i in range(5):
#    pub = xpub_bip84.derive("m/0/%d" % i)
#    # get p2wsh script
#    sc = script.p2wpkh(pub)
#    print("Address %i: %s" % (i, sc.address(network)))
#    
#print("\nNested segwit addresses:")
#xpub_bip49 = root_key.derive("m/49h/1h/0h").to_public()
#print("Nested Segwit ypub:", xpub_bip49.to_base58(version=network["ypub"]))
#for i in range(5):
#    pub = xpub_bip49.derive("m/0/%d" % i)
#    # get p2sh(p2wpkh) script
#    sc = script.p2sh(script.p2wpkh(pub))
#    print("Address %i: %s" % (i, sc.address(network)))
