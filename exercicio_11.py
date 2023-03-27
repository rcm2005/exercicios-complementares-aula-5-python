p = float(0.38)     # declarando o valor dos paes e ds broas

b =  float(4.50)


np = input("digite o numero de pãezinhos vendidos: ") # solicitando o numero de paes e broas vendidos

nb = input("digite o numero de broas vendidas: ")



valorp = np * p
valorb = nb * b    #calculando quanto foi ganho individualmente com cada produto

valortotal =  valorp + valorb #calculando o valor total com a soma do lucro dos dois produtos

valorconta = valortotal * 10 / 100 # determinando o valor a ser depositado na conta poupança


valorganho = valortotal - valorconta   #calculando o valor de dinheiro ganho com o desconto do valor da conta poupança

print(f'o valor total arrecadado é de {valorganho} e {valorconta} vai para a poupança')  # declarando os resultados para o usuário


