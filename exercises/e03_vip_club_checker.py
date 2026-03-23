"""
Exercicio 3: Verificador de Clube (Set + IF/ELIF)

Objetivo:
Usar conjuntos para verificar permissoes unicas.

Enunciado:
1. Crie um Set chamado convidados_vip com 4 nomes de sua escolha.
2. Peca para o usuario digitar o seu nome.
3. Logica:
   - Se o nome estiver no Set, exiba "Bem-vindo a area VIP!".
   - Se o nome for "Dono", exiba "Bem-vindo, chefe!".
   - Para qualquer outro nome, exiba "Acesso apenas com convite".
"""

try:
   owner = "Dono"
   vip_guests = {"João", "Massimo", "Genevra", "Matilde"}

   guest_name = input("Diga seu nome: ").strip()

   if guest_name.lower() == owner.strip().lower():
      print("Bem-vindo, chefe!")

   elif guest_name.lower() in list(map(lambda t: t.strip().lower(), vip_guests )):
      print("Bem-vindo à área VIP!")
   
   else:
      print("Acesso apenas com convite")

except KeyboardInterrupt:
    print("\nAté logo")

except Exception as e:
   print(f"\nFalha na matrix: {e}")