import pandas as pd
from datetime import timedelta, date
import requests
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

donePredictions = {}
class AI_Stocks:
    """класс получения цены акций"""
    @staticmethod
    def getPredictionAbout(stock_name: str, days_for=2):
        """получение предсказания"""
        global donePredictions
        if stock_name in donePredictions and donePredictions[stock_name][1] == datetime.now().strftime('%Y-%m-%d'):
            return donePredictions[stock_name][0]
        AAPL = AI_Stocks.getStockData(stock_name)
        X = AAPL.filter(['Close']).values
        print('test')
        print(donePredictions)
        scaler = MinMaxScaler()
        X = scaler.fit_transform(X)
        y = AAPL.filter(['Close']).shift(-1).values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        model = LinearRegression()
        model.fit(X_train, y_train)
        prediction = model.predict(scaler.transform(AAPL.tail(1).filter(['Close']).values))
        current_date = datetime.now().strftime('%Y-%m-%d')
        donePredictions[stock_name] = [prediction, current_date]
        return prediction

    @staticmethod
    def getStockData(stock_name: str):
        """получение цены акций за большой период"""
        today = date.today().strftime('%Y-%m-%d')
        time_ago = str(date.today() - timedelta(days=5 * 365))
        ticket = stock_name
        res = {'Date': [], 'Close': []}
        while time_ago < today:
            url = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticket}/history.json?from={time_ago}&till={today}"
            response = requests.get(url)

            for i in response.json()['history']['data']:
                res['Close'].append(i[11])
                res['Date'].append(i[1])

            to_date = str(time_ago).split('-')
            time_ago = str(date(int(to_date[0]), int(to_date[1]), int(to_date[2])) + timedelta(days=100))

        url = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticket}/history.json?from={time_ago}&till={today}"
        response = requests.get(url)
        for i in response.json()['history']['data']:
            res['Close'].append(i[11])
            res['Date'].append(i[1])
        df = pd.DataFrame(res)
        df.drop_duplicates()
        df = df.dropna()
        df = df[(df['Close'] != None)]
        return df.set_index('Date')



