import os 
os.system ("cls")


soma = 0
media = 0
vetor_notas = []
QUANTIDADE_NOTAS = 4

print(f"Adicionando {QUANTIDADE_NOTAS} notas.")

for i in range (QUANTIDADE_NOTAS):
   nota  = float(input(f"Digite a {i+1}ª nota: "))
   soma += nota
   vetor_notas.append(nota)
   
   media = sum(vetor_notas) / QUANTIDADE_NOTAS 

  
print("\nExibindo as notas informadas. ")  
print(f"media: {nota}")

if media > 5: 
    print("Reprovado.")
elif media <= 5:
    print("Recuperaçao.")
else:
    print("Aprovado!")
    

