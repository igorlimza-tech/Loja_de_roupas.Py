from datetime import datetime 

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


def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        
        if nome and all(caractere.isalpha() or caractere.isspace()  for caractere in nome):
            return nome
        
        print("Nome inválido! Digite apenas letras e espaços.")
        

def ler_nome_produto(mensagem):
    while True:
        nome_produto = input(mensagem).strip()
        
        if nome_produto and any(caractere.isalpha() for caractere in nome_produto):
            return nome_produto
        
        print("Nome inválido. Tente novamente!")


def ler_codigo(mensagem):
    while True:
        codigo = input(mensagem).strip()
        if len(codigo) not in (8,12,13,14):
            print("O tamanho do código está incorreto")
            continue
        if not codigo.isdigit():
            print("Digite apenas números no código de barras")
            continue
        return codigo
        
        
def ler_telefone(mensagem):
    while True:
        telefone = input(mensagem)
        telefone = telefone.strip()
        telefone = telefone.replace("(", "").replace(")","").replace("-","").replace(" ", "")
        if (len(telefone) == 10 or len(telefone) == 11) and telefone.isdigit():
            return telefone
        
        print("Número de telefone inválido. Tente novamente!")
        

def ler_sim_nao(mensagem):
    while True:
        opcao = input(mensagem).strip().upper()
        if opcao in ("S","N"):
            return opcao
        print("Opção inválida. Digite apenas S ou N ")     


def ler_data(mensagem):
    while True:
        data_nascimento = input(mensagem).strip()
        try:
            data = datetime.strptime(data_nascimento, "%d/%m/%Y")
            return data.date()
        except ValueError:
            print("Data de nascimento inválida. Digite no formato DD/MM/AAAA")           
        
    
def linha():
    print("-"*30)


def pausar():
    input("\nPressione ENTER para continuar...")
