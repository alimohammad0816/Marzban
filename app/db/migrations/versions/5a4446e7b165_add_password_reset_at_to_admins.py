"""add password_reset_at to admins

Revision ID: 5a4446e7b165
Revises: 77c86a261126
Create Date: 2023-10-27 15:54:42.099101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a4446e7b165'
down_revision = '77c86a261126'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('password_reset_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admins', 'password_reset_at')
    # ### end Alembic commands ###