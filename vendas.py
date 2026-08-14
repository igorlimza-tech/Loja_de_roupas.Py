from utilidades import ler_cpf, ler_int, linha, ler_codigo, ler_sim_nao
from clientes import busca_cliente_cpf
from produtos import busca_produto_codigo, listar_estoque

class Venda():
    def __init__(self,cliente, itens, pagamento, valor_total):
        self.cliente = cliente 
        self.itens = itens
        self.pagamento = pagamento
        self.valor_total = valor_total
     
     
    def exibir_venda(self):
        linha()
        print(f"Cliente: {self.cliente.nome}")
        linha()
        for item in self.itens:
            produto = item["Produto"]
            print(f'Produto: {produto.nome}')
            print(f'Valor Unitário: {item["Preco_Unitario"]:.2f}')
            print(f'Quantidade: {item["Quantidade"]}')
            print(f'Subtotal: R$ {item["Subtotal"]:.2f}')
        linha()
        print(f"Forma de pagamento: {self.pagamento}")
        print(f"Valor total da venda: R${self.valor_total:.2f}")
        
            
def cadastrar_venda(lista_vendas, lista_clientes, lista_estoque):
    if not lista_clientes:
        print("Cliente não cadastrado. Tente novamente!")
        return
    if not lista_estoque:
        print("Nenhum produto cadastrado no estoque! ")
        return
    
    cpf = ler_cpf("CPF: ")
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    if not cliente:
        print("Cliente não cadastrado. Tente novamente!")
        return
    
    carrinho = montar_carrinho(lista_estoque)
    valor_total = 0
    for item in carrinho:
        valor_total+=item["Subtotal"]
     
    pagamento = menu_pagamento()
    
    for item in carrinho:
        produto = item["Produto"]
        quantidade = item["Quantidade"]
        produto.baixar_estoque(quantidade)
        
    nova_venda = Venda(cliente, carrinho, pagamento, valor_total)
    lista_vendas.append(nova_venda)
    print(f"Venda realizada com sucesso! Valor da compra: R${valor_total:.2f}")


def montar_carrinho(lista_estoque):
    carrinho = []
        
    while True:
        print("===== PRODUTOS DISPONIVEIS =====")
        listar_estoque(lista_estoque)
        
        codigo_barras = ler_codigo("Código do produto que deseja selecionar: ")
        produto = busca_produto_codigo(lista_estoque,codigo_barras)
        
        if not produto:
            print("Produto não cadastrado. Tente novamente!")
            continue
        
        print("produto selecionado:")
        linha()
        produto.exibir_produto()
            
        quantidade = ler_int("Quantidade: ")
        
        if quantidade > produto.quantidade:
            print("Estoque insuficiente!")
            print(f"Quantidade disponível: {produto.quantidade}")
            continue
        
        produto_existe = False
        quantidade_invalida = False

        for item in carrinho:
            if item["Produto"] == produto:
                produto_existe = True
                
                if item["Quantidade"] + quantidade > produto.quantidade:
                    print("Quantidade solicitada ultrapassa o estoque disponível.")
                    quantidade_invalida = True
                    break
                else:
                    item["Quantidade"] += quantidade
                    item["Subtotal"]= item["Preco_unitario"] * item["Quantidade"]
                    break
       
                
        if quantidade_invalida:
            continue
                
        
        if not produto_existe:                    
            item = {"Produto": produto,
                    "Quantidade": quantidade,
                    "Preco_Unitario": produto.valor,
                    "Subtotal": produto.valor * quantidade }
        
            carrinho.append(item)
        
        opcao = ler_sim_nao("Deseja escolher mais produtos? [S/N]: ")
        if opcao == "S":
            continue
    
        return carrinho
        
    
    
def menu_pagamento():
    while True:
        print(("="*10)+ " FORMA DE PAGAMENTO " +("="*10))
        print("1- Dinheiro")
        print("2- Cartão de débito")
        print("3- Cartão de crédito")
        print("4- Pix")
        
        opcao = ler_int("Opção desejada: ")
        if opcao == 1:
            return "Dinheiro"
        elif opcao == 2:
            return "Cartão de débito"
        elif opcao == 3:
            return "Cartão de crédito"
        elif opcao == 4:
            return "Pix"
        else:
            print("Opção inválida. Tente novamente!")

def listar_vendas(lista_vendas):
    if not lista_vendas:
        print("Nenhuma venda realizada!")
    else:
        for venda in lista_vendas:
            venda.exibir_venda()