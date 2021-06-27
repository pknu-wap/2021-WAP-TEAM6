"""empty message

Revision ID: f1aa3003659c
Revises: 1550c003767a
Create Date: 2021-06-02 15:50:41.387424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1aa3003659c'
down_revision = '1550c003767a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_search')
    with op.batch_alter_table('search', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_search_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('transfer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
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

    op.create_table('_alembic_tmp_search',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subject', sa.VARCHAR(length=200), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_search_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pk_search')
    )
    # ### end Alembic commands ###