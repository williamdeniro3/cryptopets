from django.http import HttpResponse
from coinbase.wallet.client import Client
import requests


def index(request):
    ##client = Client(<api_key>, <api_secret>, api_version='YYYY-MM-DD')
    url = "https://api.coinstats.app/public/v1/coins?skip=0&limit=5&currency=EUR"


    response = requests.request("GET", url, headers={})
    jsonResponse = response.json()

    dict = {}
  
    for coin in range(len(jsonResponse['coins'])):
       coin_name = jsonResponse['coins'][coin]['id']
       coin_price = jsonResponse['coins'][coin]['price']
       coin_1d_change = jsonResponse['coins'][coin]['priceChange1d']
       dict[coin_name] = {
            'coin_price' : coin_price,
            'priceChange1d' : coin_1d_change
        }

    array = []
    for key in dict:
       if(dict[key]['priceChange1d'] < 1):
           array.append(key + "= :(")
       else:
           array.append(key + "= :)")

    return HttpResponse('\n'.join(map(str, array)))