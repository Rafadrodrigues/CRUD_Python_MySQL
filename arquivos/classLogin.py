#Classe que realiza login para utilizar 
from classSistema import Sistema
class Login:

    #Construtor da classe login
    def __init__(self, usuario:str, senha:str):
        self._usuario = usuario
        self._senha = senha

    @property
    def senha(self) -> str:
        return self._senha
    
    @senha.setter
    def senha(self,senha:str):
        self._senha = senha
    
    @property
    def usuario(self) -> str:
        return self._usuario 
    
    @usuario.setter
    def usuario(self,usuario:str):
        self._usuario = usuario

    #Efetua o login do funcionario ou adm. Para isso é preciso que faça uma verificação no banco de dados
    # def logar(self,usuario) -> bool:
    #     #A verificacao é solicita ao sistema, que vê no banco de dados, e depois repassa aqui
    #     funcionario = Sistema.efetuarLogin()
    #     while True:
    #         if usuario.usuario == self._usuario and usuario.senha == self._senha:
    #             Sistema.efetuarLogin()
    #             print("Login realizado")
    #             return True
    #         else:
    #             #Caso o usuário insira alguma informação incorreta
    #             print("Credenciais incorretas,tente novamente.")
    #             return False
           
                    
