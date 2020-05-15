from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import re, requests 
from binance_chain.http import HttpApiClient
from binance_chain.messages import TransferMsg
from binance_chain.wallet import Wallet
from binance_chain.environment import BinanceEnvironment
import random

texts= ['You are awesome today', 'You are amazing today', 'You are beautiful', 'Binance bot likes you', 'Keep it up']
randomtext = (random.choice(texts))

emojis=["🎉", "🤩", "🤗", "🤙", "🎊"]
randomemoji = (random.choice(emojis))


prod_env = BinanceEnvironment.get_production_env()
walletpriv = Wallet('xxxx', prod_env)
client = HttpApiClient(env=prod_env)
#-1001243236277 angelxx
#-445138418
app = Flask(__name__)

admintg=783083878
app.config['secret_key']="xxxx"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///xxxx.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):

	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.String(10),nullable=False)
	username=db.Column(db.String(10),nullable=False)
	wallet=db.Column(db.String(50),nullable=False)

	def __repr__(self):
		return "%s %s %s" %(self.userid,self.username,self.wallet)


@app.route('/hello')
def helloIndex():
	return 'Hello World from Python Flask!'

@app.route('/botmessages', methods=['POST'])
def botmessages():
	rhediye="^\/(hediye|tip) \d+\.?\d* bnb$"
	radres="^\/myaddress [a-z0-9]{42}$"
	data=request.json
	print (data)
	

	if (("message" in data)  and ("text" in data["message"]) and ("from" in data["message"])): #and ("username" in data["message"]["from"])):

		if (re.match(rhediye,data["message"]["text"]) and ("reply_to_message" in data['message']) ):
			userid=data['message']['from']['id']
			replyuserid=data['message']['reply_to_message']['from']['id']
			#replyusername=data['message']['reply_to_message']['from']['username']

			if ("username" in data['message']['reply_to_message']['from']):
				replyusername="@"+ data['message']['reply_to_message']['from']['username'] 
			else: 
				replyusername=data['message']['reply_to_message']['from']['first_name']

			id=User.query.filter_by(userid=replyuserid).first()
			print (id)
			print (replyuserid)
			print("tip geldiz")
			if (userid==admintg and id is not None):
				replywallet=id.wallet
				username=data['message']['from']['username']
				tip=re.findall("^\/(?:tip|hediye) (.*) bnb$",data["message"]["text"])[0]
				print("start transs")
				try:
					transfer_msg = TransferMsg(
					wallet=walletpriv,
					symbol='BNB',
					amount=(float(tip)),
					to_address=str(replywallet)
					)
					res = client.broadcast_msg(transfer_msg, sync=True)
					print (res)
					print (res[0]['hash'])
					tburl = "https://api.telegram.org/xxxxs/sendMessage?chat_id=11111&text="  + randomtext +" "+str(replyusername) + " Congratulations! You got " + str(tip) + " BNB " + randomemoji +" %0A%0A"+"https://explorer.binance.org/tx/"+res[0]['hash']



					requests.get(tburl)
					print("%s %s %s %s %s %s %s" % (userid,username,data["message"]["text"],tip,replyuserid,replyusername,replywallet))
				except:
					print ("hata")
					pass
			else:
				print("cacik cikti")
		#adress ekleme		
		if(re.match(radres,data["message"]["text"])):

			if ("username" in data['message']['from']):
				username="@"+ data['message']['from']['username'] 
			else: 
				username="Null"
			print("detect adres")
			userid=data['message']['from']['id']
			#username=data['message']['from']['username']
			wallet=re.findall("^\/myaddress (.*)$",data["message"]["text"])[0]
	
			id=User.query.filter_by(userid=userid).first()
			#print (id)
			if(id is None):
				print ("id yok")
				q=User(userid = userid, username = username, wallet = wallet)
				db.session.add(q)
				db.session.commit()
			else:
				print ("id var")
				id.wallet=wallet
				id.username=data["message"]["text"]["username"] # ekledim
				db.session.commit()
			print("%s %s %s %s" % (userid, username, data["message"]["text"], wallet))
	
		else:
			pass

	else:
		pass

	return jsonify(data)
	
		


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=False)




