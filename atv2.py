import os
os.system("cls")



print("= Solicitanto dados = ")
numero = int(input("Digite o valor que queira converter em metros:"))

def metros(a):
    centimetros = a * 100
    print(f"Valor em centimetros é: {centimetros}")

print("\nresultado")
metros(numero)


