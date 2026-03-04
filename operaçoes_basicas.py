import os 

os.system ("cls")


numero1 = int(input("Digite o primeiro numero: "))
operador = input("Digite a operação desejada (+ - * /): ")
numero2 = int(input("Digite o segundo numero: "))


match operador:
    case "+":
        rsultado = numero1 + numero2 
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        resultado = numero1 / numero2
    case _:
        print("Opção invalida")
        
        
        resultado = 0
        
        print(f"Resultado: {resultado}")