# -*- coding: utf-8 -*-

import time

time.sleep(1)
print("="*30)
print("Escreva um número  e eu irei te dar o triplo do determinado número: ")
print("Digite '-999' para poder sair do programa")

print("="*30)
print("")

while True:
    time.sleep(1)
    valor = int(input("Digite um número: "))
    valor3 = valor * 3

    if valor == -999:
        print("Saindo...")
        break
    else:
        print(f"O valor do número {valor}, múltiplicado pelo número três, é equivalente à {valor3}")

    

    
       
    
    
