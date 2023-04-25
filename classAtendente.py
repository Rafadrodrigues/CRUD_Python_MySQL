from classPessoa import Pessoa

class Atendente(Pessoa):

    def __init__(self,nome,endereco,email,cpf,telefone,login,senha) -> None:
        super().__init__(self,nome,endereco,email,cpf,telefone)
        self.login = login
        self.senha = senha

    def receberCliente():
        print("Olá, seja Bem-Vindo! \n" + 23 * "-")
        
