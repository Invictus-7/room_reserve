"""Add user relationship to Reservation

Revision ID: 9df69cc9395f
Revises: b13686629614
Create Date: 2023-01-03 10:32:39.907518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df69cc9395f'
down_revision = 'b13686629614'
branch_labels = None
depends_on = None


# Шаг_46 - вписываем в batch_op.create_foreign_key вместо None
# следующее значение - fk — обозначение внешнего ключа - Foreign Key;
#     reservation — таблица, для которой создается внешний ключ;
#     user_id — столбец, который содержит внешний ключ;
#     user — таблица, на которую ссылается внешний ключ.
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
