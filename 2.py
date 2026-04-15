import os
os.system("cls || clear")

def analisar_sequencia(quantidade_numeros):
    
    soma_pares = 0
    soma_impares = 0
    soma_geral = 0
    quantidade_pares = 0
    quantidade_impares = 0
    quantidade_positivos = 0
    quantidade_negativos = 0

    maior_numero = float('-inf')
    menor_numero = float('inf')

    print("\n--- Análise de Números ---")

    for i in range(1, quantidade_numeros + 1):
        numero = int(input(f"Digite o {i}º número: "))
        
       
        if numero % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero
        else:
            quantidade_impares += 1
            soma_impares += numero

      
        if numero > 0:
            quantidade_positivos += 1
        elif numero < 0:
            quantidade_negativos += 1
            
       
        maior_numero = max(maior_numero, numero)
        menor_numero = min(menor_numero, numero)
        soma_geral += numero

    
    print("\n--- Estatísticas dos números ---")
    print(f"Quantidade de pares: {quantidade_pares} (Soma total: {soma_pares})")
    print(f"Quantidade de ímpares: {quantidade_impares} (Soma total: {soma_impares})")
    print(f"Quantidade de positivos: {quantidade_positivos}")
    print(f"Quantidade de negativos: {quantidade_negativos}")
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")
    print(f"Soma geral de todos os números: {soma_geral}")

def main():
    
    while True:
        os.system("cls || clear") 
       
        analisar_sequencia(5)
        
        
        print("\n" + "-"*30)
        continuar = input("Deseja analisar outra sequência de números? (S/N): ").strip().upper()
        
        if continuar != 'S':
            print("Encerrando o programa... Até logo!")
            break


if __name__ == "__main__":
    main()