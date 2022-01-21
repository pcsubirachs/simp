# using bitcoinlib
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.encoding import to_hexstring
from pprint import pprint
from bitcoinlib.keys import *

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

# example
#
# Hierarchical Deterministic Key Class and Child Key Derivation Examples
#
print("\n=== Generate random HD Key on testnet ===")
hdk = HDKey(network='testnet')
print("Random BIP32 HD Key on testnet %s" % hdk.wif())

print("\n=== Import HD Key from seed ===")
k = HDKey.from_seed('000102030405060708090a0b0c0d0e0f')
print("HD Key WIF for seed 000102030405060708090a0b0c0d0e0f:  %s" % k.wif())
print("Key type is : %s" % k.key_type)

print("\n=== Generate random Bitcoin key ===")
lk = HDKey(network='bitcoin')
lk.info()

print("\n=== Import simple private key as HDKey ===")
k = HDKey('L5fbTtqEKPK6zeuCBivnQ8FALMEq6ZApD7wkHZoMUsBWcktBev73')
print("HD Key WIF for Private Key L5fbTtqEKPK6zeuCBivnQ8FALMEq6ZApD7wkHZoMUsBWcktBev73:  %s" % k.wif())
print("Key type is : %s" % k.key_type)

print("\n=== Derive path with Child Key derivation ===")
print("Derive path path 'm/0H/1':")
print("  Private Extended WIF: %s" % k.subkey_for_path('m/0H/1').wif())
print("  Public Extended WIF : %s\n" % k.subkey_for_path('m/0H/1').wif_public())

print("\n=== Test Child Key Derivation ===")
print("Use the 2 different methods to derive child keys. One through derivation from public parent, "
      "and one thought private parent. They should be the same.")
K = HDKey('xpub6ASuArnXKPbfEVRpCesNx4P939HDXENHkksgxsVG1yNp9958A33qYoPiTN9QrJmWFa2jNLdK84bWmyqTSPGtApP8P'
          '7nHUYwxHPhqmzUyeFG')
k = HDKey('xprv9wTYmMFdV23N21MM6dLNavSQV7Sj7meSPXx6AV5eTdqqGLjycVjb115Ec5LgRAXscPZgy5G4jQ9csyyZLN3PZLxoM'
          '1h3BoPuEJzsgeypdKj')

index = 1000
pub_with_pubparent = K.child_public(index).address()
pub_with_privparent = k.child_private(index).address()
if pub_with_privparent != pub_with_pubparent:
    print("Error index %4d: pub-child %s, priv-child %s" % (index, pub_with_privparent, pub_with_pubparent))
else:
    print("Child Key Derivation for key %d worked!" % index)
    print("%s == %s" % (pub_with_pubparent, pub_with_privparent))


#
# Addresses
#
print("\n=== Deserialize address ===")
pprint(deserialize_address('1HsZBGm6nNGG1Moc3TL6S9DSGbnPbsSyW3'))

print("\n=== Deserialize bech32 address ===")
pprint(deserialize_address('bc1qtlktwxgx3xu3r7fnt04q06e4gflpvmm70qw66rjckzyc0n54elxqsgqlpy'))

print("\n=== Create addreses from public key ===")
pk = HDKey().public_hex
print("Public key: %s" % pk)
print(Address(pk).address)
print(Address(pk, script_type='p2sh').address)
print(Address(pk, encoding='bech32').address)
print(Address(pk, script_type='p2sh', encoding='bech32').address)


# implement python-bitcoinlib by peter todd here
