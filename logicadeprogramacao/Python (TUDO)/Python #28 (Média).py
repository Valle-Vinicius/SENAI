nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))
media = nota1 + nota2 / 2

if media >= 7:
    print("Aprovado")

elif media <3:
    print("Reprovado")

else:
    print("Recuperação")
