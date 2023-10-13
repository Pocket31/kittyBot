# from tronpy import Tron

# client = Tron()
# balance = client.get_account_balance(str('TUYEn7biVvaM3arHPJZonZ4ecNyRZfS5pg'))
# print(balance)


import requests

# USDT TRC20 contract address
contract_address = 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'
wallet_address = 'TUYEn7biVvaM3arHPJZonZ4ecNyRZfS5pg'  # wallet address

url = f"https://apilist.tronscan.org/api/account?address={wallet_address}&includeToken=true"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

if 'error' in data:
    print(f"Error: {data['error']}")
else:
    usdt_balance = None
    for token in data['trc20token_balances']:
        if token['tokenName'] == 'Tether USD':
            usdt_balance = round(
                float(token['balance'])*pow(10, -token['tokenDecimal']), 6)
            break

    if usdt_balance is not None:
        print(f'USDT TRC20 balance in {wallet_address}: {usdt_balance}')
    else:
        print(f'USDT TRC20 token not found in {wallet_address}')
