from flask import Flask, Blueprint, jsonify, request, render_template, current_app
from mnemonic import Mnemonic
from flask_qrcode import QRcode

from bit import PrivateKeyTestnet
from bit import *

#
# User Wallet
#

wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
btc_balance = wallet.get_balance('btc')
usd_balance = wallet.balance_as('usd')
address = wallet.segwit_address
wif = wallet.to_wif()

#
# Routing
#

simp = Blueprint("simp", __name__)

# index home page
# make it super simple
@simp.route("/", methods=['POST', 'GET'])
def index():

    print('privkey: ', wallet)
    print('wif: ', wif)
    print('address: ', address)
    print('btc balance: ', btc_balance)

    return render_template('index.html', wif=wif, address=address, btc_balance=btc_balance, usd_balance=usd_balance)

# take you to the prompt to send a transaction
@simp.route("/send", methods=['GET', 'POST'])
def send():

    if request.method == 'POST':
        if request.form.get('send_tx') == 'SEND':
            # get user inputs
            send_to = request.form.get('send_to_address')
            amount = float(request.form.get('amount'))

            # create and broadcast transaction to the Bitcoin test network
            tx_ID = wallet.send([(send_to, amount, 'btc')])
            return render_template('tx.html', tx_ID=tx_ID)

    return render_template('send.html', btc_balance=btc_balance, usd_balance=usd_balance)

@simp.route("/receive", methods=['GET', 'POST'])
def receive():
    return render_template('receive.html', btc_balance=btc_balance, usd_balance=usd_balance, address=address)
