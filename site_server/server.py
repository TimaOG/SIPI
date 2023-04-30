from config import app, db, manager
from flask_login import login_user, login_required, current_user
from flask import redirect, render_template, url_for, request, flash
from models import Users


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
