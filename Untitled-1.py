import os

os.system ("cls")

matiricula = input ("Digite sua matricula: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
tempo_de_trabalho = int(input("Digite o tempo de trabalho em anos: "))

idade = 2026 

if idade >= 65 or tempo_de_trabalho >= 30:
   resultado = print("requerer aposentadoria")
   
else:
    print("Não requerer aposentadoria")
   
print("\n- Resultado -")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo_de_trabalho}")

