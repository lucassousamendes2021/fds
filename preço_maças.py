import os 

os.system ("cls")

quantidade = int(input("Quantas maçãs voçe quer comprar?: "))

if quantidade < 12:
    preço = 1.30
else:
    preço = 1.00
    
    valor = quantidade * preço
    
    print("A quantidade foi {} maçãs, o preço por unidade foi: R${:.2f}".format(quantidade, preço))
    print(f"O valor total da compra é: R${valor: .2f}")
    