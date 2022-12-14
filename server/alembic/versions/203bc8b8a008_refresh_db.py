"""refresh db

Revision ID: 203bc8b8a008
Revises: 4d308f53d962
Create Date: 2022-11-19 14:46:12.491672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '203bc8b8a008'
down_revision = '4d308f53d962'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_table', 'cars')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_table', sa.Column('cars', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
