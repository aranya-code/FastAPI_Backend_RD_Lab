"""Create phone number for user column

Revision ID: 47124d6ca9a1
Revises: 
Create Date: 2026-03-21 17:02:02.178975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47124d6ca9a1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable= True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
