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
        print(f"Iforme o seu telefone: {self.telefone}")



dados_empresa = []
print("= Solicitando dados =")
nova_empresa = Empresa(
    nome=input("\nInforme o nome da sua empresa: "),
    cnpj=input("\nInforme o cnpj da empresa: "),
    telefone=int(input("\nInforme seu telefone: "))
)

dados_empresa.append(nova_empresa)
print("\n= Exibindo dados =")


for empresa in dados_empresa:
    empresa.mostrar_dados()

print("\n= Salvando dados =")
with open("dados_empresa.csv", "a", encoding="utf-8") as arquivo:
    for empresa in dados_empresa:
        arquivo.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}")
    print("Salvo com sucesso!!")
