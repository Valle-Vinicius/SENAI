import random

# Lista de países reconhecidos pela ONU em minúsculas e sem acento
palavras = [
    "afeganistao", "africa do sul", "albania", "alemanha", "andorra", "angola", "antigua e barbuda", "arabia saudita",
    "argelia", "argentina", "armenia", "australia", "austria", "azerbaijao", "bahamas", "bangladesh", "barbados",
    "barein", "belgica", "belize", "benin", "birmânia", "bielorrussia", "bolivia", "bosnia e herzegovina", "botsuana",
    "brasil", "brunei", "bulgaria", "burkina faso", "burundi", "butao", "cabo verde", "camarões", "camboja",
    "canada", "catar", "colombia", "comores", "congo", "coreia do norte", "coreia do sul", "costa do marfim", "costa rica",
    "croacia", "cuba", "dinamarca", "djibouti", "dominica", "egito", "el salvador", "emirados arabes unidos", "equador",
    "eritrea", "eslovacia", "eslovenia", "espanha", "estados unidos", "estonia", "eswatini", "etopia", "fiji", "filipinas",
    "finlandia", "franca", "gabao", "gambia", "ganja", "georgia", "ghana", "grecia", "grenada", "guatemala", "guinea",
    "guine-bissau", "guyana", "haiti", "honduras", "hungria", "islandia", "india", "indonesia", "irlanda", "italia",
    "jamaica", "japao", "jordania", "kosovo", "kuwait", "laos", "lesoto", "letonia", "libano", "liberia",
    "lituania", "luxemburgo", "madagascar", "malawi", "malasia", "maldivas", "mali", "malta", "marrocos", "mauricio",
    "mauritania", "mexico", "micronesia", "moçambique", "moldavia", "monaco", "mongolia", "montenegro", "namibia",
    "nauru", "nepal", "nicaragua", "niger", "nigeria", "niue", "noruega", "nova zelandia", "oma", "paises baixos",
    "palestina", "panama", "papua nova guinea", "paquistao", "paraguai", "peru", "polonia", "portugal", "quenia",
    "república centro-africana", "república dominicana", "república tcheca", "romenia", "ruanda", "russia", "samoa",
    "san marino", "sao tome e principe", "seicheles", "senegal", "serbia", "singapura", "siria", "somalia", "sri lanka",
    "suazilandia", "suecia", "suica", "suriquá", "tailandia", "tanzania", "togo", "tonga", "trinidad e tobago", "tunisia",
    "turcomenistao", "turquia", "tuvalu", "uganda", "uruguai", "uzbequistao", "vanuatu", "venezuela", "vietna", "zambia",
    "zimbabue"
]



palavra = random.choice(palavras)

tentativas = 6
letras_descobertas = ['_'] * len(palavra)
letras_erradas = []

print("Bem-vindo ao Jogo da Forca!")

while tentativas > 0:
    print("Palavra: ", " ".join(letras_descobertas))
    print("Letras erradas: ", " ".join(letras_erradas))
    print("Tentativas restantes: ", tentativas)

    letra = input("Digite uma letra: ").lower()

    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
        print("Boa! Você acertou uma letra!")
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print("Errou! Tentativas restantes:", tentativas)

    if "_" not in letras_descobertas:
        print("Parabéns! Você venceu! A palavra era:", palavra)
        break

if tentativas == 0:
    print("Você perdeu! A palavra era:", palavra)
