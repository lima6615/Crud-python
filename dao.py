import mysql.connector
from mysqlx import Error

class Dao():

    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='DB_COSMETICO',
            )
        except Error as er:
            print(f"Error ao efetuar conexão: {a}!".format(er))

    def product_All(self):
        cursor = self.conexao.cursor()
        cursor.execute(f'SELECT * FROM PRODUTO')
        resultado = cursor.fetchall()
        return resultado

    def insert (self, produtos):
        cursor = self.conexao.cursor()
        sql = 'INSERT INTO PRODUTO (NOME, DESCRICAO, VALOR) VALUES("{0}", "{1}", {2})'
        cursor.execute(sql.format(produtos[0], produtos[1], produtos[2]))
        self.conexao.commit()
        print("Produto cadastrado!")

    def update(self, produto):
        cursor = self.conexao.cursor()
        sql = "UPDATE PRODUTO  SET NOME = '{0}' , DESCRICAO = '{1}', VALOR = {2} WHERE ID = {3}";
        cursor.execute(sql.format(produto[1], produto[2], produto[3], produto[0]))
        self.conexao.commit()
        print("Produto Atualizado!")

    def delete(self, id):
        cursor = self.conexao.cursor()
        cursor.execute(f'DELETE FROM PRODUTO WHERE ID = {id}')
        self.conexao.commit()
        print("Produto Deletado!")


