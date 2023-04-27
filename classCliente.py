from classPessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self,nome,endereco,email,cpf,telefone) -> None:
        super().__init__(nome,endereco,email,cpf,telefone)
    
    #Métodos para inserir/alterar o dados do Cliente
    property
    def _nome(self):
        return self._nome
    @_nome.setter
    def _nome(self,nome):
        self._nome = nome
    
    @property   
    def _endereco(self):
        return self._endereco
    @_endereco.setter
    def _endereco(self,endereco):
        self._endereco = endereco

    @property   
    def _cpf(self):
        return self._cpf
    @_cpf.setter
    def _cpf(self,cpf):
        self._cpf = cpf
    
    @property   
    def _telefone(self):
        return self._telefone
    @_telefone.setter
    def _telefone(self,telefone):
        self._telefone = telefone

    #Imprimir informações
    def InfoCliente(self,):
        print(f"Nome:{self.nome}\nEndereço:{self.endereco}\nE-mail:{self.email}\nCPF:{self.cpf}\nTelefone:{self.telefone}")