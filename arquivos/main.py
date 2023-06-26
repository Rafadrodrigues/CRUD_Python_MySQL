from time import sleep
from datetime import datetime
import Banco_de_dados
import pytz
import os

'''                                     IMPORTANTE
Eu criei esse projeto para tentar testar meus conhecimentos em orientacao a objetos e integraçao com 
banco de dados, porém, futuramente, vou estar realizando uma manutenção no código e pretendo integralo
com alguma interface grafica e deixa-lo com "mais cara " de Python. Esse é um planejamento que pretendo 
para o mês de agosto, mes que vou estar de ferias da faculdade e consequentemente vou ter mais tempo
para dar atençao"'''



#Funcao que recebe o usuário e mostrando as opções
def inicio():
    
    print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-")

    opcao = input('Qual opção deseja? ')
    print(
        "1 - Inserir\n" + 
        "2 - Deletar\n" +
        "3 - Vizualizar\n" + 
        "4 - Sair" 
        )
    
    opcao_tipo = input('Qual opção deseja? ')
    os.system("cls")

    if "Inserir" or "Deletar" or "Vizualizar" in opcao:
        print(
            "1 - Funcionário\n" + 
            "2 - Cliente\n" +
            "3 - Material\n" + 
            "4 - Venda\n" + 
            "5 - Sair"  
        )

    lista_opcoes = {"Inserir":{1:"Funcionário",2:"Cliente",3:"Material",4:"Venda"},
        "Deletar":{1:"Funcionário",2:"Cliente",3:"Material",4:"Venda"},
        "Vizualizar":{1:"Funcionário",2:"Cliente",3:"Material",4:"Venda"},
    }

    # saida = str(lista_opcoes).replace("{", "").replace("}", "").replace("'", "")

    # print(saida)
    # os.system("cls")

    # selecao = [opcao for opcao in lista_opcoes if opcao in lista_opcoes]

def _data_hora():
    fuso_BR = pytz.timezone('Brazil/East')
    horario_BR = datetime.now(fuso_BR)
    return horario_BR.strftime('%d/%m/%y %H:%M:%S')

def coletar_info_func():
#Coletando informações do funcionário.
    cadastrar_funcionario(
        nome = input('Insira seu nome: '),
        idade = int(input('Insira sua idade: ')),
        cpf = input('Insira seu CPF: '),
        telefone = input('Insira seu Telefone: '),
        cargo = input('Insira seu Cargo: '),
        endereco = input('Rua e Número da sua casa: '),
    )
def coletar_info_clien():
#Coletando informações do Cliente.
    cadastrar_cliente(
        nome = input('Insira seu nome: '),
        idade = int(input('Insira sua idade: ')),
        cpf = input('Insira seu CPF: '),
        telefone = input('Insira seu Telefone: '),
        endereco = input('Rua e Número da sua casa: '),
    )
def coletar_info_venda():
#Coletando informações da Venda.
    cadastrar_venda(
        nome = input('Nome do material vendido: '),
        valor = float(input('Valor da venda: ')),
        quantidade = float(input('Quantidade Vendida: ')),
        data_hora = _data_hora()
    )
def coletar_info_mate():
#Coletando informações do material.
    cadastrar_material(
        nome = input('Nome do material: '),
        quantidade = int(input('Quantidade: ')),
        valor = float(input('Valor da material: ')),
    )

#Funcao que realiza o cadastro de funcionarios na base de dados
cadastrar_funcionario = lambda *args, **kwargs: print(kwargs) 

#Funcao que realiza o cadastro de clientes na base de dados
cadastrar_cliente = lambda *args, **kwargs : print(kwargs)

#Funcao que realiza o cadastro de vendas na base de dados
cadastrar_venda = lambda *args, **kwargs: print(kwargs)

#Funcao que realiza o cadastro de materiais na base de dados
cadastrar_material = lambda *args, **kwargs: print(kwargs)

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":

    inicio()
    # os.system("cls")
    # sleep(2)

    # if 'Funcionario' or 'Cliente' or 'Material' or 'Venda' in selecao:
    #     Banco_de_dados.inserir_na_bd('Funcionario')
    # if 'Funcionario' in selecao:
    #     Banco_de_dados.deletar_na_bd()
    # if 'Funcionario' in selecao:
    #     Banco_de_dados.vizualizar_na_bd()
