#Classe que representa o objeto Vendas
class Venda:

    def __init__(self,id:int,nome:str,quantidade:int,valor:float) -> None:
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
