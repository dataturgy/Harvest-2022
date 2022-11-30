"""Change order_amount to integer

Revision ID: 1a1190b410d9
Revises: 5164fd5a09c6
Create Date: 2022-11-06 15:21:38.375724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a1190b410d9'
down_revision = '5164fd5a09c6'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('customer_order', 'order_amount', type_=sa.types.Integer)


def downgrade():
    op.alter_column('customer_order', 'order_amount', type_=sa.types.Numeric(12,2))
