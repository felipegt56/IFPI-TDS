from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produtos]
    minhas_vendas: List[Produtos]
    meus_pedidos: List[Produtos]

class Produto(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem Observações!'