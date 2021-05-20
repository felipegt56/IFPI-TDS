from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship, relationships
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    produtos = relationship('Produtos', back_populates='usuario')
    pedidos = relationship('Pedidos', back_populates='usuario')

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    detalhes = Column(String)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    id_usuario = Column(Integer, ForeignKey('usuario.id', name='fk_usuario' ))

    usuario = relationship('Usuarios', back_populates='produtos')

class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    local_entrega = Column(String)
    opcao = Column(String)
    observacoes = Column(String)
    id_produto = Column(Integer, ForeignKey('produto.id', name='fk_pedido_produto' ))
    id_usuario = Column(Integer, ForeignKey('usuario.id', name='fk_pedido_usuario' ))

    usuario = relationship('Usuarios', back_populates='pedidos')
    produto = relationship('Produtos')