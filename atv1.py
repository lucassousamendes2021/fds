import os 


def logo():
    os.system("cls")
    print("=========")
    print("SENAI")
    print("=========")

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b 

def dividir(a, b):
    return a / b 


logo()
print ("= Solicitando dados=")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))


soma = somar(n1, n2)
subtracao = subtrair(n1, n2)
multiplicacao = multiplicar(n1, n2)
divisao = dividir(n1, n2)


logo()
print("= Exibindo dados = ")
print(f"Soma: {n1} + {n2} = {soma}")
print(f"subtração: {n1} - {n2} = {subtracao}")
print(f"Multiplicação: {n1} x {n2} = {multiplicacao}")
print(f"Divisão: {n1} : {n2} = {divisao}")

