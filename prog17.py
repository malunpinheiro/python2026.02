temp = int(input("Digite o valor da temperatura aqui: "))

if temp < 18:
    print(f"A temperatura {temp} é frio:(")
elif temp >= 18 and temp < 30:
    print(f"A temperatura {temp} é agradável:)")
else:
    print(f"A temperatura {temp} é calor:)(")