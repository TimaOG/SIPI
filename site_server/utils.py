import requests


def getStockPrice(stock_name:str):
    """вспомогательная функция для полусения цены акции на следующий день"""
    return requests.get(f'http://localhost:5001/prediction/{stock_name}').json()['Predictions']

def getHistoryPrice(stock_name:str):
    """вспомогательная функция для полусения цены акции на следующий день"""
    return requests.get(f'http://localhost:5001/history/{stock_name}').json()['Predictions']
