
def exercicio7():
    ano=int(input('Digite o ano desejado para calcularmos o dia da páscoa:'))
    a = int(ano % 19)
    b = int(ano / 100)
    c = int(ano % 100)
    d = int(b / 4)
    e = int(b % 4)
    f = int((b + 8) / 25)
    g = int((b - f + 1) / 3)
    h = ((19 * a + b - d - g + 15) % 30)
    i = int(c / 4)
    k = int(c % 4)
    L = ((32 + 2 * e + 2 * i - h - k) % 7)
    m = int((a + 11 * h + 22 * L) / 451)
    mes = int((h + L - 7 * m + 114) / 31)
    if mes == 1: mes='Janeiro'
    elif mes == 2:
        mes = 'Fevereiro'
    elif mes == 3:
        mes = 'Março'
    elif mes == 4:
        mes = 'Abril'
    elif mes == 5:
        mes = 'Maio'
    elif mes == 6:
        mes = 'Junho'
    elif mes == 7:
        mes = 'Julho'
    elif mes == 8:
        mes = 'Agosto'
    elif mes == 9:
        mes = 'Setembro'
    elif mes == 10:
        mes = 'Outubro'
    elif mes == 11:
        mes = 'Novembro'
    else:
        mes = 'Dezembro'
    mes1 = mes
    dia = int((h+L-7*m+114) % 31)+1
    print(f'a pascoa do ano {ano} será no dia {dia} do mês {mes1}')


if __name__ == '__main__':
    exercicio7()
