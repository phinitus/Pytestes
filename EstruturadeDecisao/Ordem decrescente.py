n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))

if n1 > n2 and n2 > n3:
    print(f"{n1}, {n2}, {n3}")
elif n1 > n3 and n3 > n2:
    print(f"{n1}, {n3}, {n2}")
elif n2 > n1 and n1 > n3:
    print(f"{n2}, {n1}, {n3}")
elif n2 > n3 and n3 > n1:
    print(f"{n2}, {n3}, {n1}")
elif n3 > n1 and n1 > n2:
    print(f"{n3}, {n1}, {n2}")
elif n3 > n2 and n2 > n1:
    print(f"{n3}, {n2}, {n1}")