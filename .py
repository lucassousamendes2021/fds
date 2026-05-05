import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome:str
    idade: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}\n")

QUANTIDADE_FUNCIONARIOS = 2
lista_funcionarios = []


print("=Solicitando dados=")
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: "))
    )
    print('')
    lista_funcionarios.append(novo_funcionario)



    print("= Exibindo dados =")
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()

    print("= Salvando dados = ")
    with open("Lista_funcionarios.csv", "a") as arquivo:
        for funcionario in lista_funcionarios:
            arquivo.write(f"{funcionario.nome}, {funcionario.idade}\n")
        print("Salvo com sucesso!!")

print("= Fim do programa =")