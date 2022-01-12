## pycoin notes

#### Definitions

ku : stands for "key utilities"

ku -h : help

usage: ku [-h] [-w] [-W] [-a] [-u] [-P] [-j] [-b [BRIEF [BRIEF ...]]] [-s SUBKEY]
          [-n {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}]
          [--override-network {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}]
          [item [item ...]]

Crypto coin utility ku ("key utility") to show information about Bitcoin or other cryptocoin data structures.

positional arguments:
  item                  a BIP0032 wallet key string; a WIF; a bitcoin address; an SEC (ie. a 66 hex chars starting with 02, 03 or a 130 hex chars starting with 04); the literal string "create" to create
                        a new wallet key using strong entropy sources; P:wallet passphrase (NOT RECOMMENDED); H:wallet passphrase in hex (NOT RECOMMENDED); E:electrum value (either a master public,
                        master private, or initial data); secret_exponent (in decimal or hex); x,y where x,y form a public pair (y is a number or one of the strings "even" or "odd"); hash160 (as 40 hex
                        characters). If this argument is missing, input data will be read from stdin.

optional arguments:
  -h, --help            show this help message and exit
  -w, --wallet          show just Bitcoin wallet key
  -W, --wif             show just Bitcoin WIF
  -a, --address         show just Bitcoin address
  -u, --uncompressed    show output in uncompressed form
  -P, --public          only show public version of wallet keys
  -j, --json            output as JSON
  -b [BRIEF [BRIEF ...]], --brief [BRIEF [BRIEF ...]]
                        brief output; display a single field
  -s SUBKEY, --subkey SUBKEY
                        subkey path (example: 0H/2/15-20)
  -n {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}, --network {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}
                        specify network
  --override-network {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}
                        override detected network type

Known networks codes: ARG (Argentum mainnet), AXE (Axe mainnet), BC (Blackcoin mainnet), BCH (Bcash mainnet), BSD (BitSend mainnet), BTC (Bitcoin mainnet), BTCD (BitcoinDark mainnet), BTDX (Bitcloud
mainnet), BTG (Bgold mainnet), BTX (BitCore mainnet), CHA (Chaucha mainnet), DASH (Dash mainnet), DCR (Decred mainnet), DCRT (Decred testnet), DFC (DEFCOIN mainnet), DGB (Digibyte mainnet), DOGE
(Dogecoin mainnet), FAI (Faircoin mainnet), FTC (Feathercoin mainnet), FTX (Feathercoin testnet), GRS (Groestlcoin mainnet), JBS (Jumbucks mainnet), LTC (Litecoin mainnet), MEC (Megacoin mainnet), MONA
(Monacoin mainnet), MZC (Mazacoin mainnet), PIVX (PIVX mainnet), POLIS (Polis mainnet), RIC (Riecoin mainnet), STRAT (Strat mainnet), TBTX (BitCore testnet3), TDASH (Dash testnet), TMONA (Monacoin
testnet4), TPIVX (PIVX testnet), TVI (Viacoin testnet), VIA (Viacoin mainnet), XCH (Bcash testnet3), XDT (Dogecoin testnet), XLT (Litecoin testnet), XMY (Myriadcoin mainnet), XRT (Bitcoin regtest), XTG
(Bgold testnet), XTN (Bitcoin testnet3), ZEC (Zcash mainnet)


##### Cryptograhpy 

ecdsa : elliptical curve digital signature

Has a private key, and a public key, a number between 1 and 2^256

--- input ---
ku 1

--- output ---
input                        : 1
network                      : Bitcoin mainnet
symbol                       : BTC
secret exponent              : 1
 hex                         : 1
wif                          : KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU73sVHnoWn
 uncompressed                : 5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAnchuDf
public pair x                : 55066263022277343669578718895168534326250603453777594175500187360389116729240
public pair y                : 32670510020758816978083085130507043184471273380659243275938904335757337482424
 x as hex                    : 79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
 y as hex                    : 483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
y parity                     : even
key pair as sec              : 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
 uncompressed                : 0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798\
                                 483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
hash160                      : 751e76e8199196d454941c45d1b3a323f1433bd6
 uncompressed                : 91b24bf9f5288532960ac687abb035127b1d28a5
Bitcoin address              : 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
Bitcoin address uncompressed : 1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm
Bitcoin segwit address       : bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4
p2sh segwit                  : 3JvL6Ymt8MVWiCNHC7oWU6nLeHNJKLZGLN
 corresponding p2sh script   : 0014751e76e8199196d454941c45d1b3a323f1433bd6


For a given X coordinate, there are two possible Y coordinates on the curve.


"key_pair_as_sec": A public key. This format is used in the blockchain, which is why it's important. Defined by a cryptographic standard, stored with prefix of "02" or "03" depending on whether the Y coordinate is even or odd. If prefixed with 04, it is an X coordinate.

hash 160 : 160 bit 20 byte number, which is the SHA256 hash of the sec number, both compressed and uncompressed versions. This is used to derive the Bitcoin address. 

As you move down the output, information is lost. Once you get down to the public pair, there is no way to go back up.

You can input any of these output values to get a similar output. 

input :
ku 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798

output :
input                        : 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
network                      : Bitcoin mainnet
symbol                       : BTC
public pair x                : 55066263022277343669578718895168534326250603453777594175500187360389116729240
public pair y                : 32670510020758816978083085130507043184471273380659243275938904335757337482424
 x as hex                    : 79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
 y as hex                    : 483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
y parity                     : even
key pair as sec              : 0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
 uncompressed                : 0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798\
                                 483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
hash160                      : 751e76e8199196d454941c45d1b3a323f1433bd6
 uncompressed                : 91b24bf9f5288532960ac687abb035127b1d28a5
Bitcoin address              : 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH
Bitcoin address uncompressed : 1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm
Bitcoin segwit address       : bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4
p2sh segwit                  : 3JvL6Ymt8MVWiCNHC7oWU6nLeHNJKLZGLN
 corresponding p2sh script   : 0014751e76e8199196d454941c45d1b3a323f1433bd6

If you pass in the hash, all you get out is the address, you can't work your way back up to the sec. There is no way to know if this is a compressed address or an uncompressed address.

input :
ku 751e76e8199196d454941c45d1b3a323f1433bd6

