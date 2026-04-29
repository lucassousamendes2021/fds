import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

    def mostrar_dados(self):
        ("\n\n=== Exibindo dados do cliente ===")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Número de telefone: {self.telefone}")

print("=== Solicitando dados do cliente ===")
cliente = Cliente(
    nome= input("Digite seu nome: "),
    email = input("Digite seu email:"),
    telefone= input("Digite seu número de telefone: ")
)
print("\n=Exibindo dados do cliente")
cliente.mostrar_dados()