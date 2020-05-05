prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: "))
prod3 = float(input("Digite o preço do terceiro produto: "))

if prod1 < prod2 and prod1 < prod3:
    print("O produto 1 é o produto mais barato.")
elif prod2 < prod1 and prod2 < prod3:
    print("O produto 2 é o produto mais barato.")
elif prod3 < prod1 and prod3 < prod2:
    print("O produto 3 é o produto mais barato.")