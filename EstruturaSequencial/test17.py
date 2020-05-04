areapin = float(input("Qual o tamanho da area em metros quadrados? "))

qtinta = areapin / 6

qlatas = round(qtinta / 18) + 1

qgal = round(qtinta / 3.6) + 1

qmistlat = round(qtinta // 18)

qmistgal = round((qtinta - 18) / 3.6) + 1

valorTotallat = qlatas * 80

valorTotalgal = qgal * 25

valorTotalmist = round((qmistlat * 80) + (qmistgal * 25), 2)

print(f"A área a ser pintada é de {areapin} metros quadrados.\nSerão necessários {qtinta} litros de tinta.\n")
print(f"Que correspondem a {qlatas} latas.\nValor Total: R$ {float(valorTotallat)}\n")
print(f"Que correspondem a {qgal} galões.\nValor Total: R$ {float(valorTotalgal)}\n")
print(f"Que correspondem a {qmistlat} latas e {qmistgal} galões.\nValor Total: R$ {float(valorTotalmist)}")
