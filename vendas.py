from utilidades import ler_cpf, ler_int
from clientes import busca_cliente_cpf
from produtos import busca_produto_codigo


class Venda:
    def __init__(self,cliente, produto, quantidade, pagamento, valor_total):
        self.cliente = cliente 
        self.produto = produto     
        self.quantidade = quantidade
        self.pagamento = pagamento
        self.valor_total = valor_total
     
     
    def exibir_venda(self):
        print("-"*30)
        print(f"Cliente: {self.cliente.nome}")
        print(f"Produto: {self.produto.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Forma de pagamento: {self.pagamento}")
        print(f"Valor total da venda: R${self.valor_total:.2f}")
        
            
def cadastrar_venda(lista_vendas, lista_clientes, lista_estoque):
    cpf = ler_cpf("CPF: ")
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    if not cliente:
        print("Cliente não cadastrado. Tente novamente!")
        return
    codigo_barras = input("Código de barras: ")
    produto = busca_produto_codigo(lista_estoque,codigo_barras)
    if not produto:
        print("Produto não cadastrado. Tente novamente!")
        return
    quantidade = ler_int("Quantidade: ")
    if quantidade > produto.quantidade:
        print("Estoque insuficiente!")
        return
    if quantidade <=0:
        print("A quantidade deve ser maior que 0")
        return
    produto.quantidade -= quantidade
    pagamento = menu_pagamento()
    valor_total = (produto.valor * quantidade)
    print(f"Valor da compra: R${valor_total}")
    nova_venda = Venda(cliente, produto, quantidade, pagamento, valor_total)
    lista_vendas.append(nova_venda)
    
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