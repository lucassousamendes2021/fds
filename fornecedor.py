import os 
from dataclasses import dataclass
os.system("cls")


@dataclass
class Fornecedor:
    nome:str
    email: str
    telefone: int
    endereço: int

print("\n=Solicitando dados do fornecedor=")
fornecedor = Fornecedor(
    nome = input("Digite seu nome: "),
    email = input("Digite seu email: "),
    telefone = input("Digite o seu número de telefone: "),
    endereço = input("Digite seu endereço: ")

)
os.system("cls")
print("\n\n=== Solicitando dados do cliente ===")
print(f"Nome: {fornecedor.nome}")
print(f"Idade: {fornecedor.email}")
print(f"Peso: {fornecedor.telefone}")
print(f"Altura: {fornecedor.endereço}")