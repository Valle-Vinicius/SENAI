media = []
c = 1
c2 = 2
c3 = 3
c4 = 4
cont = 1
cont2 = 1

print("")
print("Este programa irá calcular a média de notas de 10 alunos.")
print("Para cada aluno, você vai digitar 4 notas. Depois, o programa vai calcular a média dessas notas.")
print("Vamos começar!")
print("")

for i in range(1, 11):
    print(f"===- USUÁRIO NÚMERO {cont} -===")
    nota1 = float(input(f"{c} . Digite a primeira nota!: "))
    nota2 = float(input(f"{c2} . Digite a segunda nota!: "))
    nota3 = float(input(f"{c3} . Digite a terceira nota!: "))
    nota4 = float(input(f"{c4} . Digite a quarta nota!: "))
    cont += 1
    
    medias = (nota1 + nota2 + nota3 + nota4) / 4 
    media.append(medias)

print("=-"*25)
print("As médias dos alunos, em ordem, são:")

for i in media:
    print(f"Aluno Número {cont2} : {i}")
    cont2 += 1 
print("=-"*25)
     
    

