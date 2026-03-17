try:
    admin_acesso = ("admin", "12345")

    login = input("Informe o usuário: ")
    password = input("Informe a senha: ")

    if login is None or password is None:
        print("Deve informar usuário e senha")
        exit()

    if login == admin_acesso[0] and password == admin_acesso[1]:
        print("Acesso concedido")
    else:
         print("Login ou senha incorretos")

except Exception as e:
    print(f"Erro: {e}")