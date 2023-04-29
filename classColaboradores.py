from classPessoa import Pessoa

class Colaboradores(Pessoa):

    def __init__(self,nome,endereco,email,cpf,telefone,login,senha) -> None:
        super().__init__(nome,endereco,email,cpf,telefone,login,senha)
        self._login = login
        self._senha = senha

#Métodos getter e setter dos Colaboradores
    @property   
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha = senha


