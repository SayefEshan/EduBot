"""create user quiz histories table

Revision ID: 1361c7efd118
Revises: 47fb6c161c8a
Create Date: 2025-03-29 16:56:13.571288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1361c7efd118'
down_revision: Union[str, None] = '47fb6c161c8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_quiz_histories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE"), nullable=False),
        sa.Column('quiz_id', sa.Integer, sa.ForeignKey('quizes.id', ondelete="CASCADE"), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('mark', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('user_quiz_histories')
