comprimento = float(input("Digite o comprimento da cozinha em metros: "))
altura = float(input("digite a altura da cozinha em metros: "))
largura = float(input("digite a largura da cozinha em metros: "))

paredesmenores = largura * altura * 2
paredesmaiores = comprimento * altura *2

caixa = float(1.5)


areatotal = paredesmaiores + paredesmenores 

qntcaixas = areatotal / caixa

print(qntcaixas)
