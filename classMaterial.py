#Classe responsável por atribuir definir materiais no sistema
class Material:

    def __init__(self,nome,quantidade,preco,especificacao,datafabricacao,fornecedor) -> None:
        self._nome = nome
        self._quantidade = quantidade
        self._preco = preco
        self._especificacao = especificacao
        self._datafabricacao = datafabricacao
        self._fornecedor = fornecedor

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property   
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self,quantidade):
        self._quantidade = quantidade

    @property   
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self,preco):
        self._preco = preco
    
    @property   
    def especificacao(self):
        return self._especificacao
    @especificacao.setter
    def especificacao(self,especificacao):
        self._especificacao = especificacao

    @property   
    def datafabricacao(self):
        return self._datafabricacao
    @datafabricacao.setter
    def datafabricacao(self,datafabricacao):
        self._datafabricacao = datafabricacao

    @property   
    def fornecedor(self):
        return self._fornecedor
    @fornecedor.setter
    def fornecedor(self,fornecedor):
        self._fornecedor = fornecedor

