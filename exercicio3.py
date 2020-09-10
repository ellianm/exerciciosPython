def exercicio3():
    listNumeros = []
    valor = 0
    listNumeros.append(int(input("Informe o primeiro número")))
    listNumeros.append(int(input("Informe o segundo número")))
    listNumeros.append(int(input("Informe o terceiro número")))

    if listNumeros[0] == listNumeros[1] == listNumeros[2]:
        valor = listNumeros[0]**3
    else:
        valor = listNumeros[0] + listNumeros[1] + listNumeros[2]
    return print(f'Valor total: {valor}')

if __name__ == '__main__':
    exercicio3()
