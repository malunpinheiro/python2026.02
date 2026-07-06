cargo = input("Digite o cargo do funcionário: ").lower()

if cargo == "caixa":
    salario = 1500
    print(salario)
elif cargo == "vendedor":
    salario = 2400
    print(salario)
elif cargo == "gerente":
    salario = 4000
    print(salario)
else:
    salario=0
    print("Cargo inválido")
inss = salario * 0.12

#irrf

if salario > 2000:
    irrf = salario * 0.14
else:
    irrf = salario * 0.08

#fim irrf
sf = salario - irrf - inss
print(f"Querido, seu cargo de {cargo} tem o salário de {salario} e os impostos são: ")
print(f"INSS -> {inss}")
print(f"IRRF -> {irrf}")
print(f"Seu salário final é {sf}.")