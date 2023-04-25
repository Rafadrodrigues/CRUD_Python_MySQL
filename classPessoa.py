#Classe pessoa é uma classe abstrata que vai servir de herança para outras classes.
class Pessoa:

    def __init__(self,nome,endereco,email,cpf,telefone) -> None:
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._cpf = cpf
        self._telefone = telefone
