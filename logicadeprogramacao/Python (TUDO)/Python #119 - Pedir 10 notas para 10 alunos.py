media = []
c = 1
c2 = 2
c3 = 3
c4 = 4

for i in range(1, 11):
    nota1 = float(input(f"{c} . Digite a primeira nota!: "))
    nota2 = float(input(f"{c2} . Digite a segunda nota!: "))
    nota3 = float(input(f"{c3} . Digite a terceira nota!: "))
    nota4 = float(input(f"{c4} . Digite a quarta nota!: "))
    
    medias = (nota1 + nota2 + nota3 + nota4) / 4 
    media.append(medias)

print(media)
