faturamento = {
 'SP': 67_836.43,
 'RJ': 36_678.66,
 'MG': 29_229.88,
 'ES': 27_165.48,
 'Outros': 19_849.53
}

total = sum(faturamento.values())
print(f"O faturamento total é {total:.2f}")

percentuais = {}

for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    percentuais[estado] = percentual

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")





