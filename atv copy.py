import os 
os.system("cls")

def somar(n1, n2):
    soma = n1 + n2
    return soma 


# EXEMPLO DE USO DA FUNÇÃO
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
# chamando a funçao
# enviando parametros
resultado = somar (n1, n2) 

print(f"soma: {resultado}")