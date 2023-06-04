from classPessoa import Pessoa

class Cliente(Pessoa):

    #Inicializando a classe 
    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int,num_cartao:int) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
        self._num_cartao = num_cartao

    #Métodos getter e setter para a classe
    @property
    def num_cartao(self) ->int:
        return self._num_cartao
    
    @num_cartao.setter
    def num_cartao(self,num_cartao:int):
        self._num_cartao = num_cartao

#Um método que o cliente solicita o produto ao funcionário
    def solicitar_produto(self):
        pass

