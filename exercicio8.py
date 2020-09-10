import numpy
def exercicio8():
    ended = False
    listNumeros = []
    print("Informe uma lista de números")
    while not ended:
        num = float(input("informe o número"))
        listNumeros.append(num)
        ended = input("Deseja parar de inserir?").upper() == "S"

    print(f'Média aritmética: {numpy.mean(listNumeros)}')


if __name__ == '__main__':
    exercicio8()
