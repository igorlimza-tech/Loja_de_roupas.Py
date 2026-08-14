from utilidades import ler_float, ler_int, linha, ler_codigo, ler_nome_produto


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
        if quantidade <=0:
            print("Adicione uma quantidade maior que 0!")
            return
        self.quantidade += quantidade


    def alterar_preco(self,preco):
        if preco <=0:
            print("Insira um valor maior que 0")
            return
        self.valor = preco
        

    
def cadastrar_produtos(lista_estoque):
    codigo_barras = ler_codigo("Código: ")
    produto = busca_produto_codigo(lista_estoque,codigo_barras)
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
    codigo_barras = ler_codigo("Código do produto: ")
    produto = busca_produto_codigo(lista_estoque, codigo_barras)
    if not produto:
        print("Produto não cadastrado!")
        return
    quantidade = ler_int("Quantidade a adicionar:")
    produto.adicionar_estoque(quantidade)
    print("Estoque atualizado com sucesso!")


def alterar_preco(lista_estoque):
    codigo_barras = ler_codigo("Código do produto: ")
    produto = busca_produto_codigo(lista_estoque, codigo_barras)
    if not produto:
        print("Produto não cadastrado!")
        return
    novo_preco = ler_float("Qual o novo preço: R$ ") 
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
