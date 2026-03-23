"""
Desafio e05: O Protocolo Sentinela de Dados

Cenario:
Voce foi contratado para programar a logica de um cofre digital de altissima seguranca de uma
corretora de criptomoedas. O sistema recebe varios dados de uma vez e voce precisa decidir se
libera a trava ou aciona o alarme.

1. Preparação dos Dados (Contexto)
As variáveis iniciais que representam o estado atual do sistema:
#Banco de dados do sistema
usuarios_bloqueados = {"hackerman", "dr_evil", "py_robot"}
funcionarios_ativos = ("ana_gerente", "bruno_tech", "carla_diretora")
chaves_biometricas = {"setor_a": "digital_ok", "setor_b": "iris_ok"}

#Tentativa atual (Entrada de Dados)
usuario = input("Digite o nome de usuário: ")
cargo = input("Digite o cargo (gerente, tecnico, estagiario): ")
possui_cartao = True #Simule como se viesse de um sensor
tentativa_senha = 1

Escreva um programa que use apenas um bloco de IF/ELIF/ELSE para validar o acesso.
O acesso só será concedido se todas as seguintes condições forem verdadeiras:

1. Seguranca de lista negra:
   - O usuario NAO pode estar no conjunto `usuarios_bloqueados`.
2. Verificacao de hierarquia:
   - O usuario deve estar na tupla `funcionarios_ativos`.
3. Multiplos fatores:
   - O usuario deve ter o `cartao_id` OU saber a senha mestra.
   - Exemplo de senha mestra: `Python2024`.
4. Bloqueio de estagiario:
   - Se o cargo for `estagiario`, o acesso e negado automaticamente,
     mesmo que as outras condicoes sejam verdadeiras.
5. Integridade do sistema:
   - O dicionario `chaves_biometricas` deve conter a chave `setor_a`
     com o valor `digital_ok`.

Saidas esperadas:
- Se passar em tudo: "🔒 ACESSO LIBERADO. Bem-vindo, [NOME]!"
- Se for estagiario: "⚠ Acesso negado: Estagiarios nao possuem nivel de acesso ao cofre."
- Se estiver bloqueado: "🚫 ALARME ACIONADO: Usuario na lista de restricao!"
- Para qualquer outro erro: "❌ ACESSO NEGADO: Credenciais invalidas ou erro de biometria."
"""
import random

try:
   master_pass = "PythonDigitalSafe"

   #System Database | Banco de dados do sistema
   blocked_users = {"hackerman", "dr_evil", "py_robot"}
   active_employees = ("ana_gerente", "bruno_tech", "carla_diretora")
   biometric_keys = {"setor_a": "digital_ok", "setor_b": "iris_ok"}

   #Actual attempt | Tentativa atual (Entrada de Dados)
   user = input("Digite o nome de usuário: ")
   position = input("Digite o cargo (gerente, tecnico, estagiario): ")
   has_card = True #Simule como se viesse de um sensor
   password_attempt = 1

   #Simulando a entrada via um sensor
   sensor_read = input("🤖 [Sensor simulado] O usuário inseriu o cartão de acesso? [S/N]: ").strip().lower()
   
   #Transforma apenas o S em True e qualquer exceção como False
   has_card = (sensor_read == 's')

   if not has_card:
      print("🤖 Necessário informar senha no teclado físico...")
      attempt_pass = input("Senha: ")
   else:
      attempt_pass = None

   #Simulação de um sensor biométrico
   print("\n🤚 [SENSOR BIOMÉTRICO] Por favor, posicione o dedo no leitor do Setor A...")
   attempt_digital = input("🤖 [Sensor simulado] A digital do usuário foi validada? [S/N]: ").strip().lower()
   digital_read = "digital_ok" if (attempt_digital == 's') else None
   

   #Simulando uma segurança real, fazemos uma validação de forma aleatória da iris do usuário
   check_iris = random.choice([True, False])
   if check_iris:
      print("\n👁 [SENSOR BIOMÉTRICO] Por favor, realize a validação de iris...")
      attempt_iris = input("🤖 [Sensor simulado] A iris do usuário foi validada? [S/N]: ").strip().lower()
      iris_read = "iris_ok" if (attempt_iris == 's') else None
   else:
      attempt_iris = None

   attempt_login = f"{user}_{position}"
   #attempt_pass = "teste"
   #user_biometric_keys = {"setor_a": "digital_ok", "setor_b": "iris_ok"}

   # Começamos verificando os casos de bloqueio explícito e prioritário primeiro (Fail-fast).
   if user in blocked_users:
      print("🚫 ALARME ACIONADO: Usuário na lista de restrição!")
   
   elif position.strip().lower() == "estagiario":
      print("⚠ Acesso negado: Estagiarios nao possuem nivel de acesso ao cofre.")   
   
   # Se não caiu em nenhum bloqueio acima, verificamos as regras de sucesso todas juntas:
   elif( 
      attempt_login in active_employees and
      (has_card or attempt_pass == master_pass) and
       digital_read == biometric_keys.get("setor_a") and
      (not check_iris or iris_read == biometric_keys.get("setor_b"))):
      
      print(f"🔒 ACESSO LIBERADO. Bem-vindo(a), {user.capitalize()}!")

   else:
      print("❌ ACESSO NEGADO: Credenciais invalidas ou erro de biometria.")

except KeyboardInterrupt:
   print("\n Desconectado.")

except Exception as e:
   print(f"\nErro inesperado: {e}")