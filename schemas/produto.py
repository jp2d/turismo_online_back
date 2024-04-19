from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto


class ProdutoSchema(BaseModel):
    """ Define quais dados devem ser fornecidos para um novo produto ser inserido.
    """
    nome: str = "Um dia no Rio"
    tipo: str = "Tour"
    valor: float = 123.45
    descricao: str = "Passeio pelos pontos turísticos da cidade do Rio de Janeiro"


class ProdutoBuscaSchema(BaseModel):
    """ Define qual dado deve ser fornecido para que seja buscado um produto na base de dados. A busca será
        feita apenas com base no código do produto que é formado por 10 caracteres sendo 5 letras e 5 números.
    """

    codigo: str = "ABCDE12345"


class ListagemProdutosSchema(BaseModel):
    """ Define como a listagem de produtos será retornada.
    """

    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação de uma listagem de produtos.
    """

    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "codigo": produto.codigo,
            "tipo": produto.tipo,
            "valor": produto.valor,
            "descricao": produto.descricao
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornados.
    """

    id: int = 1
    codigo: str = "ABCDE12345"
    nome: str = "Um dia no Rio"
    tipo: str = "Tour"
    valor: float = 123.45
    descricao: str = "Passeio pelos pontos turísticos da cidade do Rio de Janeiro"


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """

    mesage: str
    nome: str


def apresenta_produto(produto: Produto):
    """ Retorna uma representação de um produto.
    """

    return {
        "id": produto.id,
        "nome": produto.nome,
        "codigo": produto.codigo,
        "tipo": produto.tipo,
        "valor": produto.valor,
        "descricao": produto.descricao
    }