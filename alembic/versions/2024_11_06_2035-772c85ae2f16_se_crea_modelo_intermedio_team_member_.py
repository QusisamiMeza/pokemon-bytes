"""se crea modelo intermedio team member stat

Revision ID: 772c85ae2f16
Revises: 68a213804b5a
Create Date: 2024-11-06 20:35:18.235456

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "772c85ae2f16"
down_revision: Union[str, None] = "68a213804b5a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "team_member_stat",
        sa.Column("team_member_id", sa.Integer(), nullable=False),
        sa.Column("stat_id", sa.Integer(), nullable=False),
        sa.Column("stat_value", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["stat_id"],
            ["stat.id"],
        ),
        sa.ForeignKeyConstraint(
            ["team_member_id"],
            ["team_member.id"],
        ),
        sa.PrimaryKeyConstraint("team_member_id", "stat_id"),
    )


def downgrade() -> None:
    op.drop_table("team_member_stat")
