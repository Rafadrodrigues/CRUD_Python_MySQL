from classPessoa import Pessoa

class Colaboradores(Pessoa):

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,login:str,senha:str) -> None:
        super().__init__(nome,endereco,email,cpf,telefone,login,senha)
        self._login = login
        self._senha = senha

#Métodos getter e setter dos Colaboradores
    @property   
    def login(self):
        return self._login
    @login.setter
    def login(self,login):
        self._login = login
        
    @property   
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha = senha


