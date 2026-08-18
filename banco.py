import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

for cliente in clientes:
    print(f"Id: {cliente[0]}")
    print(f"CPF: {cliente[1]}")
    print(f"Nome: {cliente[2]}")
    print(f"Data de Nascnimento: {cliente[3]}")
    print(f"Telefone: {cliente[4]}")
    
cpf = "10154243222"
nome = "LOUD"
data_nascimento = "2001-04-22"
telefone = "32946443921"

comando = """
INSERT INTO clientes(cpf, nome, data_nascimento, telefone) 
VALUES(%s, %s, %s, %s)
"""
valores = (cpf, nome, data_nascimento, telefone) 

cursor.execute(comando, valores)
conexao.commit()

cursor.close()
conexao.close()