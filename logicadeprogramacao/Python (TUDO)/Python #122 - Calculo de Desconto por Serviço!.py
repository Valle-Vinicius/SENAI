tempo = int(input("Digite quantos anos você vem trabalhando dentro da empresa: "))
produto = float(input("Digite o preço do produto: "))

if tempo >= 5 and tempo <= 10:
    descontoproduto = produto*0.05
    produto -= descontoproduto
    print(f"Por você ser um cliente de aproximadamente {tempo} anos, você vai ganhar um desconto de 5%, totalizando o valor de R$ {produto}")

elif tempo > 10:
    descontoproduto = produto*0.10
    produto -= descontoproduto
    print(f"Por você ser um cliente de aproximadamente {tempo} anos, você vai ganhar um desconto de 10%, totalizando o valor de R$ {produto}")

elif tempo < 5 and tempo > 0:
    print("Você ainda não consegue receber um desconto!")

else:
    print("Erro!")
