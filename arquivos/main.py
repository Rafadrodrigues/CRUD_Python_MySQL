from time import sleep
from datetime import datetime
import Banco_de_dados
import pytz
import os

"""
=============================ATENCAO==========================================================
Esse projeto foi construído em um cenário fictício, onde uma empresa de Material de construção
realiza alguns inserções no Banco de dados. Esse projeto foi criado de forma simples e com 
intuito de fortalecer meus conhecimentos em Python e MySQL.
"""

#Função que vai representar as informaçoes ao usuário
def inicio() :
    
    print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-")
    print(
        "1 - Inserir\n" + 
        "2 - Deletar\n" +
        "3 - Vizualizar\n" + 
        "4 - Sair" 
        )
    opcao = input('Qual opção deseja? ')
    os.system("cls")

    if "Inserir" or "Deletar" or "Vizualizar" in opcao:
        print(
            "1 - Funcionário\n" + 
            "2 - Cliente\n" +
            "3 - Material\n" + 
            "4 - Venda\n" + 
            "5 - Sair"  
        )
    opcao_tipo = input('Qual opção deseja? ')
    os.system("cls")

    #Inserindo funcionario na base de dados
    if "Inserir" in opcao and "Funcionário" in opcao_tipo:
        funcionario = coletar_info_func()
        Banco_de_dados.inserir_na_bd("Funcionário",funcionario)
    #Inserindo cliente na base de dados
    if "Inserir" in opcao and "Cliente" in opcao_tipo:
        cliente = coletar_info_clien()
        Banco_de_dados.inserir_na_bd("Cliente",usuario=cliente)
    #Inserindo material na base de dados
    if "Inserir" in opcao and "Material" in opcao_tipo:
        material = coletar_info_mate()
        Banco_de_dados.inserir_na_bd("Material",usuario=material)
    #Inserindo venda na base de dados
    if "Inserir" in opcao and "Venda" in opcao_tipo:
        venda = coletar_info_venda()
        Banco_de_dados.inserir_na_bd("Venda",usuario=venda)
    #Deletando funcionario na base de dados
    if "Deletar" in opcao and "Funcionário" in opcao_tipo:
        funcionario = input("Insira o CPF: ")
        Banco_de_dados.deletar_na_bd( "Funcionário",funcionario)
    #Deletando cliente na base de dados
    if "Deletar" in opcao and "Cliente" in opcao_tipo:
        cliente = input("Insira o CPF: ")
        Banco_de_dados.deletar_na_bd("Cliente",cliente)
    #Deletando material na base de dados
    if "Deletar" in opcao and "Material" in opcao_tipo:
        material = input("Nome do material: ")
        Banco_de_dados.deletar_na_bd("Material",material)
    #Deletando venda na base de dados
    if "Deletar" in opcao and "Venda" in opcao_tipo:
        venda = material = input("Nome da venda: ")
        Banco_de_dados.deletar_na_bd("Venda",venda)
    #Vizualizando Funcionário na base de dados
    if "Vizualizar" in opcao and "Funcionário" in opcao_tipo:
        Banco_de_dados.vizualizar_na_bd("Funcionário")
    #Vizualizando cliente na base de dados
    if "Vizualizar" in opcao and "Cliente" in opcao_tipo:
        Banco_de_dados.vizualizar_na_bd("Cliente")
    #Vizualizando material na base de dados
    if "Vizualizar" in opcao and "Material" in opcao_tipo:
        Banco_de_dados.vizualizar_na_bd("Material")
    #Vizualizando venda na base de dados
    if "Vizualizar" in opcao and "Venda" in opcao_tipo:
        Banco_de_dados.vizualizar_na_bd("Venda")

def _data_hora() -> datetime:
#Coletando data e hora para servir de informaçao na venda
    fuso_BR = pytz.timezone('Brazil/East')
    horario_BR = datetime.now(fuso_BR)
    return horario_BR.strftime('%d/%m/%y %H:%M:%S')

def coletar_info_func() -> dict:
    nome = input('Insira seu nome: ')
    idade = int(input('Insira sua idade: '))
    cpf = input('Insira seu CPF: ')
    telefone = input('Insira seu Telefone: ')
    cargo = input('Insira seu Cargo: ')
    endereco = input('Rua e Número da sua casa: ')

    funcionario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'telefone': telefone,
        'cargo': cargo,
        'endereco': endereco,
    }

    return funcionario

def coletar_info_clien() -> dict:
#Coletando informações do Cliente.

    nome = input('Insira seu nome: ')
    idade = int(input('Insira sua idade: '))
    cpf = input('Insira seu CPF: '),
    telefone = input('Insira seu Telefone: ')
    endereco = input('Rua e Número da sua casa: ')

    cliente = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'telefone': telefone,
        'endereco': endereco,
    }
    return cliente

def coletar_info_venda() -> dict:
#Coletando informações da Venda.

    nome = input('Nome do material vendido: ')
    valor = float(input('Valor da venda: '))
    quantidade = float(input('Quantidade Vendida: '))
    data_hora = _data_hora()

    venda = {
        "nome": nome,
        "valor": valor,
        "quantidade": quantidade,
        "data_hora":data_hora,
    }
    return venda

def coletar_info_mate() -> dict: 
#Coletando informações do material.

    nome = input('Nome do material: ')
    data_hora = _data_hora()
    valor = float(input('Valor da material: '))
    
    material = {
        "nome": nome,
        "valor": valor,
        "data": data_hora,
    }

    return material

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":
    """
Os comandos comentados, são para criação da base de dados e das tabelas que serão utilizadas.
Para aqueles que já executaram o código em sua máquina, deixem comentado para que não ocorra erro
pois a tabela já vai ter sido criado, caso não tenha executado nenhuma vez, retire os comentários da
das linhas abaixo. 
    """
# Banco_de_dados.criar_base()
# sleep(2)
# os.system("cls")
# Banco_de_dados.criar_tabelas()
# sleep(2)
# os.system("cls")
inicio()