# Ferramentas utilizadas.

  Para executar será preciso ter o python instalado em seu PC. 
  
    Site para baixar o python:https://www.python.org/downloads/
  
  Baixando o MySQL:
  
    Site para baixar o MySQL:https://dev.mysql.com/downloads/installer/
    
  Após isso, vá ao local onde foi baixado o arquivo e comece o processo de instalação.
  
  Baixando o VSCODE:
  
    Site para baixar o VSCODE:https://code.visualstudio.com/download

  Após isso, vá ao local onde foi baixado o arquivo e comece o processo de instalação.
  
  Para esse executar esse código foi necessário apenas a extensão Python. A mesma pode ser instalada;
  
    Extensão > Python > Instalar.
    
    Versão do Python instalada no meu computador - 3.10.8
  
  Para inserir os dados na base de dados, primeiramente,é preciso criar as tabelas na ferramenta de manipulação do SGBD,
  utilizei o WorkBench, porém fica a escolha do usuário.
  
  A criação das tabelas foram feitas manualmente no Worbench, sendo elas;
  
    table_cliente: columns = id_cliente, nome_cliente, endereco_cliente, email_cliente, cpf_cliente, telefone_cliente
    table_colaborador: columns = id_colaborador, nome_cola, endereco_cola, email_cola, cpf_cola, telefone_cola, user_cola, senha_cola.
    table_material: columns = id_material, nome_material, quantidade_material, preco_material, especificacao_material, dataFabricacao_material, fornecedor_material.
    table_vendas: columns = id_vendas, data_vendas, valorTotal_vendas.
  
  Este código foi construído no Windows 10 64x, não foi testado em Linux.
