import os 
os.system("cls")
from dataclasses import dataclass


@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preço: float


def mostrar_dados(self):
        print(f"Informe o seu nome:{self.nome} ")
        print(f"informe o nome do autor: {self.autor}")
        print(f"Iforme a categoria do livro: {self.categoria}")
        print(f"preço: {self.preço}")


QUANTIDADE_LIVROS=3
lista_livros = []

print("---SISTEMA DE CADASTRO---")
print("1 - adicionar livro")
print("2 - listar livros")
print("3 - Sair")
match int(input("Digite a opção desejada: ")):
    case 1:
        print("Opção 1 selecionada: Adicionar livro")
    case 2:
        print("Opção 2 selecionada: Listar livros")
    case 3:
        print("Opção 3 selecionada: Sair")


print("\n==SOLICITANDO DADOS==")
for i in range(QUANTIDADE_LIVROS):
     novo_livro= Livros(
     nome= input(f"Digite o nome do seu {i+1} livro: "),
     autor= input(f"Digite o nome do autor do seu {i+1} livro: "),
     categoria= input(f"Digite a categoria do seu{i+1} livro: "),
     preço= float(input(f"Digite o preço do seu {i+1} livro: "))
     )

with open("catalogo_livros.csv", "r") as arquivo:
    for linha in arquivo:
        nome, autor, categoria, preço = linha.strip().split(",")
        lista_livros.append(Livros(
        nome=nome,
        autor=autor,
        categoria=categoria,
        preço=preço
        ))

