import os 
import time
os.system ("cls")
numero = int(input("digite um numero: "))


for i in range(1, 11, 1):
       tabuada=numero * i
       print("       ")
       time.sleep(1)
       print(f"{numero} X {i} = {tabuada}")

