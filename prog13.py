from datetime import datetime

anonasc = int(input("Digite seu ano de nascimento: "))
anoatual = datetime.now() .year
idade = anoatual - anonasc

print( f"Você tem {idade} anos.")

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")