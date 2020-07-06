num = int(input("Digite um número menor que 1000: "))
numcent = num // 100
numdez = (num - (numcent * 100)) // 10
numuni = num % 10

if 0 < num < 1000:
    if num < 10:
        print(f"O número tem {num} unidades.")
    elif num >= 10 and num < 20:
        print(f"O número tem {numdez} dezena e {num - 10} unidades.")
    elif num >= 20 and num < 100:
        print(f"O número tem {numdez} dezenas e {numuni} unidades.")
    elif num >= 100 and num< 1000:
        if num >= 100 and num < 110:
            print(f"O número tem {numcent} centena e {numuni} unidades.")
        elif num >= 110 and num < 120:
            print(f"O número tem {numcent} centena, {numdez} dezena e {numuni} unidades.")
        elif num >= 120 and num < 200:
            print(f"O número tem {numcent} centena, {numdez} dezenas e {numuni} unidades.")
        elif num >= 200 and num < 1000:
            print(f"O número tem {numcent} centenas, {numdez} dezenas e {numuni} unidades.")

else:
    print("Valor inválido!")