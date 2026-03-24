import os 
os.system ("cls")


qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0
qtd_geral = 0

print("Digite números inteiros positivos.")
print("Para encerrar, digite o número 0.")
print("-" * 40)

while True:
    valor = int(input("Digite um número: "))
    
 
    if valor == 0:
        break
        
    
    if valor < 0:
        print("Atenção: O exercício pede apenas números positivos. Tente novamente.")
        continue 
        
    soma_geral += valor
    qtd_geral += 1
    
    
    if valor % 2 == 0:
        qtd_pares += 1
        soma_pares += valor
    
    else:
        qtd_impares += 1

print("\n" + "=" * 40)
print("RESULTADOS:")


print(f"a. Quantidade de números pares: {qtd_pares}")
print(f"   Quantidade de números ímpares: {qtd_impares}")

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"b. Média de valores pares: {media_pares:.2f}")
else:
    print("b. Média de valores pares: Não é possível calcular (nenhum par foi digitado).")

if qtd_geral > 0:
    media_geral = soma_geral / qtd_geral
    print(f"c. Média geral dos números lidos: {media_geral:.2f}")
else:
    print("c. Média geral: Não é possível calcular (nenhum número foi lido).")