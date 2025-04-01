dicionario = []

while True:
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano do livro: ")
    
    livro = {
        "nome": nome,
        "autor": autor,
        "ano": ano
    }
    
    dicionario.append(livro)
    
    continuar = input("Você deseja adicionar outro livro? (sim/não): ").lower()
    
    if continuar != 'sim':
        break

print("Livros cadastrados:")

for livro in dicionario:
    print(f"{livro['nome']} de {livro['autor']} ({livro['ano']})")
