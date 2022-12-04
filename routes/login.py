from flask import flash, redirect, url_for, request
from flask_login import login_user, user_logged_out
from werkzeug.security import check_password_hash

from app import login_manager
from models.models import *
from routes.main import *


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = Users.query.filter_by(login=login).first()

        if check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            redirect(next_page)
        else:
            flash ('Ви ввели неправельний логін або пароль')
    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    flash("Ви вийшли з акаунта", category='success')
    user_logged_out()
    return redirect(url_for('main_page'))


@login_manager.users_loader
def load_users(user_id):
    return Users.get(user_id)