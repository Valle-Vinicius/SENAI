import random

numero = random.randint(1, 100)
tentativas = 0 

while True:
    pergunta = int(input("Advinhe o número entre 1 - 100! Digite um valor: "))
    tentativas += 1 
    
    if pergunta > numero:
        print("📈 Número alto demais, tente um menor! 🔽")
    elif pergunta < numero:
        print("📉 Número baixo demais, tente um maior! 🔼")
    else:
        print(f"🎉 Você ganhou! 🏆 Tentativas: {tentativas} 🚀")
