from flask import Flask, make_response, jsonify
from ai import AI_Stocks

app = Flask(__name__)
app.secret_key = '1SuperSecretKey1'


@app.route("/prediction/<stock_name>")
def openMain(stock_name: str):
    gg = AI_Stocks.getPredictionAbout(stock_name)
    print(gg)
    res = jsonify({'Predictions' : gg[0][0]})
    return res

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)


