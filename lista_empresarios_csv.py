import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    idade: int

    
    def mostrar_dados(self):
        print(f"Informe o seu nome:{self.nome} ")
        print(f"informe sua idade: {self.idade}")
        

lista_funcionarios = []

with open("lista_funcionarios.csv", "r") as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(",")
        lista_funcionarios.append(Funcionario(
        nome=nome,
        idade=idade
    ))

for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()