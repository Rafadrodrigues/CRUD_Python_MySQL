#Classe pessoa é uma classe que vai servir de herança para outras classes.
from classSistema import Sistema

class Pessoa:

    def __init__(self) -> None:
        self._nome = None
        self._endereco = None
        self._email = None
        self._cpf = None
        self._telefone = None
