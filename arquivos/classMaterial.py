#Classe responsável por atribuir definir materiais no sistema
class Material:

    def __init__(self,nome:str,quantidade:int,preco:float,especificacao:str,datafabricacao:str,fornecedor:str) -> None:
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco
        self._especificacao = especificacao
        self._datafabricacao = datafabricacao
        self._fornecedor = fornecedor

    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self,nome:str):
        self._nome = nome
    
    @property   
    def quantidade(self) -> int:
        return self._quantidade
    @quantidade.setter
    def quantidade(self,quantidade:int):
        self._quantidade = quantidade

    @property   
    def preco(self) -> float:
        return self._preco
    @preco.setter
    def preco(self,preco:float):
        self._preco = preco
    
    @property   
    def especificacao(self) -> str:
        return self._especificacao
    @especificacao.setter
    def especificacao(self,especificacao:str):
        self._especificacao = especificacao

    @property   
    def datafabricacao(self) -> str:
        return self._datafabricacao
    @datafabricacao.setter
    def datafabricacao(self,datafabricacao:str):
        self._datafabricacao = datafabricacao

    @property   
    def fornecedor(self) -> str:
        return self._fornecedor
    @fornecedor.setter
    def fornecedor(self,fornecedor:str):
        self._fornecedor = fornecedor

