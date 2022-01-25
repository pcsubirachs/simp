# current app ppints to config in app.py
#from web_app.test.hd_wallet import new_child_wallet
#from web_app.test.wallet_2 import Wallet
from flask import Flask, Blueprint, jsonify, request, render_template, current_app
from bs4 import BeautifulSoup
from mnemonic import Mnemonic
from flask_qrcode import QRcode

from bit import PrivateKeyTestnet
from bit import *

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
    # using bit library only...
    wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
    #wallet = PrivateKeyTestnet('mznsbBjB47tpnWtEmc1kGyHAEfqMkoQmHJ')
    print('privkey: ', wallet)
    wif = wallet.to_wif()
    print('wif: ', wif)
    address = wallet.segwit_address
    print('address: ', address)
    btc_balance = wallet.get_balance('btc')
    print('btc balance: ', btc_balance)
    usd_balance = wallet.balance_as('usd')


    return render_template('index.html', wif=wif, address=address, btc_balance=btc_balance, usd_balance=usd_balance)

@simp.route("/send", methods=['GET', 'POST'])
def send():
    # define this globally at some point
    wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
    btc_balance = wallet.get_balance('btc')
    usd_balance = wallet.balance_as('usd')

    # get user inputs
    request.form.get('send_to_address') == 'send_to_address'
    request.form.get('amount') == 'amount'
    
    # when user submits form, form action POSTS, action received here, wallet sends input amount
    if request.method == 'POST':
        wallet.send([('send_to_address', int('amount'), 'btc')])
    
    return render_template('send.html', btc_balance=btc_balance, usd_balance=usd_balance)

@simp.route("/receive", methods=['GET', 'POST'])
def receive():
    # define this globally at some point
    wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
    btc_balance = wallet.get_balance('btc')
    usd_balance = wallet.balance_as('usd')
    address = wallet.segwit_address

    
    return render_template('receive.html', btc_balance=btc_balance, usd_balance=usd_balance, address=address)


#@simp.route("/test", methods=['GET', 'POST'])
#def test():
#    if request.method == 'POST':
#        if request.form.get('new_wallet') == 'NEW':
#            #wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
#            wallet = PrivateKeyTestnet()
#            wif = wallet.to_wif()
#            address = wallet.segwit_address
#            btc_balance = wallet.get_balance('btc')
#            usd_balance = wallet.balance_as('usd')
#            return render_template('test.html', wif=wif, address=address, btc_balance=btc_balance, usd_balance=usd_balance)
#        elif  request.form.get('receive_btc') == 'RECEIVE':
#            #wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
#            wallet = PrivateKeyTestnet()
#            wif = wallet.to_wif()
#            address = wallet.segwit_address
#            rec_address = address
#            return render_template('testing/test.html', rec_address=rec_address)
#        elif  request.form.get('send_btc'):
#            send_address = 'send to and amount fields populate'
#            amount = 'amount'
#            return render_template('test.html', send_address=send_address, amount=amount)
#        else:
#            message = 'click something'
#            return render_template('test.html', message=message)
#    elif request.method == 'GET':
#        return render_template('test.html')
#    
#    return render_template("test.html")

#def index():
#    if request.method == 'POST':
#        if request.form.get('new_wallet') == 'NEW':
#            # using bit library only...
#
#            wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
#            #wallet = PrivateKeyTestnet('mznsbBjB47tpnWtEmc1kGyHAEfqMkoQmHJ')
#            print('privkey: ', wallet)
#            wif = wallet.to_wif()
#            print('wif: ', wif)
#            address = wallet.segwit_address
#            print('address: ', address)
#            btc_balance = wallet.get_balance('btc')
#            print('btc balance: ', btc_balance)
#            usd_balance = wallet.balance_as('usd')
#            return render_template('index.html', wif=wif, address=address, btc_balance=btc_balance, usd_balance=usd_balance)
#        elif  request.form.get('receive_btc') == 'RECEIVE':
#            # should show QR code to receive, static for now
#            wallet = PrivateKeyTestnet('cSs7bQAxg2cfHaCQbUVkrmbNouCupuabpu9ZWXaXoAT8ak8K3BrE')
#            #wallet = PrivateKeyTestnet('mznsbBjB47tpnWtEmc1kGyHAEfqMkoQmHJ')
#            wif = wallet.to_wif()
#            address = wallet.segwit_address
#            rec_address = address
#            return render_template('index.html', rec_address=rec_address)
#        elif  request.form.get('send_btc'):
#            send_address = 'send to and amount fields populate'
#            amount = 'amount'
#            return render_template('index.html', send_address=send_address, amount=amount)
#        else:
#            message = 'click something'
#            return render_template('test.html', message=message)
#    elif request.method == 'GET':
#        return render_template('index.html')
# 
#    return render_template('index.html')