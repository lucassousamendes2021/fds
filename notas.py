import os 
os.system ("cls")


soma = 0
quantidade_notas = 2

for i in range(quantidade_notas):
    nota = float(input("Digite uma nota: "))
    soma  += nota

    media = soma / quantidade_notas

    print(f"Media: {media}")