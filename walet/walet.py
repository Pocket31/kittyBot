from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider


client = Tron(network='nile')

cntr = client.get_contract("TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf")
priv_key = PrivateKey(bytes.fromhex(
    "db0d9add0d98120e2270a2fbb93166a6673f01cde1ccfa703132171e0461dfe2"))

txn = (
    client.trx.transfer("TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS",
                        "TChGkQpWkfKvADqfMKfJBf2cLsgiMDBFhk", 1_000)
    .memo("test")
    .build().inspect()
    .sign(priv_key).broadcast()
)
print(txn)
# print(txn.txid)
# print(txn.wait())


# print(dir(cntr.functions))


# print('Symbol:', cntr.functions.symbol())  # The symbol string of the contract
# # # Symbol: RMB

# precision = cntr.functions.decimals()
# print('Balance:', cntr.functions.balanceOf(
#     'TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS') / 10 ** precision)
# # # Balance: 100000.0


# full_node = HTTPProvider("https://api.trongrid.io")
# solidity_node = HTTPProvider("https://api.trongrid.io")
# event_server = HTTPProvider("https://api.trongrid.io")
# client = Tron(network='nile')


# private_key = PrivateKey(bytes.fromhex(
#     "db0d9add0d98120e2270a2fbb93166a6673f01cde1ccfa703132171e0461dfe2"))
# address = private_key.public_key.to_base58check_address()


# USDT contract address on Tron mainnet
# token_address = "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf"
# recipient_address = "TChGkQpWkfKvADqfMKfJBf2cLsgiMDBFhk"
# amount = 1000  # Amount of USDT to send (in decimal format)
# # Convert to USDT's decimal precision (6 decimals)
# amount_in_wei = int(amount * 10 ** 6)

# token_contract = client.get_contract(token_address)
# transaction = token_contract.functions.transfer(recipient_address, amount_in_wei).build_transaction(
#     owner_address=address
# )

# signed_txn = client.trx.sign(transaction, private_key)
# response = client.trx.broadcast(signed_txn)
# print(response)

# priv_key = PrivateKey(bytes.fromhex(
#     "db0d9add0d98120e2270a2fbb93166a6673f01cde1ccfa703132171e0461dfe2"))

# txn = (cntr.functions.transfer('TChGkQpWkfKvADqfMKfJBf2cLsgiMDBFhk', 1_000)
#        # address of the private key
#        .with_owner('TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS')
#        .fee_limit(5_000_000).build().sign(priv_key=priv_key))
# txn.broadcast()  # or txn.broadcast()
# # {'result': True, 'txid': '63609d84524b754a97c111eec152700f273979bb00dad993d8dcce5848b4dd9a'}

# result = txn.broadcast().wait()
# print(result)
# {'id': '63609d84524b754a97c111eec152700f273979bb00dad993d8dcce5848b4dd9a',
#  'blockNumber': 6609475, 'blockTimeStamp': 1592539509000,
#  'contractResult': ['0000000000000000000000000000000000000000000000000000000000000001'],
#  'contract_address': 'THi2qJf6XmvTJSpZHc17HgQsmJop6kb3ia',
#  'receipt': {'energy_usage': 13062, 'energy_usage_total': 13062, 'net_usage': 344, 'result': 'SUCCESS'},
#  'log': [{'address': 'THi2qJf6XmvTJSpZHc17HgQsmJop6kb3ia',
#           'topics': ['ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef',
#                      '00000000000000000000000046a23e25df9a0f6c18729dda9ad1af3b6a131160',
#                      '000000000000000000000000d8dd39e2dea27a40001884901735e3940829bb44'],
#           'data': '00000000000000000000000000000000000000000000000000000000000003e8'}]}

# trigger output can be parsed manually
# cntr.functions.transfer.parse_output(result['contractResult'][0])
# True
# or use `.result()` to parse it automatically
# txn.broadcast().result()
# True
