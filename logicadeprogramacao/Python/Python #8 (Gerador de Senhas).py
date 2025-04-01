import random
import string


while True:
    pergunta = int(input("Quantas senhas você quer gerar?"))

    for i in range(pergunta):
        senha = string.ascii_letters + string.hexdigits
        senhagerada = ''.join(random.choices(senha, k = 100))
        print(senhagerada)
