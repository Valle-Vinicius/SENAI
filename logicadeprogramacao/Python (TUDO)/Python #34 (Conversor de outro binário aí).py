numero = int(input("Digite um número: "))

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0

if numero >= 128:
    n1 = 1
    numero -= 128

if numero >= 64:
    n2 = 1
    numero -= 64

if numero >= 32:
    n3 = 1
    numero -= 32

if numero >= 16:
    n4 = 1
    numero -= 16

if numero >= 8:
    n5 = 1
    numero -= 8

if numero >= 4:
    n6 = 1
    numero -= 4

if numero >= 2:
    n7 = 1
    numero -= 2

if numero >= 1:
    n8 = 1
    numero -= 1

print(f'O número em binário é: {n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}')
