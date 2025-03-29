"""create question options table

Revision ID: 47fb6c161c8a
Revises: 8fba7b3702f9
Create Date: 2025-03-29 16:34:09.829307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47fb6c161c8a'
down_revision: Union[str, None] = '8fba7b3702f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'question_options',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question_id', sa.Integer, sa.ForeignKey('questions.id', ondelete="CASCADE"), nullable=False),
        sa.Column('option_text', sa.String(200), nullable=False),
        sa.Column('is_correct_answer', sa.Boolean, nullable=False),
        sa.Column('is_selected_option', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('question_options')