output :
input           : 751e76e8199196d454941c45d1b3a323f1433bd6
network         : Bitcoin mainnet
symbol          : BTC
hash160         : 751e76e8199196d454941c45d1b3a323f1433bd6
Bitcoin address : 1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH


The main components are the wif, the public pair x and y also known as the public key, and the bitcoin address. People generally only see the bitcoin address and the wif.


## BIP32 : Deterministic Hieracrchy of Keys

You can use random entropy with ku to create a fresh pair of keys. 

input :
ku create

output :
warning: can't open gpg, can't use as entropy source

input                        : create
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xprv9s21ZrQH143K2r3cutWusmGsPFVMmTe6g8oWFRSjy84dBEBUJigiLWdeSnSgLR\
                                 eHa8ERZpLWgpVgPLkBsYxaGwXRAYbAdQgqUWpzo317vm5
public version               : xpub661MyMwAqRbcFL861v3vEuDbwHKrAvMx3Mj73orMXTbc42WcrFzxtJx8J5rRXx\
                                 NfsrtWTUCtxjKuDC5hnCxaJewaBT7wjtUy8Bpc7EBxLJi
tree depth                   : 0
fingerprint                  : bab519b4
parent f'print               : 00000000
child index                  : 0
chain code                   : 4f1f25324c50d396525a7030987f3c72457973d592c4464aefbd8593d38d7338
private key                  : yes
secret exponent              : 57762808096945554225530302304495380117938571218058781982267998505358940859706
 hex                         : 7fb4973ebdde806a69a5f00434da329e2675f4df1100b719affe9a62360a6d3a
wif                          : L1VxG1eipwyXyYPH1wezSiLh2w6NS1YvqfmdWJjKXUeQkW68aPR6
 uncompressed                : 5JnXePMKzY2w9HB2pLdhezrKayD6JuEaVhW9Ghim5Bo5vrMND6h
public pair x                : 83679072426807913405423695532836743601114355844437867457678161240365097984079
public pair y                : 18840827588916682487344003586655777943675251453327356677967112384907849606195
 x as hex                    : b900ad354b1868dff4d8588691271b4913e7a913b212845caf0ca0d30696a04f
 y as hex                    : 29a787cfc4bd1557e15fa5bf05b928d9fde236a193af88eb3a3c699ef259a433
y parity                     : odd
key pair as sec              : 03b900ad354b1868dff4d8588691271b4913e7a913b212845caf0ca0d30696a04f
 uncompressed                : 04b900ad354b1868dff4d8588691271b4913e7a913b212845caf0ca0d30696a04f\
                                 29a787cfc4bd1557e15fa5bf05b928d9fde236a193af88eb3a3c699ef259a433
hash160                      : bab519b43a2d98e80aa3d77fb6bb8fbd4bf289eb
 uncompressed                : 5d7c75f4805b3e0b131cde0c013312985e2ad2e8
Bitcoin address              : 1J2DdkvWBMhdM5h2iCrFzntUd526QLLezw
Bitcoin address uncompressed : 19XJwXV3yLVYsfPkYxLaZ33LEsdvF8Tj7h
Bitcoin segwit address       : bc1qh263ndp69kvwsz4r6almdwu0h49l9z0tvtk5rf
p2sh segwit                  : 3MjCnXDkdZMTm77dbwVQjVT3RsD66xhrMk
 corresponding p2sh script   : 0014bab519b43a2d98e80aa3d77fb6bb8fbd4bf289eb


As a simple example similar to a brain wallet where "foo" is the word.

To get a corresponding WIF 

input :
ku P:foo -W

output :
L26c3H6jEPVSqAr1usXUp9qtQJw6NHgApq6Ls4ncyqtsvcq2MwKH

Get the BIP32 key that corresponds to that node

ku P:foo -w
xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M8ZMjxncCKZKgb5jZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq

If you feed in the BIP32 key directly, you'll find the same wif ouput.

input :
ku xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M8ZMjxncCKZKgb5jZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq

output :
input                        : xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M8ZMjxncCKZKgb5j\
                                 ZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M8ZMjxncCKZKgb5j\
                                 ZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq
public version               : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
tree depth                   : 0
fingerprint                  : 5d353a2e
parent f'print               : 00000000
child index                  : 0
chain code                   : 5eeb1023fd6dd1ae52a005ce0e73420821e1d90e08be980a85e9111fd7646bbc
private key                  : yes
secret exponent              : 65825730547097305716057160437970790220123864299761908948746835886007793998275
 hex                         : 91880b0e3017ba586b735fe7d04f1790f3c46b818a2151fb2def5f14dd2fd9c3
wif                          : L26c3H6jEPVSqAr1usXUp9qtQJw6NHgApq6Ls4ncyqtsvcq2MwKH
 uncompressed                : 5JvNzA5vXDoKYJdw8SwwLHxUxaWvn9mDea6k1vRPCX7KLUVWa7W
public pair x                : 81821982719381104061777349269130419024493616650993589394553404347774393168191
public pair y                : 58994218069605424278320703250689780154785099509277691723126325051200459038290
 x as hex                    : b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f
 y as hex                    : 826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52
y parity                     : even
key pair as sec              : 02b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f
 uncompressed                : 04b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f\
                                 826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52
hash160                      : 5d353a2ecdb262477172852d57a3f11de0c19286
 uncompressed                : e5bd3a7e6cb62b4c820e51200fb1c148d79e67da
Bitcoin address              : 19Vqc8uLTfUonmxUEZac7fz1M5c5ZZbAii
Bitcoin address uncompressed : 1MwkRkogzBRMehBntgcq2aJhXCXStJTXHT
Bitcoin segwit address       : bc1qt56n5tkdkf3ywutjs5k40gl3rhsvry5xk3m9g3
p2sh segwit                  : 37fVADSztbVGWoHYYw4ViPAcGqZ85QDmVi
 corresponding p2sh script   : 00145d353a2ecdb262477172852d57a3f11de0c19286

Get the address

ku P:foo -a
19Vqc8uLTfUonmxUEZac7fz1M5c5ZZbAii

Get the uncompressed address

ku P:foo -a -w
xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M8ZMjxncCKZKgb5jZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq

