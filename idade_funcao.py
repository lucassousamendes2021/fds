import os
os.system("cls")
from datetime import datetime 

os.system("cls")
print("======  ======")
print("    SENAI    ")
print("======  ======")


meses_do_ano = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
    "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
    "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
}


mes_texto = input("Digite o mês que você nasceu: ").lower()
ano_nascimento = int(input("Digite seu ano de nascimento: "))


if mes_texto in meses_do_ano:
    
    
    mes_nascimento = meses_do_ano[mes_texto] 
    

    data_hoje = datetime.now()
    ano_atual = data_hoje.year
    mes_atual = data_hoje.month
    
    
    idade = ano_atual - ano_nascimento
    
    
    if mes_atual < mes_nascimento:
        idade = idade - 1 
        
    os.system("cls")
    print("======  ======")
    print("    SENAI    ")
    print("======  ======")
    print(f"Sua idade exata hoje é: {idade} anos.")

else:
    print("\nMês inválido! Verifique se você digitou corretamente.")