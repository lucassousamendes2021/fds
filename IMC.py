import os
os.system ("cls")

altura = float(input("Informe sua altura para o calculo do IMC: "))
peso = float(input("informe seu peso: "))


imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")


if imc <= 18.5:
    print ("abaixo do peso")
elif imc >= 18.5 or 24.9:
    print("Peso ideal")
elif imc >= 25.0 or 29.9:
    print("levemente acima do peso")
elif imc >= 30.0 or 34.9:
    print("Obesidade grau 1")
elif imc >= 35.0 or 39.9:
    print("Obesidade grau 2")
else:
    print("ce ta fudido pae")
    