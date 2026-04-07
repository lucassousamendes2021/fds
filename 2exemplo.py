import os
os.system("cls")

# funçao com parametros
def saudacao(nome):
    print(f"Ola, {nome}!")
    print("Bem vindo(a) ao nosso site")

# exemplo de uso da funçao
nome_visitante = input("Digite seu nome: ")
saudacao(nome_visitante)   
