voton = int(input('Digite o numero de votos nulos: '))

votov = int(input('Digite o numero de votos válidos: '))

votob = int(input('Digite o numero de votos em branco: '))

total = voton + votov + votob


n = ((100 *voton)/total)
v = ((100 *votov)/total)
b = ((100 * votob)/total)


nf = round (n, 2)
vf = round(v, 2)
bf = round(b, 2)


cem = n + v + b


print (f'os votos nulos são {nf}%, os válidos {vf}% e os em branco {bf}%.')