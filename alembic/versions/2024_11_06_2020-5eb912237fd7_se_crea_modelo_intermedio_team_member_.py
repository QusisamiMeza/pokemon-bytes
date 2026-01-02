"""se crea modelo intermedio team member types

Revision ID: 5eb912237fd7
Revises: c6066923bd2f
Create Date: 2024-11-06 20:20:03.313269

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5eb912237fd7"
down_revision: Union[str, None] = "c6066923bd2f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "team_member_type",
        sa.Column("team_member_id", sa.Integer(), nullable=False),
        sa.Column("type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["team_member_id"],
            ["team_member.id"],
        ),
        sa.ForeignKeyConstraint(
            ["type_id"],
            ["type.id"],
        ),
        sa.PrimaryKeyConstraint("team_member_id", "type_id"),
    )


def downgrade() -> None:
    op.drop_table("team_member_type")
