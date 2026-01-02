"""se crea el modelo type

Revision ID: 728e631c4dd9
Revises: 83299c7778ca
Create Date: 2024-11-02 17:29:16.444925

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "728e631c4dd9"
down_revision: Union[str, None] = "83299c7778ca"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("identifier", sa.Text(), nullable=False),
        sa.Column("generation_id", sa.Integer(), nullable=False),
        sa.Column("damage_class_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("type")
