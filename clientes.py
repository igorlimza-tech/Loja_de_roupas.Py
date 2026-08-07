from utilidades import ler_int, ler_cpf

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
            
            
def busca_cliente_cpf(lista_clientes, cpf):
    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            return cliente
    return None