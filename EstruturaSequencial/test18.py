tamarq = float(input("Qual o tamanho do arquivo em MB?"))

veldown = float(input("Qual a velocidade de download em Mbps?"))

temposeg = tamarq / (veldown / 8)

tempomin = round(temposeg / 60, 2)

print(f"O tempo de download em minutos é: {tempomin} minutos.")