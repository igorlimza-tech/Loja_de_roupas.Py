from utilidades import ler_int
from clientes import cadastrar_cliente, listar_clientes
from produtos import cadastrar_produtos, listar_estoque
from vendas import  cadastrar_venda, listar_vendas

def menu():
    print(("="*10)+ " lOJA DE ROUPAS.PY " +("="*10))
    print("1- Cadastrar cliente")
    print("2- listar clientes")
    print("3- Cadastrar produto")
    print("4- listar estoque")
    print("5- Realizar venda")
    print("6- Listar vendas") 
    print("7- Sair do Programa")
                    
lista_clientes = []
lista_estoque = []
lista_vendas = []

while True:
    menu()
    opcao = ler_int("Qual opção deseja: ")

    if opcao == 1:
        cadastrar_cliente(lista_clientes)
        
    elif opcao == 2:
        listar_clientes(lista_clientes)
    
    elif opcao == 3:
        cadastrar_produtos(lista_estoque)
    
    elif opcao == 4:
        listar_estoque(lista_estoque)
    
    elif opcao == 5:
        cadastrar_venda(lista_vendas, lista_clientes, lista_estoque)
    
    elif opcao == 6:
        listar_vendas(lista_vendas)
        
    elif opcao == 7:
        print("Saindo do Programa...")
        break 