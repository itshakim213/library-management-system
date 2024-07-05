
# Library Management System

## Description
The Library Management System (LMS) is a comprehensive backend system developed using Flask. It includes user authentication, book management, and transaction processing functionalities. This project was primarily focused on learning and implementing backend development.

## Features
- User Registration and Login
- Role-based Access Control (Admin, Librarian, Member & Guest)
- Book Management (Add, View, Update, Delete)
- Transaction Management (Request, Approve, Return books)

## Technologies Used
- **Backend:** Flask, Flask-RESTful, Flask-Cors, Flask-Login, Flask-Migrate, Flask-SQLAlchemy
- **Database:** SQLite (or any other SQL database supported by SQLAlchemy)
- **API Documentation:** Postman or terminal (`curl`) or any similar tools.

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- Node.js and npm
- Git
- Virtual Environment (`venv`)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/itshakim213/library-management-system.git
   cd library-management-system/backend
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```sh
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application:**
   ```sh
   python run.py
   ```

### API Endpoints

#### Authentication
- **POST /api/register**: Register a new user
- **POST /api/login**: Login an existing user
- **POST /api/logout**: Logout the current user

#### User Management
- **GET /api/users**: Get all users (Admin only)
- **PUT /api/users/<user_id>**: Update a user (Admin only)
- **DELETE /api/users/<user_id>**: Delete a user (Admin only)

#### Book Management
- **GET /api/books**: Get all books
- **POST /api/books**: Add a new book (Librarian only)
- **PUT /api/books/<book_id>**: Update a book (Librarian only)
- **DELETE /api/books/<book_id>**: Delete a book (Librarian only)

#### Transaction Management
- **POST /api/transactions**: Request a transaction (Member only)
- **POST /api/transactions/<transaction_id>/approve**: Approve a transaction (Librarian only)
- **POST /api/transactions/<transaction_id>/return**: Return a book (Member only)
- **GET /api/transactions**: Get all transactions (Librarian only)

