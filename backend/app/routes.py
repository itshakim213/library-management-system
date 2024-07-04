from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from .resources import BookResource, BookListResource
from .models import db, User, Book, Transaction
from flask_login import login_user, logout_user, login_required, current_user
from functools import wraps
from datetime import date

# app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<int:book_id>')

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 400

    login_user(user)
    return jsonify({'message': 'Login successful'}), 200

@api_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role != role:
                return jsonify({'message': 'Access denied'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@api_bp.route('/admin', methods=['GET'])
@login_required
@role_required('Admin')
def admin_dashboard():
    return jsonify({'message': 'Welcome, Admin!'}), 200

@api_bp.route('/librarian', methods=['GET'])
@login_required
@role_required('Librarian')
def librarian_dashboard():
    return jsonify({'message': 'Welcome, Librarian!'}), 200

@api_bp.route('/books', methods=['POST'])
@login_required
@role_required('Librarian')
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data.get('title'),
        author=data.get('author'),
        published_date=data.get('published_date'),
        isbn=data.get('isbn'),
        pages=data.get('pages'),
        cover=data.get('cover'),
        language=data.get('language')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@api_bp.route('/users', methods=['GET'])
@login_required
@role_required('Admin')
def view_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        } for user in users
    ]), 200

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
@login_required
@role_required('Admin')
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
@login_required
@role_required('Admin')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

@api_bp.route('/transactions', methods=['POST'])
@login_required
@role_required('Member')
def request_transaction():
    data = request.get_json()
    book_id = data.get('book_id')
    book = Book.query.get_or_404(book_id)
    transaction = Transaction(
        user_id=current_user.id,
        book_id=book.id,
        issue_date=date.today(),
        status='requested'
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction requested successfully'}), 201

@api_bp.route('/transactions/<int:transaction_id>/approve', methods=['POST'])
@login_required
@role_required('Librarian')
def approve_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    if transaction.status != 'requested':
        return jsonify({'message': 'Invalid transaction status'}), 400
    transaction.status = 'issued'
    transaction.issue_date = date.today()
    db.session.commit()
    return jsonify({'message': 'Transaction approved successfully'}), 200

@api_bp.route('/transactions/<int:transaction_id>/return', methods=['POST'])
@login_required
@role_required('Member')
def return_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    if transaction.status != 'issued':
        return jsonify({'message': 'Invalid transaction status'}), 400
    transaction.status = 'returned'
    transaction.return_date = date.today()
    db.session.commit()
    return jsonify({'message': 'Book returned successfully'}), 200

@api_bp.route('/transactions', methods=['GET'])
@login_required
@role_required('Librarian')
def view_transactions():
    transactions = Transaction.query.all()
    return jsonify([
        {
            'id': transaction.id,
            'user_id': transaction.user_id,
            'book_id': transaction.book_id,
            'issue_date': transaction.issue_date,
            'return_date': transaction.return_date,
            'status': transaction.status
        } for transaction in transactions
    ]), 200

@api_bp.route('/books', methods=['GET'])
def view_books():
    books = Book.query.all()
    return jsonify([
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'isbn': book.isbn,
            'pages': book.pages,
            'cover': book.cover,
            'language': book.language
        } for book in books
    ]), 200
