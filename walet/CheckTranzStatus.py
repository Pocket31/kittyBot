import requests
import asyncio

trz = '090e93b1696fc7dfc774306fc0fc7d7f41f8ac9e9c9844e03cb6bcc4afba876c'


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


# print(check_tranzaktion(trz))
