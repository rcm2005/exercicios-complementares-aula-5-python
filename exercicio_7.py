
custofab = 27/100     #declarando as porcentagens relativas aos custos
distrib = 28/100
imposto = 45/100

valorcustofab = float(input('digite o custo de fabrica: ')) # solicitando o valor de fabrica do carro


valorimposto = float(45 * valorcustofab / 27)    #descobrindo valor do imposto com base nas porcentagens fornecidas e no custo de fabrica
valordistrib =  float(28 * valorcustofab / 28)

valortotal = valorcustofab + valorimposto + valordistrib   #descobrindo valor total utilizando os valores em dinheiro


valortotalr = round(valortotal, 2)        #arredondando o preço do custo do carro

print(f'O custo ao consumidor do carro é {valortotalr}')   #mostrando ao usuário o custo final a ser pago