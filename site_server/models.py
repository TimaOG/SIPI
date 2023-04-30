from config import db#, login
from flask_login import UserMixin


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

    def __init__(self, name, password, email, telegrammid, isprime, theme, regdate):
        self.username = name
        self.userpassword = password
        self.email = email
        self.telegramid = telegrammid
        self.isprime = isprime
        self.theme = theme
        self.registrationdate = regdate

    def __repr__(self):
        return f'Name: {self.username}\n Email: {self.email}\n Registration date: {self.registrationdate}\n\n'

    # @login.user_loader()
    # def load_user(self, user_id):
    #     return Users.query.get(user_id)
