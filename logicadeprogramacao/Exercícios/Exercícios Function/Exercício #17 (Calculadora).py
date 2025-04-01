def subtrair():
    print(x - y)

def soma():
    print(x + y)

def multiplicar():
    print(x * y)

def dividir():
    print(x / y)

x = float(input("Digite um número: "))
y = float(input("Digite um outro número: "))
soma = input("Escolha entre +, -, *, /: ")

if soma == "+":
    soma()
elif soma == "-":
    subtrair()
elif soma == "*":
    multiplicar()
elif soma == "/":
    dividir()
