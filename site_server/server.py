import datetime

from config import app, db
from models import Users, Notifications, Stocks, TargetStocks
from flask_login import login_user, login_required, current_user, logout_user
from flask import redirect, render_template, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from utils import getStockPrice


@app.route('/')
@app.route('/index')
def index():
    print(getStockPrice('SBER'))
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
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
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    fio = request.form.get('username')
    email = request.form.get('email')
    pass1 = request.form.get('password1')
    pass2 = request.form.get('password2')
    if request.method == 'POST' and fio and email and pass1 and pass2:
        if pass1 != pass2:
            return redirect(url_for('register'))
        else:
            passHash = generate_password_hash(pass1)
            new_user = Users(name=fio, password=passHash, email=email, telegrammid=666, isprime=True, theme=1,
                             regdate=datetime.date.today(), balance=0)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('stocks'))
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/stocks')
@login_required
def stocks():
    return render_template('stocks.html')


if __name__ == "__main__":
    app.run(debug=True)
