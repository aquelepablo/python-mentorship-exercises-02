"""
Exercicio 13: Agrupamento por Categoria (Dict & List)

Objetivo:
Agrupar tarefas por prioridade usando dicionario e listas.

Enunciado:
1. Peca ao usuário para inserir 6 nomes de tarefas e suas respectivas prioridades
   ("Alta", "Media", "Baixa").
2. Crie um dicionário onde as chaves são as prioridades.
3. Os valores devem ser Lists contendo os nomes das tarefas.
4. Ao final, exiba as tarefas agrupadas, por exemplo:
   "Alta: [Tarefa 1, Tarefa 2]".
"""
from shared.text import normalize_text_without_accents_and_special_chars

def convert_priority(value: str) -> str | None:
   value = normalize_text_without_accents_and_special_chars(value)

   if "1" in value or "alta" in value:
      return_value = "Alta"

   elif "2" in value or "media" in value:
      return_value = "Media"

   elif "3" in value or "baixa" in value:
      return_value = "Baixa"

   else:
      return_value = None
   
   return return_value

try:
   print("---| Agrupamento por categoria |---\n")

   #Constants
   MAX_TASKS = 6
   MAX_ATTEMPTS = 3
   
   #Variables
   task_normalized = None
   priority_normalized = None

   priority_task_list = {
      "Alta": [],
      "Media": [],
      "Baixa": [],
   }

   # Inputs
   for task_index in range (0, MAX_TASKS):

      task_attempts = 0
      while not task_normalized:
         if task_attempts > MAX_ATTEMPTS:
               raise ValueError("Limite de tentativas alcançado.")

         if task_attempts == 0:
               prompt_message = f"Informe a tarefa {task_index+1}/{MAX_TASKS}: "
         else:
               prompt_message = (
                  f"Entrada inválida {task_attempts}/{MAX_ATTEMPTS}. "
                  "Informe uma tarefa: "
               )
         
         raw_task = input(prompt_message)
         task = normalize_text_without_accents_and_special_chars(raw_task)
         
         if task:
               task_normalized = task
               task = None
         else:
               task_attempts += 1
      
      priority_attempts = 0
      while priority_normalized is None:
         if priority_attempts > MAX_ATTEMPTS:
               raise ValueError("Limite de tentativas alcançado.")

         if priority_attempts == 0:
               prompt_message = "Informe a prioridade (1. Alta, 2. Media, 3. Baixa): "
         else:
               prompt_message = (
                  f"Entrada inválida {priority_attempts}/{MAX_ATTEMPTS}. "
                  "Informe uma distância válida: "
               )

         raw_priority = input(prompt_message).strip()
         priority = convert_priority(raw_priority)

         if priority:
               priority_normalized = priority
               priority = None
         else:
               priority_attempts += 1
      
      priority_task_list[priority_normalized].append(task_normalized)
      task_normalized = None
      priority_normalized = None   


   # Data Transformation
   for priority in priority_task_list.keys():
       priority_task_list[priority].sort(key=lambda x: x[1])

   # Output
   print("\nLista de Tarefas por Prioridade:")
   for priority in priority_task_list.keys():
       formatted_list = f"{', '.join(f'{task.title()}' for task in priority_task_list[priority])}"
       print(f"{priority.capitalize()}: {formatted_list}")

except KeyboardInterrupt:
   print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
   print(f"Entrada inválida: {error}")