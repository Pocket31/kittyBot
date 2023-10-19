from tronpy import Tron, Contract
from tronpy.keys import PrivateKey


def create_wallet_usdt_trc_20():
    '''Создание кошелька'''

    client = Tron(network="nile")
    wallet = client.generate_address()
    wallet_info = {'address': wallet['base58check_address'],
                   'key': wallet['private_key']}

    # wallet_info = {'address': 'TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS',
    #                'key': 'db0d9add0d98120e2270a2fbb93166a6673f01cde1ccfa703132171e0461dfe2'}
    return wallet_info


# print(create_wallet_usdt_trc_20())