You can use ku to generate child nodes. You've got your node at the top, and now a 0th child sub node.
You can see in the outuput the tree depth is now 1 instead of 0, the parent fingerprint maps to the fingerprint of the original key, the child index is 0. All of this can be derived from the wallet key. 

input :

ku P:foo -s0  

output :

input                        : P:foo
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xprv9uat5uhfTLHoaSMqAueV7r41Gtxz4U9Y6TcJfanP1HYaq6AeWdzc5DJowtsZiw\
                                 wKNLUHMJQbiQZFMPNWMR51g8SdHbhcWeJTYzrtUroz4Ze
public version               : xpub68aEVREZHhr6nvSJGwBVUyzjpvoUTvsPTgXuTyBzZd5ZhtVo4BJrd1dHoCKAVf\
                                 ANDz9WMQrbKTj3pyjp7uCq8otBcsoZZPmFY4eNEYUgaec
tree depth                   : 1
fingerprint                  : eba8904f
parent f'print               : 5d353a2e
child index                  : 0
chain code                   : 75b488c3a768fdc65ea5777135bb39e4919fc90a4127490dd94dd462e3c04ab5
private key                  : yes
secret exponent              : 23166188151390713667442369645908462109279604822999991357451454304800423662420
 hex                         : 3337990bca8c69137c2de46ef968bdfd3a47168ddf391696358bd17f8a4dd354
wif                          : KxwGdpvzjzD5r6Qwg5Ev7gAv2Wn53tmSFfingBThhJEThQFcWPdj
 uncompressed                : 5JCqraWuWDxkh87nTyhJvd4c8978iSKgFemp3zCVFZuSXxoB4YF
public pair x                : 50987278974866364252820838253329192886454871984434391834424022577998929751473
public pair y                : 3927524270667234579686765978604499875336290755823599824183018479296022266845
 x as hex                    : 70b9c6f7cdcc3b9fb00828b57894ea389001e5f0b28112b56497a5bcbfd26db1
 y as hex                    : 8aee663d13c8fdf6ffcfbe3f15e95891f302c71f496cd36073e7da3ed9743dd
y parity                     : odd
key pair as sec              : 0370b9c6f7cdcc3b9fb00828b57894ea389001e5f0b28112b56497a5bcbfd26db1
 uncompressed                : 0470b9c6f7cdcc3b9fb00828b57894ea389001e5f0b28112b56497a5bcbfd26db1\
                                 08aee663d13c8fdf6ffcfbe3f15e95891f302c71f496cd36073e7da3ed9743dd
hash160                      : eba8904fdf351d57f1d7e8c0d847fcdbfdfb0297
 uncompressed                : 305df282f9a6a4711df0025e38acdb39f9a811f1
Bitcoin address              : 1NV3j6NgeAkWBytXiQkWxMFLBtTdbef1rp
Bitcoin address uncompressed : 15QjynKrQdxSi6d3xiUiEHFXxMNNPKoF59
Bitcoin segwit address       : bc1qaw5fqn7lx5w40uwharqds3lum07lkq5hfspe05
p2sh segwit                  : 3EthJtWdBTL28bbrHbV9JYD7XWvVoUeNA8
 corresponding p2sh script   : 0014eba8904fdf351d57f1d7e8c0d847fcdbfdfb0297


Retrieve just the address of the child node

ku P:foo -s0 -a

1NV3j6NgeAkWBytXiQkWxMFLBtTdbef1rp

Uncompressed address

ku P:foo -s0 -w

xprv9uat5uhfTLHoaSMqAueV7r41Gtxz4U9Y6TcJfanP1HYaq6AeWdzc5DJowtsZiwwKNLUHMJQbiQZFMPNWMR51g8SdHbhcWeJTYzrtUroz4Ze

You can create as many child nodes as you'd like

You can create a range of nodes

ku P:foo -s0-10 -a

1NV3j6NgeAkWBytXiQkWxMFLBtTdbef1rp
1UNhze6hkv2idrr7UH7LW3HZvNoQmLKho
1FZKvJujPFLshEZFHtuXdXfiZPWehKs5dg
19LCMSzwoPC2MQZPyd7PvpQ2TsCM99wykQ
19DLcJRC9bRcxLWQDyYqobAfHykbjZtV4U
1A5gzi3VHgJJQbT4ko9ZkjvcPvLeeA6NGi
1PD3ss27D3rFCtNGMvP5zshfBYgxVRZFM7
1FG4qXtMtgFNtjDE4sPWRmMgAZmWTtxS5q
13myk8hG2ghmdCcQ8cmUVLNLersj72aoqv
1NoWPpYD26hyuiY2kbKaPq3uWakWxfoxua
1CRJpBDkkiymzzCszwSn2pbRNh6EsMtvD5

Get the corresponding BIP32 nodes

ku P:foo -s0-10 -w

xprv9uat5uhfTLHoaSMqAueV7r41Gtxz4U9Y6TcJfanP1HYaq6AeWdzc5DJowtsZiwwKNLUHMJQbiQZFMPNWMR51g8SdHbhcWeJTYzrtUroz4Ze
xprv9uat5uhfTLHockgkNDfN5maaG4Gm8kKuoXbcHNc5ckWcauaUpMY2DNxaKUY3diqTSPggEaHU2hd59Umnva19wHJYvg8mpyyog8N3PkMsk9f
xprv9uat5uhfTLHogUXGQXtcfrStivEgKKhQDUg4eW2quYQPVWvUn7YhACJ21txwJUbk8WJKTj4Rb7hCZVC81tU6wEZD7TSoKWqQKZjfhBHD1s9
xprv9uat5uhfTLHoh1r6j6UxBn94cnbop2Qs5i3Rz1NYMdZEBNa4u9qGoFqC6pUW6YurtzAedSXYEE17tvUMMvpL4Eo6o5MUvZbmLnQxjDpsd3J
xprv9uat5uhfTLHomcpcnVtT3M8vKLvWk85MW8tWbhooMfnH6TRbE3wkfPRUmGWDVmtEd2BtMKxY2znSJbbC7aMh3DemPAjQvFL4nqZhK7SHaYJ
xprv9uat5uhfTLHopHUsGxex2soJhWDRKb5FVu9rEKjaNNZGUWhrtgWigXCJqPafqKYAosYpgzw9L64C1HJvu2t54UJ9DYZWBsVcfHzUKUGhopL
xprv9uat5uhfTLHor4pRp24tWu9uKTsh8X5MFK7UL6pFZtDrQnp9XzogPncQzntHtZ23tMKPiUyPedgXb55Z7rYrngBNuzwCbyNUXGUraeicShc
xprv9uat5uhfTLHotJ6A9975wtLJbwBqSrER9fbReXdcwBtDNWJX2LWsumZQD3o3ypufv6JxH2k5FdJC4XFR65m3UQEeievrMivEWMyKA2RJswm
xprv9uat5uhfTLHov1KwMTD6t6xTz9vXkDqQEfEmBse3z47Ji3dZYmm2MA4vNHmQyXkN9JKetTW6PCXHVGc5mXSFmZqGrdk1vEGsNG6cLv5NXT8
xprv9uat5uhfTLHozGhPVHrVsL2iVy4uXXfKeDnGzavFzzf2iMFBUu9vSzmBFUoD6frq5o1sYLPocoaWo2xnqeeAHmVXBJ9gf8LypAEftHTc3Bh
xprv9uat5uhfTLHp31Y2AMWndxq7uVH11yQY8neX9SS2A1LmykWBDkWh7Mz2MvfvHeiVR5u99yXuyqhEZKvgKgTpSQCiJmMN6vWy44TAiYnqHMa

