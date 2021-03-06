"""empty message

Revision ID: c806d9f66a61
Revises: 
Create Date: 2021-03-23 21:09:07.201030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c806d9f66a61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('rooms', sa.String(length=3), nullable=True),
    sa.Column('baths', sa.String(length=3), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('property_type', sa.String(length=11), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('photo'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
