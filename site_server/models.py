from config import db  # , login
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    userpassword = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    telegramid = db.Column(db.Integer)
    isprime = db.Column(db.Boolean)
    theme = db.Column(db.Integer)
    registrationdate = db.Column(db.Date)

    targetStocks = relationship('TargetStocks')

    def __init__(self, name, password, email, telegrammid, isprime, theme, regdate):
        self.username = name
        self.userpassword = password
        self.email = email
        self.telegramid = telegrammid
        self.isprime = isprime
        self.theme = theme
        self.registrationdate = regdate

    def __repr__(self):
        return f'Name: {self.username}\nEmail: {self.email}\nRegistration date: {self.registrationdate}\n\n'

    # @login.user_loader()
    # def load_user(self, user_id):
    #     return Users.query.get(user_id)


class Notifications(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    dealprice = db.Column(db.Integer)
    usetelegram = db.Column(db.Boolean)
    useemail = db.Column(db.Boolean)
    targetStock = db.Column(db.Integer, db.ForeignKey('target_stocks.id'))

    def __init__(self, price, usetelegram, useemail):
        self.dealprice = price
        self.usetelegram = usetelegram
        self.useemail = useemail

    def __repr__(self):
        return f'Price: {self.dealprice}\nUsing telegram: {self.usetelegram}\nUsing email: {self.useemail}\n\n'


class Stocks(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    stocksymbol = db.Column(db.String(255))

    targetStocks = relationship('TargetStocks')

    def __init__(self, symbl):
        self.stocksymbol = symbl

    def __repr__(self):
        return f'Stock: {self.stocksymbol}\n\n'


class TargetStocks(db.Model):
    __tablename__ = 'target_stocks'
    id = db.Column(db.Integer, primary_key=True)
    notification = relationship('Notifications')
    fkuser = db.Column(db.Integer, db.ForeignKey('users.id'))
    fkstock = db.Column(db.Integer, db.ForeignKey('stocks.id'))

    def __init__(self, userId, stockId):
        self.fkuser = userId
        self.fkstock = stockId

    def __repr__(self):
        return f'User: {self.fkuser}\nStock: {self.fkstock}\n\n'
