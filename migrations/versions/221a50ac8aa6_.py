"""empty message

Revision ID: 221a50ac8aa6
Revises: 
Create Date: 2022-09-03 15:39:51.469974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '221a50ac8aa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('publicId', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('fullName', sa.String(length=128), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=False),
    sa.Column('isStaff', sa.Boolean(), nullable=False),
    sa.Column('isAdmin', sa.Boolean(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('passwordHash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('publicId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###