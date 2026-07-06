idade = int(input("Digite aqui sua idade: "))
ing = input("Você tem o ingresso (S - Sim/N - Não)? ").upper()

if idade >=12 and ing == "S":
    print("Acesso liberado! Divirta-se no brinquedo.")
elif ing == "S" and idade <12:
    print("Você tem o ingresso, mas não tem a idade mínima de 12 anos.")
else:
    print("Acesso negado. Você precisa de um ingresso.")
