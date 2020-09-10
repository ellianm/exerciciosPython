def exercicio4():
    lista_elementos_1 = ['Douglas', 'Anderson', 'Libório', 'Maicon', 'Prefeito Géri']
    lista_elementos_2 = ['Douglas', 'Maicon', 'Libório']
    listadiferenca = list(set(lista_elementos_1) - set(lista_elementos_2))
    print(listadiferenca)

if __name__ == '__main__':
    exercicio4()
