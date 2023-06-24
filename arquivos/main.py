from time import sleep
from datetime import datetime
import pytz
import os

#Funcao que recebe o usuário e mostrando as opções
def inicio():
    
    print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-")
    print("01 - Cadastrar Funcionário\n" + 
        "02 - Cadastrar Cliente\n" +
        "03 - Cadastrar Material\n" + 
        "04 - Cadastrar Venda\n" + 
        "05 - Atualizar Funcionário\n" + 
        "06 - Atualizar Cliente\n" +
        "07 - Remover Funcionário\n" +
        "08 - Remover Cliente\n" +
        "09 - Remover Material\n" +
        "10 - Remover Venda\n" +
        "11 - Sair do sistema\n"
        )

def _data_hora():
    fuso_BR = pytz.timezone('Brazil/East')
    horario_BR = datetime.now(fuso_BR)
    return horario_BR.strftime('%d/%m/%y %H:%M:%S')

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

    lista_opcoes = [
        'Cadastrar Funcionário',
        'Cadastrar Cliente',
        'Cadastrar Material',
        'Cadastrar Venda',
        'Atualizar Funcionário',
        'Atualizar Cliente',
        'Remover Funcionário',
        'Remover Cliente',
        'Remover Material',
        'Remover Venda',
        'Sair'
    ]

    print([i for i in lista_opcoes])
#Coletando informações do funcionário.
    cadastrar_funcionario(
        nome = input('Insira seu nome: '),
        idade = int(input('Insira sua idade: ')),
        cpf = input('Insira seu CPF: '),
        telefone = input('Insira seu Telefone: '),
        cargo = input('Insira seu Cargo: '),
        endereco = input('Rua e Número da sua casa: '),
    )

#Coletando informações do Cliente.
    cadastrar_cliente(
        nome = input('Insira seu nome: '),
        idade = int(input('Insira sua idade: ')),
        cpf = input('Insira seu CPF: '),
        telefone = input('Insira seu Telefone: '),
        endereco = input('Rua e Número da sua casa: '),
    )

#Coletando informações da Venda.
    cadastrar_venda(
        nome = input('Nome do material vendido: '),
        valor = float(input('Valor da venda: ')),
        quantidade = float(input('Quantidade Vendida: ')),
        data_hora = _data_hora()
    )

#Coletando informações do material.
    cadastrar_material(
        nome = input('Nome do material: '),
        quantidade = int(input('Quantidade: ')),
        valor = float(input('Valor da material: ')),
    )

'''                                     IMPORTANTE
Eu criei esse projeto para tentar testar meus conhecimentos em orientacao a objetos e integraçao com 
banco de dados, porém, futuramente, vou estar realizando uma manutenção no código e pretendo integralo
com alguma interface grafica e deixa-lo com "mais cara " de Python. Esse é um planejamento que pretendo 
para o mês de agosto, mes que vou estar de ferias da faculdade e consequentemente vou ter mais tempo
para dar atençao"'''


