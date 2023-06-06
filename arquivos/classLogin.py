#Classe que realiza login para utilizar 
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

           
                    
