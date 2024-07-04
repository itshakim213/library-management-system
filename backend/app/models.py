from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import here to avoid circular import
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    published_date = db.Column(db.String(10), nullable=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    pages = db.Column(db.Integer, nullable=True)
    cover = db.Column(db.String(256), nullable=True)
    language = db.Column(db.String(32), nullable=True)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False, default='Guest')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='requested')

    user = db.relationship('User', back_populates='transactions')
    book = db.relationship('Book', back_populates='transactions')

User.transactions = db.relationship('Transaction', order_by=Transaction.id, back_populates='user')
Book.transactions = db.relationship('Transaction', order_by=Transaction.id, back_populates='book')
