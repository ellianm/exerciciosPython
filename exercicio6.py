
def exercicio6():
    num = int(input("Quantas iterações deseja fazer? "))
    primeiroElemento = 0
    segundoElemento = 1
    if num < 0:
        return print("Número inválido")
    else:
        print(primeiroElemento, segundoElemento, end=" ")
        for x in range(2, num):
            next = primeiroElemento + segundoElemento
            print(next, end=" ")
            primeiroElemento = segundoElemento
            segundoElemento = next


if __name__ == '__main__':
    exercicio6()
