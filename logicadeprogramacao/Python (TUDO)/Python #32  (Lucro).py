produto = float(input("Digite o valor do produto"))

if produto < 20:
    lucro = produto*0.35
    produtolucro = produto + lucro
    print(f"Você precisa vender o produto por {produtolucro}")

elif produto > 20:
    lucro = produto*0.45
    produtolucro = produto + lucro
    print(f"Você precisa vender o produto por {produtolucro} para ter um lucro")
