#Faça um programa com uma função que receba o
# raio (R) de um círculo e retorne a sua área (A = PI * R2).

def area():
    return raio**2 * 3.14

raio = float(input("Digite o valor do raio"))

resultado = area()

print(f"O valor da área é equivalente à {resultado}")
