numero1 = int(input("escolhe um número aí faz a boa"))
numero2 = int(input("escolhe um número aí faz a boa"))
numero3 = int(input("escolhe um número aí faz a boa"))

if numero1 > numero2 and numero3:
    print("o número maior é o", numero1)
else:
    if numero2 > numero1 and numero3:
        print("o maior número é o", numero2)
    else:
        if numero3 > numero2 and numero1:
            print("o maior número é o", numero3)

