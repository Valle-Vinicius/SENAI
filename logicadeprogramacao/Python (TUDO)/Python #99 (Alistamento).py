def valor():

    if idade < 16:
        print("Você não pode votar (Não-Eleitor)")


    elif idade >= 16 and idade <= 18:
        print("Você pode votar por livre espontânea vontade (Eleitor Facultativo)")

    elif idade > 18 and idade <= 65:
        print("Você tem que votar (Eleitor Obrigatório)")


idade = int(input("Digite a sua idade"))
valor()
              
