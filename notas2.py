import os 
# limpa o terminal
os.system ("cls")

# solicitanto dados
while True: 
        nota1= float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        # calculo
        soma= nota1 + nota2 + nota3 /3
        
        # saida de dados
        
        if nota1 <0 and nota2 <0 and nota3 <0:
            print ("nota invalida.")
            print("tente novamente...")
            
        elif nota1 <7 and nota2 <7 and nota3 <7:
            print("Reprovado.")
            print(f"Suas notas foram: {nota1}, {nota2} e {nota3}")
            print(f"Media parcial: {soma}")
            break
        elif nota1 <5 and nota2 <5 and nota3 <5:
            print("recuperaçao")
            print(f"Media parcial: {soma}")
            break
        else:
            print(f"APROVADO!")
            print(f"Passou com: {nota1}, {nota2} e {nota3} ")
            print(f"Nota parcial (media): {soma}")
            break
        