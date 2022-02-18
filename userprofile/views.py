from django.http import HttpResponse
from coinbase.wallet.client import Client
import requests


def index(request):
    ##client = Client(<api_key>, <api_secret>, api_version='YYYY-MM-DD')
    url = "https://api.prime.coinbase.com/v1/portfolios/APIKEYHERE/balances?"

    headers = {
        "Accept": "application/json",
        "X-CB-ACCESS-KEY": "$ACCESS_KEY",
        "X-CB-ACCESS-PASSPHRASE": "$PASSPHRASE",
        "X-CB-ACCESS-SIGNATURE": "$SIGNATURE",
        "X-CB-ACCESS-TIMESTAMP": "$TIMESTAMP"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    return HttpResponse("Hello, world. You're at the crypto pets index.")