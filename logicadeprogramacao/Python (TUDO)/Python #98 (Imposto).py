def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_com_imposto = custo + imposto
    return custo_com_imposto

custo_inicial = float(input("Digite o custo do item: "))
taxa_imposto = float(input("Digite a taxa de imposto (%): "))

novo_custo = somaImposto(taxa_imposto, custo_inicial)

print(f"O custo com o imposto é: {novo_custo}")
