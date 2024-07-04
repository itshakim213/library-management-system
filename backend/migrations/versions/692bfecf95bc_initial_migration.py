"""Initial migration.

Revision ID: 692bfecf95bc
Revises: 
Create Date: 2024-07-01 22:47:53.733446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '692bfecf95bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('author', sa.String(length=128), nullable=False),
    sa.Column('published_date', sa.String(length=10), nullable=True),
    sa.Column('isbn', sa.String(length=13), nullable=False),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('cover', sa.String(length=256), nullable=True),
    sa.Column('language', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###