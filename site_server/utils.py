import requests


def getStockPrice(stock_name:str):
    return requests.get(f'http://localhost:5001/prediction/{stock_name}').json()['Predictions']
