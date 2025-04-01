def valor():
    if nota < 3:
        print("O seu conceito é o 'Conceito E'")
    elif nota >= 3 and nota <= 5:
        print("O seu conceito e o 'Conceito D'")
    elif nota >= 6 and nota <= 7:
        print("O seu conceito e o 'Conceito C'")
    elif nota >= 8 and nota <= 9:
        print("O seu conceito e o 'Conceito B'")
    elif nota == 10:
        print("O seu conceito e o 'Conceito A'")

nota = int(input("Digite sua idade: "))
valor()
