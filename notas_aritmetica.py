import os 
os.system ("cls")
soma = 0
vetor_notas = []
QUANTIDADE_NOTAS = 3

print(f"Adicionando {QUANTIDADE_NOTAS} notas.")
for i in range (QUANTIDADE_NOTAS):
   nota  = float(input(f"Digite a {i+1}ª nota: "))
   vetor_notas.append(nota)
   soma += nota
   
   media = soma / QUANTIDADE_NOTAS 
  
print ("\nExibindo as notas informadas. ")  
  
for uma_nota in vetor_notas:
    print (f"nota: {uma_nota}")
    
    print(f"Media: {media}")