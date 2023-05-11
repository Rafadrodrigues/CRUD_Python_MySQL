from classFuncionarios import Funcionario

class Admin(Funcionario):
    
#Ainda vou pensar em mais atributos para a classe

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,usuario:str,senha:str) -> None:
        super().__init__(nome,endereco,email,cpf,telefone,usuario,senha)
    

