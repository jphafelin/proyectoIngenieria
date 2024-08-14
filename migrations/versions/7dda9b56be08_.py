"""empty message

Revision ID: 7dda9b56be08
Revises: 
Create Date: 2024-08-12 19:09:29.458816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dda9b56be08'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('username')
    )
    op.create_table('empleador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cif', sa.Integer(), nullable=False),
    sa.Column('metodo_pago', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=300), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cif')
    )
    op.create_table('programador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('precio_hora', sa.Integer(), nullable=False),
    sa.Column('tecnologias', sa.String(length=200), nullable=False),
    sa.Column('experiencia', sa.Enum('JUNIOR', 'MID', 'SENIOR', name='experience'), nullable=False),
    sa.Column('descripcion', sa.String(length=300), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ofertas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=700), nullable=False),
    sa.Column('salario', sa.Integer(), nullable=False),
    sa.Column('plazo', sa.String(length=100), nullable=False),
    sa.Column('modalidad', sa.String(length=80), nullable=False),
    sa.Column('experiencia_minima', sa.String(length=100), nullable=True),
    sa.Column('fecha_publicacion', sa.Date(), nullable=False),
    sa.Column('empleador_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['empleador_id'], ['empleador.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('proyectos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('descripcion_corta', sa.String(length=150), nullable=False),
    sa.Column('git', sa.String(length=300), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('tecnologias', sa.String(length=200), nullable=False),
    sa.Column('programador_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['programador_id'], ['programador.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_id', sa.Integer(), nullable=False),
    sa.Column('to_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['from_id'], ['empleador.id'], ),
    sa.ForeignKeyConstraint(['to_id'], ['programador.id'], ),
    sa.PrimaryKeyConstraint('id', 'from_id', 'to_id')
    )
    op.create_table('favoritos',
    sa.Column('programador_id', sa.Integer(), nullable=False),
    sa.Column('empleador_id', sa.Integer(), nullable=False),
    sa.Column('oferta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['empleador_id'], ['empleador.id'], ),
    sa.ForeignKeyConstraint(['oferta_id'], ['ofertas.id'], ),
    sa.ForeignKeyConstraint(['programador_id'], ['programador.id'], ),
    sa.PrimaryKeyConstraint('programador_id', 'empleador_id', 'oferta_id')
    )
    op.create_table('postulados',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('oferta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['oferta_id'], ['ofertas.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'oferta_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('postulados')
    op.drop_table('favoritos')
    op.drop_table('ratings')
    op.drop_table('proyectos')
    op.drop_table('ofertas')
    op.drop_table('programador')
    op.drop_table('empleador')
    op.drop_table('user')
    # ### end Alembic commands ###
