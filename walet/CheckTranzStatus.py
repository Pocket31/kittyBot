import requests

trz = '8369c7958056ff7ac1e0aeee3ecb0757a81353331fb8f3dd26a5d8333168a910'
transactions = []
status = False
while status == False:

    response = requests.get(f"https://nile.trongrid.io/v1/accounts/{'TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS'}/transactions/{'trc20'}?&contract_address={'TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf&only_confirmed=true'}"
                            )
    lol = response.json()

    for transaction in lol['data']:
        transactions.append(transaction['transaction_id'])

    if trz in transactions:
        print('транзакция успешна')
        status = True
    else:
        print('транзация еще не прошла')
