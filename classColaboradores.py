
from classPessoa import Pessoa

class Colaboradores(Pessoa):

    def __init__(self,nome,endereco,email,cpf,telefone,login,senha) -> None:
        super().__init__(self,nome,endereco,email,cpf,telefone,login,senha)
        self._login = login
        self._senha = senha

#Métodos getter e setter dos Colaboradores
    @property
    def _nome(self):
        return self._nome
    @_nome.setter
    def _nome(self,nome):
        self._nome = nome
    
    @property   
    def _endereco(self):
        return self._endereco
    @_endereco.setter
    def _endereco(self,endereco):
        self._endereco = endereco

    @property   
    def _cpf(self):
        return self._cpf
    @_cpf.setter
    def _cpf(self,cpf):
        self._cpf = cpf
    
    @property   
    def _telefone(self):
        return self._telefone
    @_telefone.setter
    def _telefone(self,telefone):
        self._telefone = telefone

    @property   
    def _login(self):
        return self._login
    @_login.setter
    def _login(self,login):
        self._login = login

    @property   
    def _senha(self):
        return self._senha
    @_senha.setter
    def _senha(self,senha):
        self._senha = senha


