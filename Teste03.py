import json

#Arquivo JSON
faturamento_mensal = {
    "faturamento_diario": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 26742.6612},
        {"dia": 7, "valor": 0.0},
        {"dia": 8, "valor": 42889.2258},
        {"dia": 9, "valor": 46251.174},
        {"dia": 10, "valor": 11191.4722},
        {"dia": 11, "valor": 0.0},
        {"dia": 12, "valor": 0.0},
        {"dia": 13, "valor": 3847.4823},
        {"dia": 14, "valor": 373.7838},
        {"dia": 15, "valor": 2659.7563},
        {"dia": 16, "valor": 48924.2448},
        {"dia": 17, "valor": 18419.2614},
        {"dia": 18, "valor": 0.0},
        {"dia": 19, "valor": 0.0},
        {"dia": 20, "valor": 35240.1826},
        {"dia": 21, "valor": 43829.1667},
        {"dia": 22, "valor": 18235.6852},
        {"dia": 23, "valor": 4355.0662},
        {"dia": 24, "valor": 13327.1025},
        {"dia": 25, "valor": 0.0},
        {"dia": 26, "valor": 0.0},
        {"dia": 27, "valor": 25681.8318},
        {"dia": 28, "valor": 1718.1221},
        {"dia": 29, "valor": 13220.495},
        {"dia": 30, "valor": 8414.61}
    ]
}

with open ('faturamento.json', 'w') as json_file:
    json.dump(faturamento_mensal, json_file, indent=4)

faturamentoDiario = [dia['valor'] for dia in faturamento_mensal['faturamento_diario'] if dia['valor'] > 0]

maiorFaturamento = max(faturamentoDiario)
print(f"O maior faturamento diário foi {maiorFaturamento:.2f}")

menorFaturamento = min(faturamentoDiario)
print(f"O menor faturamento diário foi {menorFaturamento:.2f}")

mediaMensal = sum(faturamentoDiario) / len(faturamentoDiario)
print(f"a média mensal foi {mediaMensal:.2f}")

AcimaMedia = 0

for valor in faturamentoDiario:
    if valor > mediaMensal:
        AcimaMedia +=1

print(f"O numero de dias com faturamento acima da média foi de {AcimaMedia}")

