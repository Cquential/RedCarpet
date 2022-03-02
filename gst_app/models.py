from app import db
from flask_login import UserMixin

class Tax_Payer(UserMixin, db.Model):
    __tablename__ = 'Tax_Payer'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.username}>'