from django.shortcuts import render
import requests
from backendapp.api.apikeys import api_tokens




def home(request):
    url = 'https://stocknewsapi.com/api/v1?'
    ticker = 'tickers=DIS'
    ampersand = "&"
    items ='items=5'
    token = api_tokens(request)
    stock_news_url = url + ticker + ampersand + items+ ampersand +  token
    print (stock_news_url)

    response = requests.get(stock_news_url)
    stocknews = response.json()
    
    for item in stocknews['data']:
          print(item["text"])