Get the corresponding wifs

ku P:foo -s0-10 -W

KxwGdpvzjzD5r6Qwg5Ev7gAv2Wn53tmSFfingBThhJEThQFcWPdj
L2VbYJ5CX5RukRrXgSRs2A49XHABz5UMRt14bF3bzJeDGHJn2ALB
KxkqD1CTR4C28JkCu2PpFoNLtJjuZgXW1T5wjJ8iqi81Rz5Y1828
L4gxgoZugkyQqhCyTHDNDvAzqRPozs3vjjFfQXzzCBgz1iKzQAii
L3iu7pDXFqJ53NkHxwFhhXiG1MMnJG46Ab6VhzGwaw5FeLoJqks2
KzFZadNu81enWFLRLXt4ACqsGriW4gQ4ou5ZfVUZutrRF8uoTyrA
L2nUc8tUPHHSRHe2wkWv2wwoszv3p9X1hASzfyf9bYi81w1R2AVx
L352SNyuqHvNH8PpQYiVzUiifaPMfEG1fJ52MRCrrJDwUcKGYt5F
L5BYPTRGyiLJGfucqsai7t5jskmLbRhGRJ4AEKaJzQWDTJBfCP7g
KzD1j134pMHZ35U8tgkwe9oCCnYGiDNPQAg4imLqPdqWeYJQ2rKB
L1kv16ChRQ2aYYYFUSSyRUa1B2EtUHCKAZkw1aP8Z4KgfHMNK37N

Now when viewing the public version of the key, there is no "xprv" in the wallet key, it is now "xpub"

ku P:foo -P       

input                        : P:foo
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
tree depth                   : 0
fingerprint                  : 5d353a2e
parent f'print               : 00000000
child index                  : 0
chain code                   : 5eeb1023fd6dd1ae52a005ce0e73420821e1d90e08be980a85e9111fd7646bbc
private key                  : no
public pair x                : 81821982719381104061777349269130419024493616650993589394553404347774393168191
public pair y                : 58994218069605424278320703250689780154785099509277691723126325051200459038290
 x as hex                    : b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f
 y as hex                    : 826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52
y parity                     : even
key pair as sec              : 02b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f
 uncompressed                : 04b4e599dfa44555a4ed38bcfff0071d5af676a86abf123c5b4b4e8e67a0b0b13f\
                                 826d8b4d3010aea16ff4c1c1d3ae68541d9a04df54a2c48cc241c2983544de52
hash160                      : 5d353a2ecdb262477172852d57a3f11de0c19286
 uncompressed                : e5bd3a7e6cb62b4c820e51200fb1c148d79e67da
Bitcoin address              : 19Vqc8uLTfUonmxUEZac7fz1M5c5ZZbAii
Bitcoin address uncompressed : 1MwkRkogzBRMehBntgcq2aJhXCXStJTXHT
Bitcoin segwit address       : bc1qt56n5tkdkf3ywutjs5k40gl3rhsvry5xk3m9g3
p2sh segwit                  : 37fVADSztbVGWoHYYw4ViPAcGqZ85QDmVi
 corresponding p2sh script   : 00145d353a2ecdb262477172852d57a3f11de0c19286

Get the first 5 addresses using the xpub

ku xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtSVYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy -s0-5 



input                        : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub68aEVREZHhr6nvSJGwBVUyzjpvoUTvsPTgXuTyBzZd5ZhtVo4BJrd1dHoCKAVf\
                                 ANDz9WMQrbKTj3pyjp7uCq8otBcsoZZPmFY4eNEYUgaec
tree depth                   : 1
fingerprint                  : eba8904f
parent f'print               : 5d353a2e
child index                  : 0
chain code                   : 75b488c3a768fdc65ea5777135bb39e4919fc90a4127490dd94dd462e3c04ab5
private key                  : no
public pair x                : 50987278974866364252820838253329192886454871984434391834424022577998929751473
public pair y                : 3927524270667234579686765978604499875336290755823599824183018479296022266845
 x as hex                    : 70b9c6f7cdcc3b9fb00828b57894ea389001e5f0b28112b56497a5bcbfd26db1
 y as hex                    : 8aee663d13c8fdf6ffcfbe3f15e95891f302c71f496cd36073e7da3ed9743dd
y parity                     : odd
key pair as sec              : 0370b9c6f7cdcc3b9fb00828b57894ea389001e5f0b28112b56497a5bcbfd26db1
 uncompressed                : 0470b9c6f7cdcc3b9fb00828b57894ea389001e5f0b28112b56497a5bcbfd26db1\
                                 08aee663d13c8fdf6ffcfbe3f15e95891f302c71f496cd36073e7da3ed9743dd
hash160                      : eba8904fdf351d57f1d7e8c0d847fcdbfdfb0297
 uncompressed                : 305df282f9a6a4711df0025e38acdb39f9a811f1
