import os
os.system("cls")

def logo_empresa():
    print("===="*30)
    print("FOLHA DE PAGAMENTOS".center(120))
    print("===="*30)

matricula = int(input("Digite a matricula para acessar seus dados: "))
senha = int(input("Digite a senha para acessar seus dados: "))

if matricula == 123456 and senha == 789:
    print("Acesso permitido")
else:    
    print("Acesso negado")

salario_base = float(input("Digite o seu salario base: "))
desconto_vt = input("Deseja receber o vale transporte? s/n: ").upper()
match desconto_vt:
    case "s":
        print(f"Sera descontado um valor de {desconto_vt} do seu salario. Seu salario atual é de 1426.92.")
    case "n":
        print("Vale transporte não adicionado ao seu salário")


desconto_vr = int(input("Digite o vale refeiçao fornecido pela empresa: "))
print(f"Sera descontado um valor de R${desconto_vr} do seu salario. Seu salario atual é de 926.92")

dependentes = int(input("Digite o número de dependentes: "))

print("-" * 40)
print("Calculando sua folha de pagamento...\n")

desconto_inss = salario_base * 0.09
desconto_vt = 0.0
if desconto_vt == "s":
    desconto_vt = salario_base * 0.06

desconto_vr = desconto_vr * 0.20



salario_liquido = (salario_base - desconto_inss - desconto_vt - desconto_vr) + dependentes

os.system("cls")
def logo_empresa():
    print("===="*30)
    print("FOLHA DE PAGAMENTOS".center(120))
    print("===="*30)

print("=== RESUMO DA FOLHA ===")
print(f"Matrícula do Funcionário: {matricula}")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"(-) Desconto INSS: R$ {desconto_inss:.2f}")
print(f"(-) Desconto Vale Transporte: R$ {desconto_vt:.2f}")
print(f"(-) Desconto Vale Refeição: R$ {desconto_vr:.2f}")
print(f"(+) Acréscimo Dependentes: R$ {dependentes:.2f}")
print("-" * 40)
print(f"SALÁRIO LÍQUIDO A RECEBER: R$ {salario_liquido:.2f}")
print("=======================")

