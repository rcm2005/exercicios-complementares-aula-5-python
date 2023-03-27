real= float(input('Insira um valor em reais: '))
cotação = float(5.22)

valor = real / cotação

valorf = round(valor, 2)


print(f'{real} é equivalente a {valorf} dólares')