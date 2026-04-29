import os 
from dataclasses import dataclass

os.system("cls")


@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int


pessoa1 = Pessoa('Lucas', 17)
pessoa2 = Pessoa('Renner', 18)
pet1 = Pet('Rodolfo', 4)
pet2 = Pet('Duke', 5)
print("""
 == PET SHOP DEUS É MAIS FORTE ==""")
print(f"\nNome: {pessoa1.nome} \nIdade: {pessoa1.idade}")
print(f"Nome do pet: {pet1.nome} \nIdade: {pet1.idade}")
print("-"*40)
print(f"Nome: {pessoa2.nome} \nIdade: {pessoa2.idade}")
print(f"Nome do pet: {pet2.nome} \nIdade do pet: {pet2.idade}\n")