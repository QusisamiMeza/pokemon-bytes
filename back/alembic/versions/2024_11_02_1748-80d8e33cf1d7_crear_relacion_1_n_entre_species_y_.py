"""Crear relacion 1:N entre species y pokemon

Revision ID: 80d8e33cf1d7
Revises: 1f610b98b4a6
Create Date: 2024-11-02 17:48:34.716653

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "80d8e33cf1d7"
down_revision: Union[str, None] = "1f610b98b4a6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon") as batch_op:
        batch_op.create_foreign_key(
            "fk_pokemon_species", "species", ["species_id"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon") as batch_op:
        batch_op.drop_constraint("fk_pokemon_species", type_="foreignkey")
