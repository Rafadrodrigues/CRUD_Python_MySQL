from classColaboradores import Colaboradores

class Admin(Colaboradores):

    def __init__(self,nome,endereco,email,cpf,telefone,login,senha) -> None:
        super().__init__(nome,endereco,email,cpf,telefone,login,senha)
        pass