import os 
os.system ("cls")


numeros = []


for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)


quantidade_negativos = 0
soma_positivos = 0

for num in numeros:
    if num < 0:
        quantidade_negativos += 1
    elif num > 0:
        soma_positivos += num


print("Quantidade de números negativos:", quantidade_negativos)
print("Soma dos números positivos:", soma_positivos)