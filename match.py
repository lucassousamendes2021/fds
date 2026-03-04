import os

os.system ("cls")


dia = input("Digite o dia da semana: ")

match dia:
    case "segunda":
        print("Hoje é segunda-feira. ")
    case "terça":
        print("Hoje é terça-feira. ")
    case "quarta":
        print("Hoje é quarta-feira. ")    
    case "quinta":
        print("Hoje é quina-feira. ")
    case "sexta":
        print("Hoje é sexta-feira. ")
    case "sabado":
        print("Hoje é sábado. ")
    case _:
        print("Dia inválido")
        
        print (dia)