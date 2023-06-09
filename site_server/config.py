from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
upl_folder = 'static/images'
app.config['SECRET_KEY'] = '1SuperSecretKey1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/SIPI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
news_url = 'https://ria.ru/tag_thematic_category_Akcii/'
stoсks_url = 'https://www.tinkoff.ru/invest/stocks/?start=0&end=60&country=All&orderType=Asc&sortType=ByName&countryOfRisk=RU'
"""конфиги"""
