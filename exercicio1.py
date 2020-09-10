
def exercicio1():
    ended = False
    listNumeros = []
    print("Informe uma lista de números")
    while not ended:
        num = input("informe o número")
        listNumeros.append(num)
        ended = input("Deseja parar de inserir?").upper() == "S"
    print(f'Primeiro elemento da lista: {listNumeros[0]}')
    print(f'Último elemento da lista: {listNumeros[len(listNumeros)-1]}')


if __name__ == '__main__':
    exercicio1()
