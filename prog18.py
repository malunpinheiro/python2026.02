sexo = input("Digite aqui seu gênero (M - masculino/F - feminino): ").upper()
idade = int(input("Digite aqui sua idade: "))
print(f"Sexo {sexo} idade {idade}")

if sexo == "M" and idade >= 18:
    print("Candidato apto a se alistar!")
else:
    input("Você não está apto:(")
