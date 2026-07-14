#comando do garçom
v=1
total = 0
while v != 0:
    v = int(input("Digite um valor: "))
    total += v
p = total * 1.1
print(f"O valor total da comanda com os 10% é {p}")
