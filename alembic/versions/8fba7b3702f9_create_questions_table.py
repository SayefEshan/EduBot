"""create questions table

Revision ID: 8fba7b3702f9
Revises: b25bb263cc66
Create Date: 2025-03-29 16:20:24.727844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fba7b3702f9'
down_revision: Union[str, None] = 'b25bb263cc66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('quiz_id', sa.Integer, sa.ForeignKey('quizes.id', ondelete="CASCADE"), nullable=False),
        sa.Column('question_text', sa.String(200), nullable=False),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('questions')
