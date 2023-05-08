from classCliente import Cliente

class Funcionario(Cliente):

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,cargo:str,salario:float) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
        self._cargo = cargo
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self,cargo:str):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario 
    
    @salario.setter
    def salario(self,salario:float):
        self._salario = salario
    




