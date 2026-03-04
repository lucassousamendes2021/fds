import os

os.system ("cls")


print("MENU")

print ("""
       
   =========MENU==========

codigo      prato            valor
  1        macarrão          25,00
  2        lasanha           30,00
  3        strogonoff        20,00
  
  """)
 
prato = int(input("Escolha o prato desejado atraves do codigo: "))

match prato:
     case 1:
        print("voçê escolheu macarrão. ")
        print("Valor: 25,00 ")
     case 2:
        print("Voçê escolheu lasanha. ")
        print("Valor: 30,00 ")
     case 3:
        print("Voçê escolheu strogonoff. ")
        print("Valor: 20,00 ")
        

