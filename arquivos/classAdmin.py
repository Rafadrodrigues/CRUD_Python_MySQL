from classColaboradores import Colaboradores

class Admin(Colaboradores):

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,login:str,senha:str) -> None:
        super().__init__(nome,endereco,email,cpf,telefone,login,senha)
