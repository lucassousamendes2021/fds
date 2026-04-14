import os 
os.system("cls")

def calcular_imc(peso, altura):
    return peso / altura ** 2 

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")


match imc:
    case imc if imc <18.5:
        print("Você está abaixo do peso.")
    case imc if 18.5 <= imc < 25:
        print("Você está com o peso normal.")
    case imc if 25 <= imc < 30:
        print("Você está com sobrepeso.")
    case imc if 30 <= imc < 35:
        print("Você está com obesidade grau 1.")
    case imc if 35 <= imc < 40:
        print("Você está com obesidade grau 2.")
    case imc if imc >= 40:
        print("Você está com obesidade grau 3.")
    

