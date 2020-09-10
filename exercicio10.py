
def exercicio8():
    numVitorias = int(input("Informe o número de vitórias"))
    numEmpates = int(input("Informe o número de empates"))
    numDerrotas = int(input("Informe o número de derrotas"))

    totalDePontos = (numVitorias * 3) + (numEmpates * 1)
    print(f'Total de pontos do time foi: {totalDePontos}')

if __name__ == '__main__':
    exercicio8()