Bitcoin address              : 1NV3j6NgeAkWBytXiQkWxMFLBtTdbef1rp
Bitcoin address uncompressed : 15QjynKrQdxSi6d3xiUiEHFXxMNNPKoF59
Bitcoin segwit address       : bc1qaw5fqn7lx5w40uwharqds3lum07lkq5hfspe05
p2sh segwit                  : 3EthJtWdBTL28bbrHbV9JYD7XWvVoUeNA8
 corresponding p2sh script   : 0014eba8904fdf351d57f1d7e8c0d847fcdbfdfb0297

input                        : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub68aEVREZHhr6qEmDUFCNSuXJp67FYD3mAkXD5m1hB63bThudMtrGmBH4AjsxHQ\
                                 yt64jAgfRPosuZa2U6LXDUF3NADBha6ics996eiXdZngw
tree depth                   : 1
fingerprint                  : 052d59d3
parent f'print               : 5d353a2e
child index                  : 1
chain code                   : 5e532890a1257134b02e1fd02e5584dc523659810343053fdcdef33aadad8901
private key                  : no
public pair x                : 89807432816009602976906242117043443025900718907470740875099556639385944867007
public pair y                : 64848699134590900058838460257784018640930212155472103022533323701074271296174
 x as hex                    : c68d34a5c930dd8d249884bace979d187dd645c71f9fa30c9b4153d03fc840bf
 y as hex                    : 8f5f1020f0e718f81177b0385aaa52a4585dcbac029718dd5e48cc9a654e5aae
y parity                     : even
key pair as sec              : 02c68d34a5c930dd8d249884bace979d187dd645c71f9fa30c9b4153d03fc840bf
 uncompressed                : 04c68d34a5c930dd8d249884bace979d187dd645c71f9fa30c9b4153d03fc840bf\
                                 8f5f1020f0e718f81177b0385aaa52a4585dcbac029718dd5e48cc9a654e5aae
hash160                      : 052d59d3821d1267f931f8d4849ce8bcf8173e38
 uncompressed                : 10805b0ee6b814805291974a940f4328a84d8178
Bitcoin address              : 1UNhze6hkv2idrr7UH7LW3HZvNoQmLKho
Bitcoin address uncompressed : 12WFaP1JsinSF21gnFF81GH25d9ktVUdTo
Bitcoin segwit address       : bc1qq5k4n5uzr5fx07f3lr2gf88ghnupw03cc2flmz
p2sh segwit                  : 3KtU5NrebuLr9zKzP1MhDTAx981TQDYtTV
 corresponding p2sh script   : 0014052d59d3821d1267f931f8d4849ce8bcf8173e38

input                        : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub68aEVREZHhr6txbjWZRd2zPdGx5AinRFahbfStSTTswNNKFdKerwhzcVsAwm3F\
                                 nDHM6ekmXdWRDxFEke6Sir8d1w7Y3sMfe1YVg32ic92HQ
tree depth                   : 1
fingerprint                  : 9faedd58
parent f'print               : 5d353a2e
child index                  : 2
chain code                   : d419a7564eba275817bd381e1aec07afccc1de302a5d101989cc951ad7cf0d16
private key                  : no
public pair x                : 77282402810046154288415342400489560575936318622874494581021732499859086289644
public pair y                : 85448158840544475293895714045343297662293367521636576692051437469892771814810
 x as hex                    : aadc4a366de404bfffa59156c44f4c8dddffdc3dfef0e709c9a05f9ce530aaec
 y as hex                    : bce9f1ab5cd5890347af462e1e030d5c38c2121f7d1da24e9b7b5891b8039d9a
y parity                     : even
key pair as sec              : 02aadc4a366de404bfffa59156c44f4c8dddffdc3dfef0e709c9a05f9ce530aaec
 uncompressed                : 04aadc4a366de404bfffa59156c44f4c8dddffdc3dfef0e709c9a05f9ce530aaec\
                                 bce9f1ab5cd5890347af462e1e030d5c38c2121f7d1da24e9b7b5891b8039d9a
hash160                      : 9faedd58a05f56ebdd8f0be63daecdcde0035d2d
 uncompressed                : eff2647d412d54aa062effebd29560941187b6c6
Bitcoin address              : 1FZKvJujPFLshEZFHtuXdXfiZPWehKs5dg
Bitcoin address uncompressed : 1NsisaR9STa6TMVvy6WNPo2adYLBx7Edeb
Bitcoin segwit address       : bc1qn7hd6k9qtatwhhv0p0nrmtkdehsqxhfdwgse63
p2sh segwit                  : 3Csq9viwNyF4DNm2neaepmxeUBXwHFxAwd
 corresponding p2sh script   : 00149faedd58a05f56ebdd8f0be63daecdcde0035d2d

input                        : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub68aEVREZHhr6uVvZq81xYv5oApSJDV8iSvy2nPn9uy6D4AuDSh9XM49fx4nGjW\
                                 SZh5YYF6CoyCSDBkTsxradCYiPjUpssxez4KcZ3f3iuJT
tree depth                   : 1
fingerprint                  : 5b6262dc
parent f'print               : 5d353a2e
child index                  : 3
chain code                   : 0a58cac9f81acf60a02cb3d1996013925c80c71066bf8018ad7d8f97526e83ea
private key                  : no
public pair x                : 57679717998409371733797327355869524226109629845892420304205662472672587568056
public pair y                : 92082029723190455449967127427645372768990826427962093181733837722323916355252
 x as hex                    : 7f85903fb2378b484c39e5a46f927da6fa7336ee12634723955f2ae3f01053b8
 y as hex                    : cb9494f62b9f542c00ab293721ff4030103305a3ae29e2b09ac228609ee6f6b4
y parity                     : even
key pair as sec              : 027f85903fb2378b484c39e5a46f927da6fa7336ee12634723955f2ae3f01053b8
 uncompressed                : 047f85903fb2378b484c39e5a46f927da6fa7336ee12634723955f2ae3f01053b8\
                                 cb9494f62b9f542c00ab293721ff4030103305a3ae29e2b09ac228609ee6f6b4
hash160                      : 5b6262dcc0380aa74ebb6d7111b7c97c6184988f
 uncompressed                : 9f5dbb8e62ba6161de0bec3a673d3d0d6cb9c7b2
