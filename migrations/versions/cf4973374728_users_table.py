"""users table

Revision ID: cf4973374728
Revises: b9234534886e
Create Date: 2022-03-12 17:47:37.666619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf4973374728'
down_revision = 'b9234534886e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_contact', table_name='user')
    op.drop_column('user', 'contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('contact', sa.VARCHAR(length=120), nullable=True))
    op.create_index('ix_user_contact', 'user', ['contact'], unique=False)
    # ### end Alembic commands ###
