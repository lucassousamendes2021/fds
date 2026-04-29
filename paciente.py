import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade:int
    peso:int
    altura: float
print("=== Solicitando dados do paciente ===")
paciente = Paciente(
    nome= input("Digite seu nome: "),
    idade = input("Digite sua idade: "),
    peso= input("Digite seu peso atual: "),
    altura = input("Digite sua altura atual: "),
)
os.system("cls")
print("\n\n=== Solicitando dados do cliente ===")
print(f"Nome: {paciente.nome}")
print(f"Idade: {paciente.idade}")
print(f"Peso: {paciente.peso}")
print(f"Altura: {paciente.altura}")