Bitcoin address              : 19LCMSzwoPC2MQZPyd7PvpQ2TsCM99wykQ
Bitcoin address uncompressed : 1FXejAEL4b5uTtg6kGHpT88qnDvfLtot5p
Bitcoin segwit address       : bc1qtd3x9hxq8q92wn4md4c3rd7f03scfxy00sj4g5
p2sh segwit                  : 3LAWpF1HDsA1JG4Et4eRFFaaQgucnA6qEo
 corresponding p2sh script   : 00145b6262dcc0380aa74ebb6d7111b7c97c6184988f

input                        : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub68aEVREZHhr6z6u5tXRTQV5esNm19aoCsMp7Q6DQv1KFyFkjmbG1DBjxcWA6Uw\
                                 zGtedf5HYNvDX9qxE8nyA7LxHnVy4xuBWfzRNMekE35aB
tree depth                   : 1
fingerprint                  : 5a165dc3
parent f'print               : 5d353a2e
child index                  : 4
chain code                   : d8ae32298574da770bb13c8d1fca61235685a939369d4de2ccc081344fa25fff
private key                  : no
public pair x                : 5720150465431372184303490133581840211926410638032184650933859394814521457278
public pair y                : 1006418695027384411127497636177062201660068305785949461230322070618849946084
 x as hex                    : ca57d8ce4716af6a762a01fc21c6dc4a5eadf862a9333aecef039c85b113a7e
 y as hex                    : 2399ce0233b509faa61a836c42f7f173fba4ebe59e9eb74910dae67441c29e4
y parity                     : even
key pair as sec              : 020ca57d8ce4716af6a762a01fc21c6dc4a5eadf862a9333aecef039c85b113a7e
 uncompressed                : 040ca57d8ce4716af6a762a01fc21c6dc4a5eadf862a9333aecef039c85b113a7e\
                                 02399ce0233b509faa61a836c42f7f173fba4ebe59e9eb74910dae67441c29e4
hash160                      : 5a165dc3c05c56bf754a3d114dab71f7fe03d419
 uncompressed                : d6af509931fa9ebfb8fe71055b0543a08ec12ada
Bitcoin address              : 19DLcJRC9bRcxLWQDyYqobAfHykbjZtV4U
Bitcoin address uncompressed : 1La9d98YV1YsmWkE7Y1Rm7eoKAj2dR1pPD
Bitcoin segwit address       : bc1qtgt9ms7qt3tt7a2285g5m2m37llq84qenxl4ct
p2sh segwit                  : 3HH116aspwwq6Ab9A1YqXzDfMRb3J729nj
 corresponding p2sh script   : 00145a165dc3c05c56bf754a3d114dab71f7fe03d419

input                        : xpub661MyMwAqRbcFVF9ULcqLdsEa5WnCCugQAcgNd9iEMQ31tgH6u4DLQWoQayvtS\
                                 VYFvXz2vPPpbXE1qpjoUFidhjFj82pVShWu9curWmb2zy
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xpub68aEVREZHhr72mZLNzBxQ1k3FY3uj3o6s85T2i9Bvi6FMK31SDpyEKWnggnTwV\
                                 4C9arVkTf3mmseHPhRX1CinoxPnTurziTAZzNBmVRE8VH
tree depth                   : 1
fingerprint                  : 639c2e98
parent f'print               : 5d353a2e
child index                  : 5
chain code                   : e48329b496b2a88349811d6dd1e9e823f5a590e147d47dd70b9ed5bca234120f
private key                  : no
public pair x                : 54561738128461250492129880054413749376094312377223990131970203406810654752680
public pair y                : 13798840315059813852842009824721659154625328609444013733641611853521322092643
 x as hex                    : 78a0d972953591dcf8f6220a0e1e5a2291b0a503604095d64a1e046ec8c0bfa8
 y as hex                    : 1e81dde9b0926b2b0587286684670938d0f995a00b11bd1cf78320c38f7da863
y parity                     : odd
key pair as sec              : 0378a0d972953591dcf8f6220a0e1e5a2291b0a503604095d64a1e046ec8c0bfa8
 uncompressed                : 0478a0d972953591dcf8f6220a0e1e5a2291b0a503604095d64a1e046ec8c0bfa8\
                                 1e81dde9b0926b2b0587286684670938d0f995a00b11bd1cf78320c38f7da863
hash160                      : 639c2e98539808eb087fa64543efc4dd7aaa5e4e
 uncompressed                : 5b5dcae72fe4526efb9a9458704a2c76a7bae7eb
Bitcoin address              : 1A5gzi3VHgJJQbT4ko9ZkjvcPvLeeA6NGi
Bitcoin address uncompressed : 19L6rHEr8pma1QuJgDHxcpmsRkvFV8iaa7
Bitcoin segwit address       : bc1qvwwzaxznnqywkzrl5ez58m7ym4a25hjw9pma3s
p2sh segwit                  : 3ELJbuAHwifoBaCWExbJcy5t9Za1PLjEzB
 corresponding p2sh script   : 0014639c2e98539808eb087fa64543efc4dd7aaa5e4e


Be aware that if you give out a child private key, a person could work their way back up to the top of the tree and retrieve that private key as well. To prevent this, you can use a hardened child node. 
This will create entirely new addresses which can't be traversed back up the tree. The tradeoff here is that you can traverse down the nodes with the private key, but not with the public key when it's been hardened.


ku P:foo -s0H

input                        : P:foo
network                      : Bitcoin mainnet
symbol                       : BTC
wallet key                   : xprv9uat5uhonzpmkkZSz4BkLFgnUhhR2ZLE9Q2oh1zeuG4SvcKdzZUJP9QyxyUmJX\
                                 3BxJRmtHAiQLaFG34619xsGJ7wD5BNCvMiU3LA7sfr3kE
public version               : xpub68aEVREhdNP4yEdv65ikhPdX2jXuS245WcxQVQQGTbbRoQenY6nYvwjTpDFkgc\
                                 9CmxURGRzeV1ZAfX47qL6WtidZ6UjJsw6AGkMox8LkzZi
tree depth                   : 1
fingerprint                  : 5bcc53c1
parent f'print               : 5d353a2e
child index                  : 0H (2147483648)
chain code                   : 7903c678c6ffc19959c45ab84faaea0ecf380e1f2e417395cad62d0ed8257774
private key                  : yes
secret exponent              : 99267221948443422929750553059152500607821588225920435785800094833811947682341
 hex                         : db7741ae20d18b3931aab81149119b7e9ee055447cc09cd38a1f8858cdf67a25
