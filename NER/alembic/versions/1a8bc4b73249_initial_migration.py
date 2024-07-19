"""Initial migration

Revision ID: 1a8bc4b73249
Revises: 
Create Date: 2024-07-19 01:20:31.092053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a8bc4b73249'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entity_text', sa.String(), nullable=True),
    sa.Column('entity_type', sa.String(), nullable=True),
    sa.Column('original_text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entities_id'), 'entities', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entities_id'), table_name='entities')
    op.drop_table('entities')
    # ### end Alembic commands ###