"""refresh db

Revision ID: cdc1197685fc
Revises: 203bc8b8a008
Create Date: 2022-11-19 14:46:17.546194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdc1197685fc'
down_revision = '203bc8b8a008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_table', sa.Column('cars', sa.ARRAY(sa.Integer()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_table', 'cars')
    # ### end Alembic commands ###