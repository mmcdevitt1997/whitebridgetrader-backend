from django.shortcuts import render
import requests

def home(request):
    response = requests.get('api url')
    stocknews = response.json()
    
    for item in stocknews['data']:
          item["news_url"]