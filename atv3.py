import os 
os.system("cls")


def calcular_inflacao(preco):
    if preco < 100:
        preco_inflacionado = preco * 1.10
    else:
        preco_inflacionado = preco * 1.20
        return preco_inflacionado

preco_produto = float(input("Digite o preço do produto: R$ "))
novo_preco = calcular_inflacao(preco_produto)    
print(f"O preço inflacionado do produto é: R$ {novo_preco:.2f} ")