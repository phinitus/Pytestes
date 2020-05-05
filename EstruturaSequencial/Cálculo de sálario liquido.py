vhora = float(input("Quanto você ganha por hora? "))
nhora = int(input("Quantas horas trabalhadas? "))

salb = vhora * nhora

IR = salb * 0.11

INSS = salb * 0.08

SIND = salb * 0.05

desc = IR + INSS + SIND

salliq = salb - desc

print(f"Seu Salário liquido é: R${salliq}")