import os 
os.system ("cls")


total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = float('inf')

while True:
    
    print("\n--- MENU ---")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    
    opcao = input("Escolha uma opção (1 ou 2): ")
    
    if opcao == '1':
        
        salario = float(input("Digite o salário da família: R$ "))
        filhos = int(input("Digite o número de filhos: "))
        
      
        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos
        
      
        if salario > maior_salario:
            maior_salario = salario
            
      
        if salario < menor_salario'     :
            menor_salario = salario
            
        print("Família adicionada com sucesso!")

    elif opcao == '2':
        
        if total_familias > 0:
            
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias
            
            
            print("\n=== RESULTADOS DA PESQUISA ===")
            print(f"a) Total de famílias que responderam: {total_familias}")
            print(f"b) Média do salário da população: R$ {media_salario:.2f}")
            print(f"c) Média do número de filhos: {media_filhos:.1f}")
            print(f"d) Maior salário: R$ {maior_salario:.2f}")
            print(f"e) Menor salário: R$ {menor_salario:.2f}")
        else:
            print("\nNenhuma família foi registrada na pesquisa.")
            break
        
    else:
        print("\nOpção inválida! Por favor, digite 1 ou 2.")

