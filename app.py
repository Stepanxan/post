from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:19982804@localhost:3306/post_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


login_manager = LoginManager(app)
login_manager.init_app(app)

with app.app_context():
     db.create_all()


if __name__ == "__main__":
    app.run(debug=True)