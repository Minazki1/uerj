def binario(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * binario(int(num // 2))


num = int(input("Digite um número: "))
print(binario(num))
