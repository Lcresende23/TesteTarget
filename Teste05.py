def inverter(s):
    invercao = ''

    for i in range(len(s) - 1, -1, -1):
        invercao += s[i]
    return invercao

palavra = input("Digite a string que deseja inverter: ")
invertida = inverter(palavra)
print(f"A palavra {palavra} invertida ficou {invertida}")


