"""empty message

Revision ID: 1550c003767a
Revises: 6cb42d5a72bf
Create Date: 2021-06-02 15:49:09.857394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1550c003767a'
down_revision = '6cb42d5a72bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('search', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_search_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('transfer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_transfer_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transfer', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_transfer_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('search', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_search_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
