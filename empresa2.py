import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: int

    
    def mostrar_dados(self):
        print(f"Informe o seu nome:{self.nome} ")
        print(f"informe o cnpj da empresa: {self.cnpj}")
        print(f"Iforme o seu telefone: {self.telefone}\n")

lista_empresas = []

with open("dados_empresa.csv", "r") as arquivo:
    for linha in arquivo:
        nome, cnpj, telefone = linha.strip().split(",")
        lista_empresas.append(Empresa(
        nome=nome,
        cnpj=cnpj,
        telefone=telefone
        ))

for empresa in lista_empresas:
    empresa.mostrar_dados()