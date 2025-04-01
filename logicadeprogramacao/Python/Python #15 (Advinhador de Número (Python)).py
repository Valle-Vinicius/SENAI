print("Pense em um número entre 1 e 100, e eu tentarei adivinhar!")
input("Quando estiver pronto, pressione qualquer tecla + Enter")

baixo = 1
alto = 100
tentativas = 0

while True:
    tentativas += 1
    palpite = (baixo + alto) // 2
    resposta = input(f"Meu palpite é {palpite}. O número é maior, menor ou igual ao seu número? (maior/menor/igual): ").lower()
    
    if resposta == "igual":
        print(f"O número era {palpite}. Foram necessárias {tentativas} tentativas.")
        break

    elif resposta == "maior":
        baixo = palpite + 1
    elif resposta == "menor":
        alto = palpite - 1
