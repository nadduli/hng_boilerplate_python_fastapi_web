"""Ensure id and foreign keys are of type String

Revision ID: ff92a0037698
Revises: 299ab5d402fc
Create Date: 2024-08-08 19:03:17.115224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff92a0037698'
down_revision: Union[str, None] = '299ab5d402fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_comments', sa.Column('user_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'product_comments', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product_comments', type_='foreignkey')
    op.drop_column('product_comments', 'user_id')
    # ### end Alembic commands ###
