"""Add unit_price to OrderProductAssociasion table

Revision ID: d490e6ac3cbd
Revises: d36dc94da650
Create Date: 2023-11-28 19:45:34.611474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd490e6ac3cbd'
down_revision: Union[str, None] = 'd36dc94da650'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'order_product_association',
        sa.Column('unit_price', sa.Integer(), server_default='0', nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_product_association', 'unit_price')
    # ### end Alembic commands ###
