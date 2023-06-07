#Classe pessoa é uma classe que vai servir de herança para outras classes.
from abc import ABC,abstractclassmethod

#Uma classe abstrata
class Pessoa(ABC):
    #Atributos da classe
    def __init__(self,nome:str,endereco:str,email:str,cpf:str,telefone:int) -> None:
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._cpf = cpf
        self._telefone = telefone

    #Getter e setter
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self,nome:str):
        self._nome = nome
    
    @property   
    def endereco(self) -> str:
        return self._endereco
    @endereco.setter
    def endereco(self,endereco:str):
        self._endereco = endereco

    @property   
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self,email:str):
        self._email = email

    @property   
    def cpf(self) -> str:
        return self._cpf
    @cpf.setter
    def cpf(self,cpf:str):
        self._cpf = cpf
    
    @property   
    def telefone(self) -> int:
        return self._telefone
    @telefone.setter
    def telefone(self,telefone:int):
        self._telefone = telefone
