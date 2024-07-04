from flask_restful import Resource, reqparse
from .models import Book, db

book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
book_parser.add_argument('author', type=str, required=True, help='Author cannot be blank')
book_parser.add_argument('published_date', type=str)
book_parser.add_argument('isbn', type=str, required=True, help='ISBN cannot be blank')
book_parser.add_argument('pages', type=int)
book_parser.add_argument('cover', type=str)
book_parser.add_argument('language', type=str)

class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'isbn': book.isbn,
            'pages': book.pages,
            'cover': book.cover,
            'language': book.language
        }

    def put(self, book_id):
        args = book_parser.parse_args()
        book = Book.query.get_or_404(book_id)
        book.title = args['title']
        book.author = args['author']
        book.published_date = args.get('published_date')
        book.isbn = args['isbn']
        book.pages = args.get('pages')
        book.cover = args.get('cover')
        book.language = args.get('language')
        db.session.commit()
        return {
            'message': 'Book updated successfully'
        }

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {
            'message': 'Book deleted successfully'
        }

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return [
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
        ]

    def post(self):
        args = book_parser.parse_args()
        book = Book(
            title=args['title'],
            author=args['author'],
            published_date=args.get('published_date'),
            isbn=args['isbn'],
            pages=args.get('pages'),
            cover=args.get('cover'),
            language=args.get('language')
        )
        db.session.add(book)
        db.session.commit()
        return {
            'message': 'Book added successfully'
        }, 201
