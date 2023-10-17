import requests

url = "https://api.shasta.trongrid.io/wallet/triggersmartcontract"

payload = {
    "owner_address": "TEEWS5zXLmgNjEazXcgrQq41cPzd2KabRS",
    "contract_address": "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf",
    "function_selector": "transfer(address,uint256)",
    "parameter": "00000000000000000000004115208EF33A926919ED270E2FA61367B2DA3753DA0000000000000000000000000000000000000000000000000000000000000032",
    "fee_limit": 1000000000,
    "call_value": 0,
    "visible": True
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
