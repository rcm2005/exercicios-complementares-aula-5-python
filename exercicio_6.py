#calcular area de um circulo

raio = float(input('digite o raio do circulo em centimetros: '))


pi = 3.1415

area = pi * raio**2
arear = round(area,2)

print(f'A area do circulo é {arear} centimetros quadrados')