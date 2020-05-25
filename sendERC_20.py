import json
from web3 import Web3,HTTPProvider

infura_provider = HTTPProvider('https://mainnet.infura.io/v3/xx')
web3 = Web3(infura_provider)
#web3.eth.enable_unaudited_features()


contract_Address=web3.toChecksumAddress("xx")

abi=json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"stop","outputs":[],"payable":false,"sta$
unicorns = web3.eth.contract(contract_Address, abi=abi)

nonce = web3.eth.getTransactionCount('xx')
unicorn_txn = unicorns.functions.transfer(
'xx',
1,
).buildTransaction({
'chainId': 1,
'gas': 200000,
'gasPrice': web3.toWei('2', 'gwei'),
'nonce': nonce,
})
private_key = 'xx'
signed_txn = web3.eth.account.signTransaction(unicorn_txn, private_key=private_key)

TxHash=web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(TxHash.hex())
