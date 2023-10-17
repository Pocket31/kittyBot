from tronpy import Tron
from tronpy.keys import PrivateKey
import time

client = Tron(network='nile')
contract = client.get_contract('TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf')


def send_transaction(private_key, wallet_address_from, wallett_address_to, amount):
    priv_key = PrivateKey(bytes.fromhex(f'{private_key}'))
    txn = (
        contract.functions.transfer(
            f'{wallett_address_to}', amount)  # 2000000 = 20
        # address of the private key
        .with_owner(f'{wallet_address_from}')
        .fee_limit(5_000_000)
        .build()
        .sign(priv_key)
    )
    transaction_info = txn.broadcast().wait()
    return transaction_info['id']


private_key = 'db0d9add0d98120e2270a2fbb93166a6673f01cde1ccfa703132171e0461dfe2'
wallet_address_from = 'TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS'
wallett_address_to = 'TChGkQpWkfKvADqfMKfJBf2cLsgiMDBFhk'
amount = 2000000


print(send_transaction(private_key=private_key, wallet_address_from=wallet_address_from,
                       wallett_address_to=wallett_address_to, amount=amount))
