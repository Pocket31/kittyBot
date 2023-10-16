from tronpy import Tron

# client = Tron(network="nile")
# balance = client.get_account_balance(str('TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS'))
# print(balance)


def check_balance_usdt_trc_20(wallet_address):
    import requests

    # USDT TRC20 contract address
    contract_address = 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'
    wallet_address = wallet_address  # wallet address

    url = f"https://apilist.tronscan.org/api/account?address={wallet_address}&includeToken=true"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    data = response.json()

    if 'error' in data:
        return f"Error: {data['error']}"
    else:
        usdt_balance = None
        for token in data['trc20token_balances']:
            if token['tokenName'] == 'Tether USD':
                usdt_balance = round(
                    float(token['balance'])*pow(10, -token['tokenDecimal']), 6)
                break

        if usdt_balance is None:
            usdt_balance = 0.00
        return usdt_balance


print(check_balance_usdt_trc_20('TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS'))
