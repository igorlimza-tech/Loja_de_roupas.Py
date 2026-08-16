from utilidades import ler_int, pausar
from clientes import cadastrar_cliente, listar_clientes
from produtos import cadastrar_produtos, listar_estoque, alterar_preco, adicionar_estoque
from vendas import cadastrar_venda, listar_vendas

def menu():
    print(("=" * 10) + " LOJA DE ROUPAS.PY " + ("=" * 10))
    print("1- Cadastrar cliente")
    print("2- Listar clientes")
    print("3- Cadastrar produto")
    print("4- Listar estoque")
    print("5- Realizar venda")
    print("6- Listar vendas")
    print("7- Gerenciamento do estoque") 
    print("8- Sair do Programa")


def sub_menu():
    print("=== GERENCIAMENTO DO ESTOQUE ===")
    print("1- Adicionar produtos ao estoque")
    print("2- Alterar valor do produto")
    print("3- Voltar ao menu principal")


def main():                    
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
            pausar()
        
        elif opcao == 3:
            cadastrar_produtos(lista_estoque)
        
        elif opcao == 4:
            listar_estoque(lista_estoque)
            pausar()
        
        elif opcao == 5:
            cadastrar_venda(lista_vendas, lista_clientes, lista_estoque)
        
        elif opcao == 6:
            listar_vendas(lista_vendas)
            pausar()

        elif opcao == 7:
            if not lista_estoque:
                print("Nenhum produto cadastrado no estoque!")
                continue
            while True:
                sub_menu()
                sub_opcao = ler_int("Qual opção deseja: ")
                if sub_opcao == 1:
                    adicionar_estoque(lista_estoque)
                elif sub_opcao == 2:
                    alterar_preco(lista_estoque)
                elif sub_opcao == 3:
                    print("Voltando ao menu principal")
                    break 
                else:
                    print("Digite uma opção de 1 a 3")
                
            
        elif opcao == 8:
            print("Saindo do Programa...")
            break

        else:
            print("Digite uma opção de 1 a 8 ")

if __name__ == "__main__":
    main()