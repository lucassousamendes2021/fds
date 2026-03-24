import os 
os.system("cls")

soma = 0 
quantidade = 0
 
print ("--- calculadora de media---")
print("Insira os valores  inteiros positivos.(Digite um numero negativo para encerrar)")


while True:
    valor = int(input("Digite um valor:"))
    
    if valor > 0:
        
        
        soma += valor
        quantidade += 1
    
    if quantidade < 0:
        media = soma / quantidade 
        print(f"\nA media aritmetica dos numeros informados é {media}")
    else:
        print("\nNemhum valor positivo foi inserido para calcular a media.")
        