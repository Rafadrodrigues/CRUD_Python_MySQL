from classPessoa import Cliente

class Colaboradores(Cliente):

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)



