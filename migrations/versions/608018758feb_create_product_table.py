"""create product table

Revision ID: 608018758feb
Revises: 
Create Date: 2020-03-19 11:00:30.370628

"""
import uuid

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.dialects import postgresql

revision = '608018758feb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    products = op.create_table(
        'products',
        sa.Column('uuid', postgresql.UUID(), primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('price', sa.Float)
    )

    op.bulk_insert(products, [{
        'uuid': str(uuid.uuid4()),
        'name': 'salad',
        'price': 1.30
    }])


def downgrade():
    op.drop_table('products')
