class Material:

    def __init__(self,nome,quantidade,preco,especificacao,margemLucro,datafabricacao,fornecedor) -> None:
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco
        self._espeficacao = especificacao
        self._margemLucro = margemLucro
        self._datafabricacao = datafabricacao
        self._fornecedor = fornecedor