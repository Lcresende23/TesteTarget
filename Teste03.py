import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)


faturamentoDiario = [dia['valor'] for dia in dados if dia['valor'] > 0]

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