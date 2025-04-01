pergunta = int(input("Qual a velocidade atual do carro?: "))

if pergunta > 80:
    ValorMulta = (pergunta-80) * 5
    KMAcima = pergunta-80

    print(f"Você passou {KMAcima} Kilomêtros acima da velocidade, totalizando uma multa de R${ValorMulta}")

elif pergunta < 80:
    print(f"Você estava numa velocidade de {pergunta} KM/H, o que é permitido nessa via! Parabéns")

else:
    print("Erro!")
    
    
