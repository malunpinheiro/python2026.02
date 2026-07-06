cod = input("Digite o código: ")
match cod:
    case "200":
        print("Sucesso! Tudo certo com a sua requisição.")
    case "400":
        print("Erro do cliente: Requisição malformada.")
    case "401" | "403":
        print("Erro de permissão: Você não tem acesso a essa página.")
    case "500" | "503":
        print("Erro no servidor: Nosso sistema está instável no momento.")
    case _:
        print("Código HTTP - desconhecido.")