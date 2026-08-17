from utilidades import ler_int, pausar
from clientes import cadastrar_cliente, listar_clientes, alterar_nome_cliente, alterar_data, alterar_telefone
from produtos import cadastrar_produtos, listar_estoque, alterar_preco, adicionar_estoque, alterar_nome_produto, alterar_codigo
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
    print("8- Gerenciamento de clientes") 
    print("9- Sair do Programa")


def sub_menu_produtos():
    print("=== GERENCIAMENTO DO ESTOQUE ===")
    print("1- Adicionar produtos ao estoque")
    print("2- Alterar valor do produto")
    print("3- Alterar o nome do produto")
    print("4- Alterar o código do produto")
    print("5- Voltar ao menu principal")
    
def sub_menu_clientes():   
    print("=== GERENCIAMENTO DO CLIENTE ===")
    print("1- Alterar o nome: ")
    print("2- alterar o telefone: ")
    print("3- Alterar a data de nascimento: ")
    print("4- Voltar ao menu principal")

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
                sub_menu_produtos()
                sub_opcao_produtos = ler_int("Qual opção deseja: ")
                if sub_opcao_produtos == 1:
                    adicionar_estoque(lista_estoque)
                elif sub_opcao_produtos == 2:
                    alterar_preco(lista_estoque)
                elif sub_opcao_produtos == 3:
                    alterar_nome_produto(lista_estoque)
                elif sub_opcao_produtos == 4:
                    alterar_codigo(lista_estoque)
                elif sub_opcao_produtos == 5:
                    print("Voltando ao menu principal")
                    break 
                else:
                    print("Digite uma opção de 1 a 5")
                    
        elif opcao == 8:        
            if not lista_clientes:
                print("Nenhum cliente cadastrado!")
                continue
            
            while True:
                sub_menu_clientes()
                sub_opcao_clientes = ler_int("Qual opçaõ deseja: ")
                if sub_opcao_clientes == 1:
                    alterar_nome_cliente(lista_clientes)
                elif sub_opcao_clientes == 2:
                    alterar_telefone(lista_clientes)
                elif sub_opcao_clientes == 3:
                    alterar_data(lista_clientes)
                elif sub_opcao_clientes == 4:
                    print("Voltando para o menu principal...")
                    break
                else:
                    print("Digite uma opção de 1 a 4 ")
                    
        elif opcao == 9:
            print("Saindo do Programa...")
            break

        else:
            print("Digite uma opção de 1 a 9 ")

if __name__ == "__main__":
    main()