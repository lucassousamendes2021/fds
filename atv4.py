import os 
os.system ("cls")

def calcular_media(vetor_notas):
    soma = 0
    quantidade = 0

    for nota in vetor_notas:
        soma += nota
        quantidade += 1
        return soma / quantidade
    nota = []
    
    for i in range(3):
        nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
        nota.append(nota)

        media_final = calcular_media(nota)
        print("\n---- RESULTADOS----")
        print(f"notas registradas: {nota}") 
        print(f"Media do aluno é: {media_final:.2f}")


