areapin = float(input(("Qual o tamanho da area em metros quadrados? ")))

qtinta = areapin / 3

qlatas = round(qtinta / 18) + 1

valorTotal = qlatas * 80

print(f"A área a ser pintada é de {areapin} metros quadrados.\nSerão necessários {qtinta} litros de tinta.\nQue correspondem a {qlatas} latas.\nValor Total: R$ {float(valorTotal)}")