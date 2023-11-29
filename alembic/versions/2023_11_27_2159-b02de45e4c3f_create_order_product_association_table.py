"""Create order product association table

Revision ID: b02de45e4c3f
Revises: 6718ba8af268
Create Date: 2023-11-27 21:59:51.017151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b02de45e4c3f'
down_revision: Union[str, None] = '6718ba8af268'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'order_product_association',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['order_id'],
            ['orders.id'],
        ),
        sa.ForeignKeyConstraint(
            ['product_id'],
            ['products.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('order_id', 'product_id', name='idx_unique_order_product'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_product_association')
    # ### end Alembic commands ###
