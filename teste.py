def babu():
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um número: "))
  num3 = int(input("Digite um número: "))
  media = (num1 + num2 + num3 )/3

  if media >=7:
    print(f"A média dos números totais é {media}, O que significa que você passou na matéria!")
  elif media > 0 and media <7:
    print(f"A média dos números totais é {media}, O que significa que você não passou na matéria!")
  elif media < 0 or media > 10:
    print("Erro! Você deve ter digitado algum número errado!")
  else:
    print("Erro! Você digitou alguma coisa errada")

babu()