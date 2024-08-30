def num(n):
    a = 0
    b = 1

    while b < n:
        a, b = b, a + b
    return b == n or n == 0

verificar = int(input("Informe o número que quer conferir: "))

if num(verificar):
    print(f"O número {verificar} pertence à sequencia!")
else:
    print(f"O número {verificar} não pertence à sequencia")