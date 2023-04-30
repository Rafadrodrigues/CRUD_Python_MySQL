from classPessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self,nome,endereco,email,cpf,telefone) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
    
    #Métodos para inserir/alterar o dados do Cliente
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property   
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco

    @property   
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf
    
    @property   
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self,telefone):
        self._telefone = telefone

    #Imprimir informações
    def infoCliente(self):
        print(f"Seus dados:Nome:{self._nome}\nEndereço:{self._endereco}\nE-mail:{self._email}\n\
        CPF:{self._cpf}\nTelefone:{self._telefone}")
        
novo_cliente = Cliente("Rafael","Quatro Vintens","rafarodrigues919@gmail.com",12805960661,33998016559)

novo_cliente.infoCliente()