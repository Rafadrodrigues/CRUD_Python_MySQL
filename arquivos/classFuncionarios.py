from classCliente import Cliente

class Funcionario(Cliente):

    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,cargo:str,salario:float,usuario:str,senha:str) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
        self._cargo = cargo
        self._salario = salario
        self._usuario = usuario
        self._senha = senha

    @property
    def cargo(self) -> str:
        return self._cargo
    
    @property
    def salario(self) -> float:
        return self._salario 

    @property
    def usuario(self) -> str:
        return self._usuario
    
    @usuario.setter
    def usuario(self,usuario:str):
        self._usuario = usuario

    def realizar_venda(self):
        pass

    def relatorio_de_venda(self):
        pass

