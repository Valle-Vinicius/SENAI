peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
altura2 = altura * altura

imc = peso/altura2

if imc < 20:
    print("Você está abaixo do peso")

elif imc >= 20 and imc < 25:
    print("Você está no peso normal")

elif imc >= 25 and imc < 30:
    print("Você está sobrepeso")

elif imc >= 30 and imc < 40:
    print("Você está obeso")

elif imc >= 40:
    print("Você está obeso mórbido")
