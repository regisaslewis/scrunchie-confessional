"""add product_owners association table

Revision ID: 161218bc8ca3
Revises: f1f599fb16f1
Create Date: 2023-11-28 16:37:42.914761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '161218bc8ca3'
down_revision = 'f1f599fb16f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_owners',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_products_owners_product_id_products')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_products_owners_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products_owners')
    # ### end Alembic commands ###
