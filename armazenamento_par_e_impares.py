import os
os.system("cls")

numeros = []
numero = []

for i in range(6):
    
    numero_digitado = float(input(f"Digite o {i+1}º numero: "))
    numeros.append(numero_digitado)
    
    numeros_pares = numeros 
    numeros_impares = numeros 
    
for numero in numeros: 
   if numeros > numeros_impares:
            numeros_impares = numeros
   if numeros < numeros_pares:
            numeros_pares = numeros
            
            
print("\n---RESULTADOS---")
print(f"Numeros informados: {numeros}")
print(f"numeros pares: {numeros_pares}")
print(f"numeros impares: {numeros_impares}")
