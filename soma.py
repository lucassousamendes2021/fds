import os
os.system("cls")


soma = 0

for i in range(5):
     numero=int(input(f"{i}-Digite um numero: "))
     soma += numero

print(f"soma: {soma}")
