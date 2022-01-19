# current app ppints to config in app.py
#from web_app.test.hd_wallet import new_child_wallet
#from web_app.test.wallet_2 import Wallet
from flask import Flask, Blueprint, jsonify, request, render_template, current_app
from bs4 import BeautifulSoup
from mnemonic import Mnemonic
from flask_qrcode import QRcode

from bit import PrivateKeyTestnet
from bit import *

from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.keys import HDKey

#from web_app.models import db, User, Wallet 


#
# Routing
#

simp = Blueprint("simp", __name__)

#
# Home
#

# index home page
# make it super simple
@simp.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form.get('new_wallet') == 'NEW':
            #wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
            wallet = PrivateKeyTestnet()
            wif = wallet.to_wif()
            address = wallet.segwit_address
            btc_balance = wallet.get_balance('btc')
            usd_balance = wallet.balance_as('usd')
            return render_template('index.html', wif=wif, address=address, btc_balance=btc_balance, usd_balance=usd_balance)
        elif  request.form.get('receive_btc') == 'RECEIVE':
            # should show QR code to receive

            #wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
            wallet = PrivateKeyTestnet()
            wif = wallet.to_wif()
            address = wallet.segwit_address
            rec_address = address
            return render_template('index.html', rec_address=rec_address)
        elif  request.form.get('send_btc'):
            send_address = 'send to and amount fields populate'
            amount = 'amount'
            return render_template('index.html', send_address=send_address, amount=amount)
        else:
            message = 'click something'
            return render_template('test.html', message=message)
    elif request.method == 'GET':
        return render_template('index.html')
 
    return render_template('index.html')

@simp.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        if request.form.get('new_wallet') == 'NEW':
            #wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
            wallet = PrivateKeyTestnet()
            wif = wallet.to_wif()
            address = wallet.segwit_address
            btc_balance = wallet.get_balance('btc')
            usd_balance = wallet.balance_as('usd')
            return render_template('test.html', wif=wif, address=address, btc_balance=btc_balance, usd_balance=usd_balance)
        elif  request.form.get('receive_btc') == 'RECEIVE':
            #wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
            wallet = PrivateKeyTestnet()
            wif = wallet.to_wif()
            address = wallet.segwit_address
            rec_address = address
            return render_template('testing/test.html', rec_address=rec_address)
        elif  request.form.get('send_btc'):
            send_address = 'send to and amount fields populate'
            amount = 'amount'
            return render_template('test.html', send_address=send_address, amount=amount)
        else:
            message = 'click something'
            return render_template('test.html', message=message)
    elif request.method == 'GET':
        return render_template('test.html')
    
    return render_template("test.html")
