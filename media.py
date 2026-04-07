import os
os.system ("cls")

def calcular_media(n1, n2):
    media = (n1 + n2) / 2 
    return media
def verificar_resultados(media):
    if media >= 7:
        resultado = "aprovado"
    else:
        resultado = "reprovado"
    return resultado
print("= Solicitando dados =")
n1= int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = calcular_media(n1, n2)
resultado = verificar_resultados(media)

print("\n= Exibindo resultados = ")
print(f"Media: {media}")
print(f"Resultado: {resultado}")