i = 1    #inserindo as variaveis que indicam quantos aneis de cada tipo sao necessarios para 
          #uma galinha
a = 2

numero = input("digite o numero de galinhas totais: ")
#solicitação do numero total de galinhas para a operação

custoi = int(0.40)   #+ custo de cada anel individual
custoa = int(0.35)


custounidade = (custoi * i) + (custoa * a) #custo para uma galinha

custotal = custounidade * numero