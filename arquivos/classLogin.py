#Classe que realiza login para utilizar 
class Login:

    #Construtor da classe login
    def __init__(self, username:str,password:str):
        self._usuario = username
        self._senha = password

    @property
    def password(self) -> str:
        return self._passwordo 
    
    @password.setter
    def password(self,password:str):
        self._password = password
    
    @property
    def username(self) -> str:
        return self._username 
    
    @username.setter
    def username(self,username:str):
        self._username= username

    #Efetua o login do funcionario ou adm. Para isso é preciso que faça uma verificação no banco de dados
    def logar(self,objeto) -> bool:
        if self._username == objeto._username and self._password == objeto._password:
            print("Login realizado")
            return True
        else:
            #Caso o usuário insira alguma informação incorreta
            print("Credenciais incorretas")
            return False
