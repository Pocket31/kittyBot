import requests
import asyncio
from tronpy import Tron, Contract
from tronpy.keys import PrivateKey

client = Tron(network='nile')
contract = client.get_contract('TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf')
precision = contract.functions.decimals()


def create_wallet_usdt_trc_20():
    '''Создание кошелька'''
    wallet = client.generate_address()
    wallet_info = {'address': wallet['base58check_address'],
                   'key': wallet['private_key']}
    return wallet_info


def check_balance_usdt_trc_20(wallet_address):
    '''Проверка баланса кошелька'''
    return contract.functions.balanceOf(f'{wallet_address}') / 10 ** precision


def send_transaction(private_key, wallet_address_from, wallett_address_to, amount):
    '''Отправка транзакции'''
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


async def check_tranzaktion(tranzaction_id):
    '''Проверка статуса транзакции'''
    transactions = []
    status = False
    while status == False:
        response = requests.get(f"https://nile.trongrid.io/v1/accounts/{'TChGkQpWkfKvADqfMKfJBf2cLsgiMDBFhk'}/transactions/{'trc20'}?&contract_address={'TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf&only_confirmed=true'}"
                                )
        lol = response.json()
        await asyncio.sleep(30)
        for transaction in lol['data']:
            transactions.append(transaction['transaction_id'])

        if tranzaction_id in transactions:
            return True
        else:
            continue
