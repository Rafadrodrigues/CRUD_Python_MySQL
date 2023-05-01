#Classe pessoa é uma classe que vai servir de herança para outras classes.
class Pessoa:

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int) -> None:
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._cpf = cpf
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property   
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco

    @property   
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf
    
    @property   
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self,telefone):
        self._telefone = telefone
