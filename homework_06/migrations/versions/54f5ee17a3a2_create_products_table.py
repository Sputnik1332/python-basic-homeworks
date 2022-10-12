"""Create products table

Revision ID: 54f5ee17a3a2
Revises: 
Create Date: 2022-10-05 20:33:18.305930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "54f5ee17a3a2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("product")
    # ### end Alembic commands ###