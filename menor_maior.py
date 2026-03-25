import os
os.system("cls")

numeros = []
numero = []

for i in range(5):
    
    numero_digitado = float(input(f"Digite o {i+1}º numero: "))
    numeros.append(numero_digitado)
    
    maior_numero = numeros [0]
    menor_numero = numeros [0]
for numero in numeros: 
   if numero > maior_numero:
            maior_numero = numero
   if numero < menor_numero:
            menor_numero = numero
            
            
print("\n---RESULTADOS---")
print(f"Numeros informados: {numeros}")
print(f"O maior numero é: {maior_numero}")
print(f"O menor numero é: {menor_numero}")