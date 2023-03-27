i = 1.0    #inserindo as variaveis que indicam quantos aneis de cada tipo sao necessarios para 
          #uma galinha
a = 2.0


numero = float(input("digite o numero de galinhas totais: "))
#solicitação do numero total de galinhas para a operação

custoi = 0.40   #+ custo de cada anel individual
custoa = 0.35


custounidade = (custoi * i) + (custoa * a) #custo para uma galinha

custotal = float(custounidade * numero)

custofinal = round(custotal, 2)    #para arrendondar o custo total em 2 casas decimais


print (f'o custo total será de R$ {custofinal}')

