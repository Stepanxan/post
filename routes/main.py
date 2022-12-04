from app import app
from flask import render_template
from flask_login import login_required

from models.models import Posts


@app.route('/', methods=["GET"])
def main_page():
    post = Posts.query.all()
    return render_template('index.html', post=post)


@app.route('/about')
@login_required
def about():
    return render_template("about.html")

