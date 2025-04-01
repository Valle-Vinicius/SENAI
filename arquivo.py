gabarito = ["A", "C", "E", "D", "B", "E", "C"]
contador = 1
gabaritoaluno = []
contadoracertos = 0

for i in range(7):  
    valor = input(f"Digite a resposta da questão {contador}: ")
    contador += 1
    gabaritoaluno.append(valor)

for i in range(7):  
    if gabaritoaluno[i] == gabarito[i]:
        contadoracertos += 1

print(f"Ao todo você teve {contadoracertos} acertos.")

print("Agora eu estou na Branch Raiz 1! E não no arquivo original!")
