import os 
os.system ("cls")

vetor = []
total = 0
gaveta = 0
print("""
        -------EXAMES DISPONIVEIS-------     
            
              
Código           Exames                    Valor
 1          Hemograma Completo           R$ 150.00
 2               Raio X                  R$ 80.00  
 3          Ultrassonografia             R$ 110.00
 4          Eletrocardiograma            R$ 230.00
 5             Tomografia                R$ 250.00
 6        Ressonância Magnética          R$ 50.00
 7          Exame de Glicose             R$ 15.00
     
      
      """)
exame = int(input("Informe qual exame deseja: "))
vetor.append
 match exame:
    case 1:
        print("Voce escolheu Hemograma Completo e o seu valor é de R$ 150.00")
    
    case 2:
        print('Voce escolheu Raio X e o seu é de R$ 80,00')
      
    case 3:
        print('Voce escolheu Ultrassonografia e o seu valor é de R$ 110.00')
     
    case 4:
        print('Voce escolheu Eletrocardiograma e o seu valor é de R$ 230.00')
       
    case 5:
        print('Voce escolheu Tomografia e o seu valor é de R$ 250.00')
        
    case 6:
        print('Voce escolheu Ressonância Magnética e o seu valor é de R$ 50.00')
     
    case 7:
        print('Voce escolheu Exame de Glicose e o seu valor é de R$ 15.00') 
 
    
        exames = ["Hemograma Completo","raio x", "ultrassonografia", "eletrocardiograma", 'tomografia', 'ressonacia', 'magnetica', 'exame de glicose']
        valores = [150.00, 80.00, 110.00, 230.00, 250.00, 50.00, 15.00]
        
        while True:
            codigo = int(input("Digite o código do exame desejado (1 a 7): "))
    
   
        if 1 <= codigo <= 7:
           gaveta = codigo - 1 
        
     
           nome_escolhido = exames[gaveta]
           valor_escolhido = valores[gaveta]
        
           print(f"Você escolheu {nome_escolhido} e o seu valor é de R$ {valor_escolhido:.2f}")
        
       
           total += valor_escolhido 
        
        else:
            print("Código inválido. Tente outro código.")
        
        
  
       
        print("\nVoce quer agendar outro exame? ")
        resposta = int(input("Digite 1 para SIM e 2 para NÃO: "))
        if resposta == 2:
       
            print("\n===============================")
            print("          CONTA FINAL            ")
            print("\n===============================")  
            print(f"O total a pagar é: {total:.2f}") 
            print("\n===============================")