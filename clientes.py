from utilidades import ler_cpf, ler_nome, ler_telefone, ler_data, linha

class Cliente:
    def __init__(self,cpf, nome, data_nascimento, telefone):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
    
    def exibir_dados(self):
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Telefone: {self.telefone}")
        linha()
    
def cadastrar_cliente(lista_clientes):
    cpf = ler_cpf("CPF: ")
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    
    if cliente:
        print("CPF já cadastrado!")
        return
    
    nome = ler_nome("Nome: ")
    data_nascimento = ler_data("Data de nascimento: ")             
    telefone = ler_telefone("Telefone: ")
    
    novo_cliente = Cliente(cpf, nome, data_nascimento, telefone)
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