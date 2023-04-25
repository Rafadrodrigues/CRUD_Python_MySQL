import mysql.connector
#conectamos o python com banco de dados
con = mysql.connector.connect(host='localhost', database='name_bd', user='root', password='88554663')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor MySQL')
    #Curso serve para nosso código interagir com o BD 
    cursor = con.cursor()
    cursor.execute('Select Database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados ',linha)

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão com MySql foi encerrada. ')