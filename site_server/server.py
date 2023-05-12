from config import app, db
from models import Users, Notifications, Stocks, TargetStocks
from flask_login import login_user, login_required, current_user
from flask import redirect, render_template, url_for, request, flash


@app.route('/')
@app.route('/index')
def index():
    # user = Users.query.first()
    # targetStock = user.targetStocks
    # stock = Stocks.query.filter_by(id=1).first()
    # stock = Stocks.query.filter_by(id=targetStock.fkstock)
    # print(stock)
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/stocks')
def stock():
    return render_template('stocks.html')


if __name__ == "__main__":
    app.run(debug=True)
