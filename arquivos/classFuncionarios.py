from classCliente import Cliente

class Funcionario(Cliente):

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,cargo:str,salario:float,usuario:str,senha:str) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
        self._cargo = cargo
        self._salario = salario
        self._usuario = usuario
        self._senha = senha

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

    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self,usuario:str):
        self._usuario = usuario

    @property
    def salario(self):
        return self._salario 
    
    @usuario.setter
    def usuario(self,usuario:str):
        self._usuario = usuario
    




