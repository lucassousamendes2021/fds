import os
os.system("cls")


def calcular_inss(salario):

    return salario * 0.09

def calcular_vt(salario, quer_receber):

    if quer_receber == 's':
        return salario * 0.06
    else:
        return 0.0

def calcular_vr(valor_beneficio):
   
    return valor_beneficio * 0.20

def calcular_dependentes(quantidade):
    
    return quantidade * 150.00




def executar_sistema():
    print("="*30)
    print("SISTEMA DE FOLHA DE PAGAMENTO ")
    print("="*30)
executar_sistema()
matricula = input("Digite a sua matrícula: ")
senha = input("Digite a sua senha: ")
if matricula == 123456 and senha == 789:
    print("Acesso negado")
else:
    print("Acesso permitido")
    
    print("\nLogin realizado com sucesso! Insira os dados abaixo:")
    print("-" * 40)
    
    
    salario_base = float(input("Qual é o seu salário base? R$ "))
    recebe_vt = input("Deseja receber vale transporte? (s/n): ").strip().lower()
    valor_vr = float(input("Qual o valor do vale refeição fornecido pela empresa? R$ "))
    quantidade_dependentes = int(input("Qual a quantidade de dependentes? "))
    
    print("-" * 40)
    print("Calculando sua folha de pagamento...\n")
    
   
    desconto_inss = calcular_inss(salario_base)
    desconto_vt = calcular_vt(salario_base, recebe_vt)
    desconto_vr = calcular_vr(valor_vr)
    acrescimo_dep = calcular_dependentes(quantidade_dependentes)
    
   
    salario_liquido = (salario_base - desconto_inss - desconto_vt - desconto_vr) + acrescimo_dep
    
   
    print("=== RESUMO DA FOLHA ===")
    print(f"Matrícula: {matricula}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"(-) INSS: R$ {desconto_inss:.2f}")
    print(f"(-) Vale Transporte: R$ {desconto_vt:.2f}")
    print(f"(-) Vale Refeição: R$ {desconto_vr:.2f}")
    print(f"(+) Dependentes: R$ {acrescimo_dep:.2f}")
    print("-" * 40)
    print(f"SALÁRIO LÍQUIDO A RECEBER: R$ {salario_liquido:.2f}")
    print("=======================")




