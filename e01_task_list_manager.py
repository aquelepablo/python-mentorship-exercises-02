"""
Exercício 1: Gerenciador de lista de tarefas
"""

try:
    tasks = ["Estudar Python", "Limpar quarto", "Fazer exercícios"]
    qty_tasks = len(tasks)

    new_task = input("Informe uma tarefa: ").strip()

    tasks_lower = list(map(lambda t: t.strip().lower(), tasks))

    if not new_task:
        print("Erro: Deve ser informada uma tarefa.")

    elif new_task.lower() in tasks_lower:
        print("Erro: Essa tarefa já existe")

    else:
        tasks.append(new_task)
        print(f"A tarefa {new_task.capitalize()} foi incluída com sucesso.")
        print("Lista atual:")
        for item in tasks:
            print(f" - {item.title()}")

except Exception as e:
    print(f"Erro: Houve um erro na informação enviada. Envie uma tarefa com ao menos duas palavras. (Ex.: Cozinhar bolo) - {e}")