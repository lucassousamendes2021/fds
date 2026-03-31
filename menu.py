import os 
os.system ("cls")

cardapio = [

("pizza", 25.00),
("lasanha", 20.00),
("strogonof", 18.00),
("bife acebolado", 15.00),
("pao com ovo", 5.00),

]

pedidos = []
total = 0

while True:
    print("\nCardapio")
    for i, item  in enumerate (cardapio):
        print(f"{i+1}º - {item[0]} R$ {item[1]:.2f}")
    escolha = input("Escolha o numero do prato desejado: ")

    if escolha.isdigit():
        escolha_num = int(escolha)
    
    if 1 <= escolha_num <= len(cardapio):
        pedido = cardapio [escolha_num - 1]
        pedidos.append(pedido)
        total += pedido[1]
        break
    else:
        print("Numero invalido. Tente novamente. ")    
        
else:
 print("Por favor, digite um numero")
    

    

continuar = input("Deseja escolher outro prato? (s/n): ").lower()
if continuar != 's':
    
    print("\nVoçe pediu:")
for prato, valor in pedidos:
    print(f"- {prato}: R$ {valor:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
