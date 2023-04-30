from classColaboradores import Colaboradores

class Admin(Colaboradores):

    def __init__(self,nome,endereco,email,cpf,telefone,login,senha) -> None:
        super().__init__(nome,endereco,email,cpf,telefone,login,senha)
    
#Essa comandos dentro da funcao eu não tenho certeza se está certo .
    def informacoesAdmin(self):
        super()._nome
        super()._endereco
        super()._email
        super()._cpf
        super()._telefone
        super()._login
        super()._senha