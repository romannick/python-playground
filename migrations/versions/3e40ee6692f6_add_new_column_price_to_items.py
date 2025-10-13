"""Add new column price to Items

Revision ID: 3e40ee6692f6
Revises:
Create Date: 2025-10-13 15:08:57.465347
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e40ee6692f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Use batch_alter_table for safe schema changes
    with op.batch_alter_table('items', schema=None) as batch_op:
        # Adjust existing 'name' column length if needed
        batch_op.alter_column(
            'name',
            existing_type=sa.VARCHAR(length=120),
            type_=sa.String(length=100),
            existing_nullable=False
        )

        # Add new column 'price'
        batch_op.add_column(
            sa.Column('price', sa.Float, nullable=False, server_default='0.0')
        )


def downgrade():
    with op.batch_alter_table('items', schema=None) as batch_op:
        # Remove the 'price' column
        batch_op.drop_column('price')

        # Revert 'name' column type
        batch_op.alter_column(
            'name',
            existing_type=sa.String(length=100),
            type_=sa.VARCHAR(length=120),
            existing_nullable=False
        )
