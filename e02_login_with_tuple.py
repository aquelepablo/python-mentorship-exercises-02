"""
Exercício 2: Sistema de Login com Tupla (Tuple + IF/ELSE)
Objetivo: Usar a imutabilidade para segurança básica.
1. Crie uma tupla chamada admin_acesso que contém: ("admin", "12345").
2. Peça para o usuário digitar o usuario e a senha.
3. Lógica:
○ Se o usuario for igual ao primeiro item da tupla E a senha for igual ao segundo item, exiba "Acesso 
concedido!".
○ Caso contrário, exiba "Login ou senha incorretos".
"""

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