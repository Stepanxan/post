from flask import flash, redirect, url_for, request
from werkzeug.security import generate_password_hash


from models.models import *
from routes.main import *


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    first_name = request.form.get('first_name')
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (first_name or email or login or password or password2):
            flash('Будь ласка заповніть всі поля')
        elif password != password2:
            flash('Паролі не співпадають', category='error')
            return redirect(url_for('registration'))
        else:
            has_password = generate_password_hash(password)
            user = Users(
                first_name=first_name,
                email=email,
                login=login,
                password=has_password
            )

            try:
                db.session.add(user)
                db.session.commit()
                flash("Реєстрація пройшла успішно", category='success')
                return redirect(url_for('login'))
            except:
                flash("Користувач з таким email вже існує", category='error')
                return redirect(url_for('registration'))

    else:
        return redirect(url_for('registration.html'))