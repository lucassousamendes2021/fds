import os
os.system("cls")


soma = 0
quantidade_notas = 3

for i in range(quantidade_notas):
    nota = float(input("Digite uma nota: "))
    soma += nota

    media = soma / quantidade_notas

    if media >= 7:
       resultado = "aprovado"
    elif media <= 4:
        resultado = "reprovado"
    else:
        resultado = "recuperaçao"

    print(f"Media: {media}")
    print(f"Resultado: {resultado}") 