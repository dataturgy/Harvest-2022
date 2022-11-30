"""load data

Revision ID: f02eb79abbed
Revises: 1a1190b410d9
Create Date: 2022-11-06 14:57:45.867937

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import os 


# revision identifiers, used by Alembic.
revision = 'f02eb79abbed'
down_revision = '1a1190b410d9'
branch_labels = None
depends_on = None


def upgrade():
    file_dir = os.path.dirname(__file__)
    data_dir = f'{file_dir}{os.path.sep}..{os.path.sep}..{os.path.sep}..{os.path.sep}data{os.path.sep}'
    
    # get metadata from current connection
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect()

    articles = pd.read_csv(f'{data_dir}article.csv').to_dict('records')
    op.bulk_insert(sa.Table('article', meta), articles)

    customers = pd.read_csv(f'{data_dir}customer.csv').to_dict('records') 
    op.bulk_insert(sa.Table('customer', meta), customers)

    customer_orders = pd.read_csv(f'{data_dir}customer_order.csv').to_dict('records') 
    op.bulk_insert(sa.Table('customer_order', meta), customer_orders)


def downgrade():
    op.execute('TRUNCATE TABLE customer_order')
    op.execute('TRUNCATE TABLE article CASCADE')
    op.execute('TRUNCATE TABLE customer CASCADE')

