"""create quizes table

Revision ID: b25bb263cc66
Revises: 0bca48ade8fb
Create Date: 2025-03-29 14:54:21.393066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b25bb263cc66'
down_revision: Union[str, None] = '2bc1796f76bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'quizes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ai_token', sa.String(50), nullable=False),
        sa.Column('quiz_category_id', sa.Integer, sa.ForeignKey('quiz_categories.id'), nullable=False),
        sa.Column('title', sa.String(200), nullable=True),
        sa.Column('title_limit', sa.DateTime, nullable=True),
        sa.Column('question_count', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )



def downgrade() -> None:
    op.drop_table('quizes')
