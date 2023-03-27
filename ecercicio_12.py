comprimento = float(input("Digite o comprimento da cozinha em metros: "))
altura = float(input("digite a altura da cozinha em metros: "))     #solicitando as medidas das paredes
largura = float(input("digite a largura da cozinha em metros: "))  # obs: as medidas devem ser inseridas em metros

paredesmenores = largura * altura * 2     #somando a area das duas paredes menores iguais
paredesmaiores = comprimento * altura *2    #somando area paredes maiores

caixa = float(1.5)         # determinando a area em asulejos por caixa

areatotal = paredesmaiores + paredesmenores #calculando a area total somando as paredes

qntcaixas = areatotal / caixa   #descobrindo a quantidade total de caixas que serão necessárias

print(qntcaixas)
