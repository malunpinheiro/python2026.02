#caixa de mercad
#001 -> arroz (R$4,00)
#002 -> feijão (R$7,00)
#003 -> macarrão (R$5,00)

codigo = ""
total = 0
while codigo != "0":
      codigo = input("Digite um código: ")
      if codigo == "001":
        print("Produto tal adicionado")
        total = total+4
      elif codigo == "002":
        total = total+7
      elif codigo == "003":
        total = total+5
      else:
        total = total+0
        print("Código inválido")
print(f"O total das compras foi {total}")