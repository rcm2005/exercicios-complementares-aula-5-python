print('Conversor de segundos para horas, minutos e segundos')

valori = int(input('Digite um valor em segundos: '))


segundos = valori % 60
minutos = valori // 60
horas = minutos // 60
minutos = segundos % 60


print(f' {valori} segundos são {horas} hora(s),{minutos} minuto(s) e {segundos} segundo(s)')




