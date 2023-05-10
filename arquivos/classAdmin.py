from classFuncionarios import Funcionario
from crudSistema import removerFuncionario

class Admin(Funcionario):
    
#Ainda vou pensar em mais atributos para a classe

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
        pass

