"""empty message

Revision ID: 3efdf2bc8997
Revises: 
Create Date: 2018-03-19 21:31:07.014174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3efdf2bc8997'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('photo_name', sa.String(length=80), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###