from mnemonic import *

#Initialize class instance, picking from available dictionaries:
#english
#chinese_simplified
#chinese_traditional
#french
#italian
#japanese
#korean
#spanish

#mnemo = Mnemonic(language)
mnemo = Mnemonic("english")

#Generate word list given the strength (128 - 256):

words = mnemo.generate(strength=256)
print('words: ', words)
#Given the word list and custom passphrase (empty in example), generate seed:

seed = mnemo.to_seed(words, passphrase="")
print('seed: ', seed)

# get seed to WIF format for input
hex_yes = seed.hex()
print('hex: ', hex_yes)
#Given the word list, calculate original entropy:

entropy = mnemo.to_entropy(words)
print('entropy: ', entropy)