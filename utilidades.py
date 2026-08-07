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



    



