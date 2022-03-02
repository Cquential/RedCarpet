from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import (
    login_user,
    User_Mixin,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    return app

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "info"
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

@app.route('/')
def test():
    return "Demo succ"

@app.route('/login')
def login():
    pass

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9080, debug=True)