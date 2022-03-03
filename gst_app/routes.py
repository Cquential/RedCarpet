from crypt import methods
from email.policy import strict
from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
    session
)

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from app import create_app,db,login_manager,bcrypt
from models import Tax_Payer
from forms import login_form,register_form


# if app
app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return Tax_Payer.query.get(int(user_id))


@app.route('/', methods=('GET','POST'), strict_slashes=False)
def test():
    return render_template('index.html', title="Home")

@app.route('/login')
def login():
    return "<html> <body> You log in <p> GG </p> <marquee>fuck</marquee> </body> </html>"