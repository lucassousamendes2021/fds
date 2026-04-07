import os 
os.system("cls")

def negativo(n1):
    if n1 < 0:
        print(f"o numero escolhido é negativo ({numero}). ")
    else:
        print(f"O numero escolhido é positivo ({numero}). ")

numero = int(input("Digite um numero: "))
negativo(numero)

