import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

print("=== Solicitando dados do cliente ===")
cliente = Cliente(
    nome= input("Digite seu nome: "),
    email = input("Digite seu email:"),
    telefone= input("Digite seu número de telefone: ")
)
os.system("cls")
print("\n\n=== Solicitando dados do cliente ===")
print(f"Nome: {cliente.nome}")
print(f"Email: {cliente.email}")
print(f"Número de telefone: {cliente.telefone}")