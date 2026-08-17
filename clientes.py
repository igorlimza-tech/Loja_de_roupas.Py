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
        
    
    def alterar_nome_cliente(self, novo_nome):
        self.nome = novo_nome
        
        
    def alterar_data(self, nova_data):
        self.data_nascimento = nova_data
    
    
    def alterar_telefone(self, novo_telefone):
        self.telefone = novo_telefone
    
    
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


def alterar_nome_cliente(lista_clientes):
    cpf = ler_cpf("CPF: ")
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    if not cliente:
        print("Nenhum cliente encontrado!")
        return
    
    novo_nome = ler_nome("Digite o novo nome: ")
    cliente.alterar_nome_cliente(novo_nome)
    print("Nome alterado com sucesso!")
   

def alterar_data(lista_clientes):
    cpf = ler_cpf("CPF: ")
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    if not cliente:
        print("Nenhum cliente encontrado!")   
        return
    nova_data = ler_data("Digite a nova data de nascimento: ")
    cliente.alterar_data(nova_data)
    print("Nova data alterada com sucesso!")


def alterar_telefone(lista_clientes):
    cpf = ler_cpf("CPF: ") 
    cliente = busca_cliente_cpf(lista_clientes, cpf)
    if not cliente:
        print("Nenhum cliente cadastrado!")
        return

    novo_telefone = ler_telefone("Novo telefone: ")
    cliente.alterar_telefone(novo_telefone)
    print("Telefone alterado com sucesso!")