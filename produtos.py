from utilidades import ler_float, ler_int, linha, ler_codigo, ler_nome_produto


class Produto:
    def __init__(self, codigo_barras, nome, valor, quantidade):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
    
    def exibir_produto(self):
        print(f"Código: {self.codigo_barras}")
        print(f"Nome: {self.nome}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")
        linha()
    
    
    def baixar_estoque(self, quantidade):
        if quantidade > self.quantidade:
            print("A quantidade retirada não pode ser maior que a do estoque!")
            return
        if quantidade <=0:
            print("Retire uma quantidade maior que 0!")
            return    
        self.quantidade -= quantidade


    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Adicione uma quantidade maior que 0!")
            return
        self.quantidade += quantidade


    def alterar_preco(self, preco):
        if preco <=0:
            print("Insira um valor maior que 0")
            return
        self.valor = preco
        

    
def cadastrar_produtos(lista_estoque):
    codigo_barras = ler_codigo("Código: ")
    produto = busca_produto_codigo(lista_estoque, codigo_barras)
    if produto:
        print("Código de barras já cadastrado!")
        return
    
    nome = ler_nome_produto("Nome do produto: ")
    valor = ler_float("Valor: ")
    quantidade = ler_int("Quantidade: ")
    
    novo_produto = Produto(codigo_barras, nome, valor, quantidade)
    lista_estoque.append(novo_produto)
    print("Produto cadastrado com sucesso!")


def adicionar_estoque(lista_estoque):
    produto = selecionar_produto(lista_estoque)
    quantidade = ler_int("Qual quantidade deseja adicionar: ")
    produto.adicionar_estoque(quantidade)
    print("Estoque alterado com sucesso!")



def alterar_preco(lista_estoque):
    produto = selecionar_produto(lista_estoque)
    novo_preco = ler_float("Novo preço do produto: R$ ")
    produto.alterar_preco(novo_preco)
    print("Valor alterado com sucesso!")


def listar_estoque(lista_estoque):
    if not lista_estoque:
        print("Nenhum produto cadastrado!")
    else:
        for produto in lista_estoque:
            produto.exibir_produto()
            

def busca_produto_codigo(lista_estoque, codigo_barras):
    for produto in lista_estoque:
        if produto.codigo_barras == codigo_barras: 
            return produto
    return None


def selecionar_produto(lista_estoque):
    while True:
        print("===== PRODUTOS DISPONIVEIS =====")
        listar_estoque(lista_estoque)
             
        print("1- Buscar por nome ")
        print("2- Buscar por código ")
        opcao_busca = ler_int("Buscar por: ")
        if opcao_busca == 1:
            nome = input("Nome do produto: ").strip()
            if not nome:
                print("Digite um nome para realizar a busca!")
                continue
            
            encontrados = busca_produto_nome(lista_estoque, nome)
            
            if not encontrados:
                print("Nenhum produto encontrado!")
                continue
            
            for i, produto_encontrado in enumerate(encontrados, start=1):
                print(f"{i} - {produto_encontrado.nome}")

            opcao = ler_int("Qual produto deseja escolher: ")
            if  1 <= opcao <= len(encontrados):
                produto = encontrados[opcao-1]
            else:
                print("Opção inválida. Digite um número dentro das opçoes disponiveis! ")
                continue 
                
        elif opcao_busca == 2:
            codigo_barras = ler_codigo("Código do produto que deseja: ")
            produto = busca_produto_codigo(lista_estoque, codigo_barras) 
        
            
            if not produto:
                print("Produto não cadastrado. Tente novamente!")
                continue
        
        else:
            print("Escolha 1 para nome ou 2 para código")
            continue
        
        print("Produto selecionado!")
        return produto

def busca_produto_nome(lista_estoque, nome):
    encontrados = []
    
    for produto in lista_estoque:
        if nome.lower() in produto.nome.lower():
            encontrados.append(produto)
            
    return  encontrados        