import os

os.system ("cls")

print("Solicitando dados -")
ano_nascimento = int(input("Digite sua idade: "))
sexo = (input("Digite seu sexo: ")).lower()

idade = 2026 - ano_nascimento

idade_obrigatorio = idade >= 18
sexo_obrigatorio = sexo == "masculino"

if idade_obrigatorio and sexo_obrigatorio:
    print("Deve apresentar-se ao serviço militar obrigatorio")
else:
    print("Não é nescessario apresentar-se ao serviço militar obrigatorio")
    