wif                          : L4aKjYLZkddjmxBaeoY7PHXDfVuzy7ppqvdqcs1A98FKdXSE4pJz
 uncompressed                : 5KUwYPWMZYQjKLkddCuMvzDHTr9PCMaVWfS7V4dHa7B3QjSUHuK
public pair x                : 24523023807010046501359142424205116674660194532738600088934096164150256999593
public pair y                : 23159854892368232119438885112726915939185318574874735826188721901649019299634
 x as hex                    : 36378a23625821c3fdfa6c9a48a5a9f7bf8526777ce94a61b71c9b69660a1ca9
 y as hex                    : 3334036a2872f59de66d9ef28e5e92166fc2d24573f694a5f0043001a5406732
y parity                     : even
key pair as sec              : 0236378a23625821c3fdfa6c9a48a5a9f7bf8526777ce94a61b71c9b69660a1ca9
 uncompressed                : 0436378a23625821c3fdfa6c9a48a5a9f7bf8526777ce94a61b71c9b69660a1ca9\
                                 3334036a2872f59de66d9ef28e5e92166fc2d24573f694a5f0043001a5406732
hash160                      : 5bcc53c1f3e0b9298d47420e095eea2dd1016ae9
 uncompressed                : 2992ed4532c267f46ebc6963207cf74b6aa2ed97
Bitcoin address              : 19NPGMke7KUhptbKp9QKpTG6ohp3yR4LmS
Bitcoin address uncompressed : 14npiXCWBrEhnezAftk9djjvHCoT8S5zbu
Bitcoin segwit address       : bc1qt0x98s0nuzujnr28gg8qjhh29hgsz6hfleuz89
p2sh segwit                  : 3AowR7H9DyyzDXowohygPcJxebTVmLgRtV
 corresponding p2sh script   : 00145bcc53c1f3e0b9298d47420e095eea2dd1016ae9


#### Output as JSON

ku create -P -j

warning: can't open gpg, can't use as entropy source
{
   "BTC_address": "1Dwc1kmu8DXAjDNFJprYRTZvJaDc8eT9J9",
   "BTC_address_segwit": "bc1q3h6n9cpf9ycp5kdzm9f7dc5see44kez73q9val",
   "BTC_address_uncompressed": "1M6MZXqUbB5e1o84uZh9j6JnLx8XuCEe8e",
   "address": "1Dwc1kmu8DXAjDNFJprYRTZvJaDc8eT9J9",
   "address_segwit": "bc1q3h6n9cpf9ycp5kdzm9f7dc5see44kez73q9val",
   "address_uncompressed": "1M6MZXqUbB5e1o84uZh9j6JnLx8XuCEe8e",
   "chain_code": "2611f1f61bd318ebdd4e27b2a1199ccb24ba03b68b7f89758c4453f547ed3870",
   "child_index": "0",
   "fingerprint": "8df532e0",
   "hash160": "8df532e02929301a59a2d953e6e290ce6b5b645e",
   "hash160_uncompressed": "dc65c24418ec134de377a0cf5711b1839a806c61",
   "input": "create",
   "key_pair_as_sec": "03d142e682c7e3f7533ebfae024b42f42f5c1a11c615f893665a7f5c1401b6811a",
   "key_pair_as_sec_uncompressed": "04d142e682c7e3f7533ebfae024b42f42f5c1a11c615f893665a7f5c1401b6811a3c3c9bdc345ab75c57c699c1351acce2442275b3099c61a61e30d2211d17667d",
   "network": "Bitcoin mainnet",
   "p2sh_segwit": "39sKq8XgEZt8mZrKXtdRTXi8HMo7kmgRip",
   "p2sh_segwit_script": "00148df532e02929301a59a2d953e6e290ce6b5b645e",
   "parent_fingerprint": "00000000",
   "private_key": "no",
   "public_pair_x": "94651588187681802956937359865368626461100120985505173184912761842106241548570",
   "public_pair_x_hex": "d142e682c7e3f7533ebfae024b42f42f5c1a11c615f893665a7f5c1401b6811a",
   "public_pair_y": "27245857446268263341314670522065708120693911791425396878449801946410956318333",
   "public_pair_y_hex": "3c3c9bdc345ab75c57c699c1351acce2442275b3099c61a61e30d2211d17667d",
   "symbol": "BTC",
   "tree_depth": "0",
   "wallet_key": "xpub661MyMwAqRbcEvRBfbPUemiJuu22f7yi1J1bztGFSrEHatMwLaEaHjDa6hsemFj6pLrP7WQ5DzohH75t3L7urpr1a95oRomEBrYApHXnFYT",
   "y_parity": "odd"
}


# TX tool

### Help

tx -h

tx -h
usage: tx [-h] [-t TRANSACTION_VERSION] [-l LOCK_TIME]
          [-n {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}]
          [-a] [-s] [-i address] [-I] [-k KEYCHAIN] [-K KEY_PATHS] [-f path-to-private-keys] [-g GPG_ARGUMENT] [--remove-tx-in tx_in_index_to_delete]
          [--remove-tx-out tx_out_index_to_delete] [--replace-input-script tx_in_script_slash_hex] [-F transaction-fee] [-C] [--db DB] [-u] [-b BITCOIND_URL]
          [-o path-to-output-file] [-d] [--pdb] [--trace] [-p pay-to-script] [--signature known-good-signature] [--sec known-sec] [-P pay-to-script-file]
          [--dump-signatures] [--dump-secs] [--coinbase COINBASE]
          [argument [argument ...]]

Manipulate bitcoin (or alt coin) transactions.

positional arguments:
  argument              generic argument: can be a hex transaction id (exactly 64 characters) to be fetched from cache or a web service; a transaction as a hex string; a
                        path name to a transaction to be loaded; a spendable 4-tuple of the form tx_id/tx_out_idx/script_hex/satoshi_count to be added to TxIn list; an
                        address/satoshi_count to be added to the TxOut list; an address or script to be added to the TxOut list and placed in the "split pool".

