import os
os.system ("cls")


#ENTRADA
print("- Solicitando dados")
idade = int(input("informe sua idade: "))


#PROCESSAMENTO
 
if idade >= 65:
    print("Não são obrigados a votar")

elif idade >= 16:
    print("Acesso ao voto opcional. ")

elif idade >= 18:
    print("Voto obrigatorio. ")

else:
    print("Não podem votar. ")


    
    
