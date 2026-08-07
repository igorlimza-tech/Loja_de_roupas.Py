class Cliente:
    def __init__(self,cpf, nome, idade, telefone):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
    
    def exibir_dados(self):
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome} ")
        print(f"Idade: {self.idade} ")
        print(f"Telefone: {self.telefone}")
    
    
def cadastrar_cliente(lista_clientes):
    cpf = ler_cpf("CPF: ")
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    if cliente:
        print("CPF já cadastrado!")
        return
    
    nome = input("Nome: ")
    idade = ler_int("Idade: ")             
    telefone = input("Telefone: ")
    novo_cliente = Cliente(cpf, nome, idade, telefone)
    lista_clientes.append(novo_cliente) 
    print("Cliente cadastrado com sucesso!")

def listar_clientes(lista_clientes):
    if not lista_clientes:
        print("Nenhum cliente cadastrado!")
    else:
        for cliente in lista_clientes:
            cliente.exibir_dados()


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
    print(produto.quantidade)
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

        
class Produto:
    def __init__(self,codigo_barras, nome, valor, quantidade):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
    
    def exibir_produto(self):
        print(f"Código: {self.codigo_barras}")
        print(f"Nome: {self.nome}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")
        print("-"*30)

    
def cadastrar_produtos(lista_estoque):
    codigo_barras = input("Código: ")
    produto = busca_produto_codigo(lista_estoque,codigo_barras)
    if produto:
        print("Código de barras já cadastrado!")
        return
    nome = input("Nome do produto: ")
    valor = ler_float("Valor: ")
    quantidade = ler_int("Quantidade: ")
    
    novo_produto = Produto(codigo_barras, nome, valor, quantidade)
    lista_estoque.append(novo_produto)
    print("Produto cadastrado com sucesso!")

    
def listar_estoque(lista_estoque):
    if not lista_estoque:
        print("Nenhum produto cadastrado!")
    else:
        for produto in lista_estoque:
            produto.exibir_produto()
            

def listar_vendas(lista_vendas):
    if not lista_vendas:
        print("Nenhuma venda realizada!")
    else:
        for venda in lista_vendas:
            venda.exibir_venda()


def ler_int(mensagem):
    while True:
        try: 
            num = int(input(mensagem))
            if num >0:
                return num
            else:
                print("Insira um valor maior que 0")
        except ValueError:
            print("Digite apenas números inteiros!")
            

def ler_float(mensagem):
    while True:
        try: 
            num = input(mensagem)
            num = num.replace(",", ".")
            num = float(num)
            if num >0:
                return num
            else:
                print("Insira um valor maior que 0")
        except ValueError:
            print("Digite apenas números!")
            
            
def validar_cpf(cpf):
    cpf = cpf.strip()
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito_1 = resto if resto < 10 else 0

    if digito_1 != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito_2 = resto if resto < 10 else 0

    if digito_2 != int(cpf[10]):
        return False

    return True


def ler_cpf(mensagem):
    while True:
        cpf = input(mensagem)

        if validar_cpf(cpf):
            return cpf.replace(".", "").replace("-", "")

        print("CPF inválido. Tente novamente!")


def busca_cliente_cpf(lista_clientes, cpf):
    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            return cliente
    return None
    


def busca_produto_codigo(lista_estoque, codigo_barras):
    for produto in lista_estoque:
        if produto.codigo_barras == codigo_barras: 
            return produto
    return None
       

def menu_pagamento():
    while True:
        print(("="*10)+ "FORMA DE PAGAMENTO " +("="*10))
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
            
                   
def menu():
    print(("="*10)+ "lOJA DE ROUPAS.PY " +("="*10))
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