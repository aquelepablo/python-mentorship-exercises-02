"""
Exercício 1: Gerenciador de Lista de Tarefas (List + IF)
Objetivo: Praticar busca e existência em listas.
1. Crie uma lista chamada tarefas com: "Estudar Python", "Limpar quarto", "Fazer exercícios".
2. Peça para o usuário digitar uma nova tarefa.
3. Lógica: Se a tarefa já estiver na lista (use o operador in), exiba "Essa tarefa já existe!". Caso contrário, adicione-a à 
lista com .append() e exiba a lista atualizada.

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