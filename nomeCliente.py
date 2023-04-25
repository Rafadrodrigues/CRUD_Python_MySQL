import classPessoa

class Cliente(classPessoa):

    def __init__(self,nome,endereco,email,cpf,telefone) -> None:
        super().__init__(self,nome,endereco,email,cpf,telefone)
        self.vendas = []
