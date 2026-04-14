import os 
os.system("cls")

nota = 0 
def calcular_nota():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    return (nota1 + nota2) / 2


nota = calcular_nota()
print(f"Sua média é: {nota}")




