dia = int(input("digite o numero de dias trabalhados: "))

enc = 80 *dia #declarando quanto um encanador recebe por dia


imposto = enc *8 /100  #calculando o imposto de renda  ser pago


salario = enc - imposto  #calculando salario liquido sem o imposto 


print(f"O imposto será de {imposto} e o encanador receberá {salario}")  #mostrando o valor do salario liquido para o usuario.