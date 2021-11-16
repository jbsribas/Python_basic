import pyodbc as db

def conecta_old():
    conexao = db.connect("Driver=;"
                      "Server=server_name;"
                      "Database=db_name;"
                      "Trusted_Connection=yes;")
    return conexao

def conecta(driver,server,dbName):
    conexao = db.connect("Driver="+driver+";"
                      "Server="+server+";"
                      "Database="+dbName+";"
                      "Trusted_Connection=yes;")
    return conexao


#consulta consulta mostrando os resultados na tela
def consultaV(tabela,conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM '+tabela)

    for linha in cursor:
        print('row = %r' % (linha,))

#uma consulta retornando todos os registros sem mostrar na tela
def consultaR(tabela,conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM '+tabela)

    return cursor

#uma consulta retornando todos os registros sem mostrar na tela
def consultaClienteIdade(conexao,idade):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM cliente'+
                    "where IDADE >="+idade)
    return cursor
