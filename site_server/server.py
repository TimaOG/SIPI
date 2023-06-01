import datetime
import requests
import codecs
from bs4 import BeautifulSoup
from config import app, db, news_url, stoсks_url
from models import Users, Notifications, Stocks, TargetStocks
from flask_login import login_user, login_required, current_user, logout_user
from flask import redirect, render_template, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
from utils import getStockPrice

"""сервер основной"""


def news_parser():
    page = requests.get(news_url)
    print('News status code: ' + str(page.status_code))
    filteredNews = []
    soap = BeautifulSoup(page.text, "html.parser")
    allNews = soap.find_all('div', class_='list-item')
    for new in allNews:
        filteredNews.append({'title': new.find('a', class_='list-item__title color-font-hover-only').text,
                             'href': new.find('a', class_='list-item__title color-font-hover-only')['href'],
                             'date': new.find('div', class_='list-item__date').text
                             })
    return filteredNews


def stocks_parser():
    page = requests.get(stoсks_url)
    print('Stocks status code: ' + str(page.status_code))
    filteredStocks = []
    soap = BeautifulSoup(page.content.decode('utf-8'), "html.parser")
    allStocks = soap.find_all('tr', class_='Table-module__row_Qlwsh Table-module__row_clickable_FeO1O')
    for stock in allStocks:
        filteredStocks.append(
            {'name': stock.find('div', class_='SecurityRow__showName_inlal SecurityRow__overflowEllipsis_zFECb').text,
             'code': stock.find('div', class_='SecurityRow__ticker_KMm7A').text,
             'price': stock.find('span', class_='Money-module__money_p_VHJ').text.replace('\xa0', ' '),
             'percent': stock.find('div', class_='PriceCellWithYearChange__relative_Ijlmu').text
             })
    return filteredStocks


@app.route('/')
@app.route('/index')
def index():
    """открытие главной страницы"""
    news = news_parser()
    if current_user.is_authenticated:
        stocks = []
        user = Users.query.filter_by(id=current_user.id).first()
        targets = TargetStocks.query.filter_by(fkuser=user.id).all()
        for target in targets:
            stocks.append(Stocks.query.filter_by(id=target.fkstock).first())
        return render_template('index.html', news=news[0:6], stocks=stocks)
    return render_template('index.html', news=news[0:6])


@app.route('/settings', methods=['POST', 'GET'])
@login_required
def change_settings():
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        email = request.form.get('email')
        telegramId = request.form.get('telegramId')
        isMailing = request.form.get('isMailing')
        if name:
            user = Users.query.filter_by(id=current_user.id).first()
            user.username = name
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        elif passwd:
            user = Users.query.filter_by(id=current_user.id).first()
            passHash = generate_password_hash(passwd)
            user.userpassword = passHash
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        elif email:
            user = Users.query.filter_by(id=current_user.id).first()
            user.email = email
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        elif telegramId:
            user = Users.query.filter_by(id=current_user.id).first()
            user.telegramid = telegramId
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        elif isMailing:
            user = Users.query.filter_by(id=current_user.id).first()
            user.isMailing = True if isMailing == 'on' else False
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """функция логина"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            user = Users.query.filter_by(email=email).first()
            if user and check_password_hash(user.userpassword, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """функция логаут"""
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """функционал регистрации"""
    fio = request.form.get('username')
    email = request.form.get('email')
    pass1 = request.form.get('password1')
    pass2 = request.form.get('password2')
    if request.method == 'POST' and fio and email and pass1 and pass2:
        if pass1 != pass2:
            return redirect(url_for('register'))
        else:
            passHash = generate_password_hash(pass1)
            new_user = Users(name=fio, password=passHash, email=email, telegrammid=666, isMailing=True, theme=1,
                             regdate=datetime.date.today(), balance=0)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/profile')
def profile():
    """функция профиля"""
    return render_template('profile.html')


@app.route('/stoks')
# @login_required
def stocks():
    """функция получения акций"""
    stocks = stocks_parser()
    for item in stocks:
        if Stocks.query.filter_by(code=item['code']).scalar():
            stock = Stocks.query.filter_by(code=item['code']).first()
            stock.price = item['price']
            stock.percent = item['percent']
            db.session.add(stock)
        else:
            new_stock = Stocks(name=item['name'], code=item['code'], price=item['price'], percent=item['percent'], prediction='0')
            db.session.add(new_stock)
        db.session.commit()
    db_stocks = Stocks.query.all()
    return render_template('stoks.html', stocks=db_stocks)


@app.route('/analiz')
# @login_required
def analiz():
    """анализ акций"""
    return render_template('analiz.html')


@app.route('/totarget/<code>', methods=['GET', 'POST'])
@login_required
def saveToTarget(code):
    """сохранение акции в избранное"""
    if request.method == 'POST':
        user = Users.query.filter_by(id=current_user.id).first()
        stock = Stocks.query.filter_by(code=code).first()
        new_target = TargetStocks(userId=user.id, stockId=stock.id)
        db.session.add(new_target)
        db.session.commit()
        return redirect(url_for('stocks'))
    return render_template('stoks.html')


if __name__ == "__main__":
    app.run(debug=True)
