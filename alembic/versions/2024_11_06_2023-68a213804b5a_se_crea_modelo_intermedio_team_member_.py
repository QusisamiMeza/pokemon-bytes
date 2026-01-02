"""se crea modelo intermedio team member move

Revision ID: 68a213804b5a
Revises: 5eb912237fd7
Create Date: 2024-11-06 20:23:21.351177

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68a213804b5a"
down_revision: Union[str, None] = "5eb912237fd7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "team_member_move",
        sa.Column("team_member_id", sa.Integer(), nullable=False),
        sa.Column("move_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["move_id"],
            ["move.id"],
        ),
        sa.ForeignKeyConstraint(
            ["team_member_id"],
            ["team_member.id"],
        ),
        sa.PrimaryKeyConstraint("team_member_id", "move_id"),
    )


def downgrade() -> None:
    op.drop_table("team_member_move")
