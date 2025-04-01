#-*- Coding UTF-8 -*-

# O objetivo dessa programação é o usuário enviar um número. Caso o valor do número seja positivo, ele ache a raiz quadrada e, caso contrário, ele ache a potenciação do determinado número.

import math

num = float(input("Digite um número"))

if num => 0:
    valor1 = math.sqrt(num)
    print(f"O valor da raiz quadrada do número {num} é {valor1}")


elif num < 0:
    valor1 = pow(num, 2)
    print(f"O valor da potenciação do número {num} é {valor1}")
    
else:
    print("Erro!")
