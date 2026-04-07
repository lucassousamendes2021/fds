import os 
os.system("cls")

def tabuada(numero):
 for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")

# EXEMPLO DE USO DA FUNÇÃO
numero = int(input("Digite um numero para a tabuada: "))
# chamando a funçao
# enviando parametros
tabuada(numero)