import os 
from dataclasses import dataclass

os.system("cls")


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

@dataclass
class Funcionario:
    nome: str
    matricula: int
    email: str
    setor: str

cliente1 = Cliente('Jucelina', 'Jucelina@gmail.com', '40028922')
funcionario1 = Funcionario('Rogerio','40350','Rogerio@gmail.com','Analista de sistemas')
print(f"Nome do cliente: {cliente1.nome}")
print(f"E-mail: {cliente1.email}")
print(f"Telefone: {cliente1.telefone}\n\n")
print("-"*40)
print(f"Nome do funcionario: {funcionario1.nome} \nMatricula: {funcionario1.matricula} \nEmail: {funcionario1.email} \nSetor: {funcionario1.setor}")