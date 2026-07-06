nome = input("Digite seu nome: ")
notasbi1 = float(input("Digite a nota 1: "))
notasbi2 = float(input("Digite a nota 2: "))
notasbi3 = float(input("Digite a nota 3: "))
notasbi4 = float(input("Digite a nota 4: "))

media = (notasbi1 + notasbi2 + notasbi3 + notasbi4) / 4
print("Sua média é: ", (media))

if media >= 6:
    print("Aprovado")
else:
    print("Recuperação")