"""create tables

Revision ID: 5164fd5a09c6
Revises: 
Create Date: 2022-11-06 14:37:29.830544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5164fd5a09c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer',
        sa.Column('customer_nr', sa.Integer, primary_key=True),
        sa.Column('customer_name', sa.String(50), nullable=False),
        sa.Column('customer_address', sa.String(50), nullable=False),
        sa.Column('customer_city', sa.String(50), nullable=False),
    )

    op.create_table(
        'customer_order',
        sa.Column('customer_nr', sa.Integer, nullable=False),
        sa.Column('article_nr', sa.Integer, nullable=False),
        sa.Column('order_amount', sa.Numeric(12, 2), nullable=False)
    )

    op.create_table(
        'article',
        sa.Column('article_nr', sa.Integer, primary_key=True),
        sa.Column('article_name', sa.String(50), nullable=False),
        sa.Column('article_price', sa.Numeric(12, 2), nullable=False),
        sa.Column('article_warehouse', sa.Integer, nullable=False),
        sa.Column('article_shelf', sa.Integer, nullable=False),
    )

    op.create_foreign_key("fk_customer_nr", "customer_order", "customer", ["customer_nr"], ["customer_nr"])
    op.create_foreign_key("fk_article_nr", "customer_order", "article", ["article_nr"], ["article_nr"])

def downgrade():
    op.drop_table('customer_order')
    op.drop_table('customer')
    op.drop_table('article')