optional arguments:
  -h, --help            show this help message and exit
  -t TRANSACTION_VERSION, --transaction-version TRANSACTION_VERSION
                        Transaction version, either 1 (default) or 3 (not yet supported).
  -l LOCK_TIME, --lock-time LOCK_TIME
                        Lock time; either a blockindex, or a date/time (example: "2014-01-01T15:00:00"
  -n {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}, --network {ARG,AXE,BC,BCH,BSD,BTC,BTCD,BTDX,BTG,BTX,CHA,DASH,DCR,DCRT,DFC,DGB,DOGE,FAI,FTC,FTX,GRS,JBS,LTC,MEC,MONA,MZC,PIVX,POLIS,RIC,STRAT,TBTX,TDASH,TMONA,TPIVX,TVI,VIA,XCH,XDT,XLT,XMY,XRT,XTG,XTN,ZEC}
                        Default network code (environment variable PYCOIN_DEFAULT_NETCODE or "BTC"=Bitcoin mainnet if unset
  -a, --augment         augment tx by adding any missing spendable metadata by fetching inputs from cache and/or web services
  -s, --verbose-signature
                        Display technical signature details.
  -i address, --fetch-spendables address
                        Add all unspent spendables for the given bitcoin address. This information is fetched from web services. With no outputs, incoming spendables will
                        be printed.
  -I, --dump-inputs     Dump inputs to this transaction.
  -k KEYCHAIN, --keychain KEYCHAIN
                        path to keychain file for hierarchical key hints (SQLite3 file created with keychain tool)
  -K KEY_PATHS, --key-paths KEY_PATHS
                        Key path hints to search hiearachical private keys (example: 0/0H/0-20)
  -f path-to-private-keys, --private-key-file path-to-private-keys
                        file containing WIF or BIP0032 private keys. If file name ends with .gpg, "gpg -d" will be invoked automatically. File is read one line at a time,
                        and if the file contains only one WIF per line, it will also be scanned for a bitcoin address, and any addresses found will be assumed to be public
                        keys for the given private key.
  -g GPG_ARGUMENT, --gpg-argument GPG_ARGUMENT
                        argument to pass to gpg (besides -d).
  --remove-tx-in tx_in_index_to_delete
                        remove a tx_in
  --remove-tx-out tx_out_index_to_delete
                        remove a tx_out
  --replace-input-script tx_in_script_slash_hex
                        replace an input script: arg looks like "1/796a"
  -F transaction-fee, --fee transaction-fee
                        fee, in satoshis, to pay on transaction, or "standard" to auto-calculate. This is only useful if the "split pool" is used; otherwise, the fee is
                        automatically set to the unclaimed funds.
  -C, --cache           force the resultant transaction into the transaction cache. Mostly for testing.
  --db DB               force the transaction expressed by the given hex into a RAM-based transaction cache. Mostly for testing.
  -u, --show-unspents   show TxOut items for this transaction in Spendable form.
  -b BITCOIND_URL, --bitcoind-url BITCOIND_URL
                        URL to bitcoind instance to validate against (http://user:pass@host:port).
  -o path-to-output-file, --output-file path-to-output-file
                        file to write transaction to. This supresses most other output.
  -d, --disassemble     Disassemble scripts.
  --pdb                 Enter PDB debugger on each script instruction.
  --trace               Trace scripts.
  -p pay-to-script, --pay-to-script pay-to-script
                        a hex version of a script required for a pay-to-scriptinput (a bitcoin address that starts with 3)
  --signature known-good-signature
                        a hex version of a signature that will be used if useful
  --sec known-sec       a hex version of an SEC that will be used if useful
  -P pay-to-script-file, --pay-to-script-file pay-to-script-file
                        a file containing hex scripts (one per line) corresponding to pay-to-script inputs
  --dump-signatures     print signatures (for use with --signature)
  --dump-secs           print secs (for use with --sec)
  --coinbase COINBASE   add an input as a coinbase from the given address

Files are binary by default unless they end with the suffix ".hex". Known networks codes: ARG (Argentum mainnet), AXE (Axe mainnet), BC (Blackcoin mainnet), BCH (Bcash
mainnet), BSD (BitSend mainnet), BTC (Bitcoin mainnet), BTCD (BitcoinDark mainnet), BTDX (Bitcloud mainnet), BTG (Bgold mainnet), BTX (BitCore mainnet), CHA (Chaucha
mainnet), DASH (Dash mainnet), DCR (Decred mainnet), DCRT (Decred testnet), DFC (DEFCOIN mainnet), DGB (Digibyte mainnet), DOGE (Dogecoin mainnet), FAI (Faircoin mainnet),
FTC (Feathercoin mainnet), FTX (Feathercoin testnet), GRS (Groestlcoin mainnet), JBS (Jumbucks mainnet), LTC (Litecoin mainnet), MEC (Megacoin mainnet), MONA (Monacoin
mainnet), MZC (Mazacoin mainnet), PIVX (PIVX mainnet), POLIS (Polis mainnet), RIC (Riecoin mainnet), STRAT (Strat mainnet), TBTX (BitCore testnet3), TDASH (Dash testnet),
TMONA (Monacoin testnet4), TPIVX (PIVX testnet), TVI (Viacoin testnet), VIA (Viacoin mainnet), XCH (Bcash testnet3), XDT (Dogecoin testnet), XLT (Litecoin testnet), XMY
(Myriadcoin mainnet), XRT (Bitcoin regtest), XTG (Bgold testnet), XTN (Bitcoin testnet3), ZEC (Zcash mainnet)

### Tx Notes

You can use tx to perform web searches to get transactions. It will query web services to get transactions. 

You need to set some prior variables to allow, and specify which service providers you are allowing. It will query the web services in this order.

ex.)

export PYCOIN_CACHE_DIR=~/.pycoin_cache
export PYCOIN_SERVICE_PROVIDERS=BLOCKCHAIN_INFO:BLOCKR_ID:BLOCKEXPLORER:BITEASY

tx a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d

"tx" can sign transactions

You can use gpg to encode your wifs


# Networks

It's easy to add networks. 

# Scripts

There is a base script type, which needs to conform to a certain interface. You need a front script method, it complies script to try and match it to this type. If it's not a script multi-sig, it won't match it. 

The way you generate a solution script for multi sig is very different than a regular transaction. 

Pay to address script, which is 99% of Bitcoin transactions.