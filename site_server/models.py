from config import db, login
from flask_login import UserMixin
from sqlalchemy.orm import relationship



class Users(db.Model, UserMixin):
    """класс для работы с пользователями"""
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    userpassword = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    telegramid = db.Column(db.Integer)
    isMailing = db.Column(db.Boolean)
    theme = db.Column(db.Integer)
    registrationdate = db.Column(db.Date)
    balance = db.Column(db.Integer)

    targetStocks = relationship('TargetStocks')

    def __init__(self, name, password, email, telegrammid, isMailing, theme, regdate, balance):
        self.username = name
        self.userpassword = password
        self.email = email
        self.telegramid = telegrammid
        self.isMailing = isMailing
        self.theme = theme
        self.registrationdate = regdate
        self.balance = balance

    def __repr__(self):
        return f'Name: {self.username}\nEmail: {self.email}\nRegistration date: {self.registrationdate}\n\n'


@login.user_loader
def load_user(user_id):
    """подгррузка пользователя"""
    user = Users.query.get(user_id)
    return user


class Notifications(db.Model):
    """класс работы с уведомлениями"""
    __table_args__ = {'extend_existing': True}
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
    """класс работы с акциями"""
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    stocksymbol = db.Column(db.String(255))

    targetStocks = relationship('TargetStocks')

    def __init__(self, symbl):
        self.stocksymbol = symbl

    def __repr__(self):
        return f'Stock: {self.stocksymbol}\n\n'


class TargetStocks(db.Model):
    """отслеживаемые акции"""
    __table_args__ = {'extend_existing': True}
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
