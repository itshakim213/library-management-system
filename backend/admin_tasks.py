# admin_tasks.py
from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

# Update user role
user = User.query.filter_by(username='admin').first()
user.role = 'Admin'


librarian = User.query.filter_by(username='librarian').first()
librarian.role = 'Librarian'

member = User.query.filter_by(username='member').first()
member.role = 'Member'
db.session.commit()
