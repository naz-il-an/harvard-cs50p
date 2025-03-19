import requests
import sys

if len(sys.argv)<2:
    sys.exit('Missing command-line argument')
elif sys.argv[1].isalpha():
    sys.exit('Command-line argument is not a number')

try:
    price = requests.get('https://api.coincap.io/v2/assets/bitcoin')
    price = price.json()
    price = float(price['data']['priceUsd'])
    amount = price * float(sys.argv[1])

    
except requests.RequestException:
    pass


print(f"${amount:,.4f}")
