"""renaming grade column to year

Revision ID: f3903ed2129a
Revises: 791279dd0760
Create Date: 2023-12-12 14:00:48.448542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f3903ed2129a"
down_revision = "791279dd0760"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "grade", new_column_name="year")


def downgrade() -> None:
    op.alter_column("students", "year", new_column_name="grade")
