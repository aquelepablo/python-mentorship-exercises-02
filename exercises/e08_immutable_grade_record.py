"""
Exercicio 8: Registro de Notas Imutavel (Tuple & Dict)

Objetivo:
Armazenar notas em tuplas e organizar alunos em um dicionario.

Enunciado:
1. Crie um sistema que peca o nome de 3 alunos e 2 notas para cada um.
2. Armazene as notas de cada aluno em uma Tuple para garantir que nao sejam alteradas.
3. Coloque essas tuplas dentro de um Dicionario onde a chave é o nome do aluno.
4. Calcule a media de cada aluno.
5. Exiba quem foi aprovado (media >= 7).
"""

from statistics import mean
from shared.text import normalize_number, normalize_text_without_accents_and_special_chars

try:

    print("---| Registro de Notas Imutável |---\n")

    # Constants / Configuration
    MIN_GRADE = 0.0
    MAX_GRADE = 10.0

    # Variables
    students_data = {}
    approved_students = {}

    # Inputs
    for count in range(1, 4):
        name_sentence = input(f"Informe o nome do {count}º aluno: ")
        first_grade, second_grade = (input("Informe a primeira nota (0 a 10): ")), (input("Informe a segunda nota (0 a 10): "))

        # Sanitization
        name_normalized = normalize_text_without_accents_and_special_chars(name_sentence)
        first_grade_normalized, second_grade_normalized = (normalize_number(first_grade, 2)), (normalize_number(second_grade, 2))

        #Validation:
        while not name_normalized:
            name_sentence = input(f"Nome inválido. Favor informar um nome valido para o {count}º aluno: ")
            name_normalized = normalize_text_without_accents_and_special_chars(name_sentence)
        
        ## Validation for duplicate names
        while students_data.get(name_normalized):
            name_sentence = input(f"{name_normalized.title()} já existe. Favor informar um nome diferente para o {count}º aluno: ")
            name_normalized = normalize_text_without_accents_and_special_chars(name_sentence)

        ## Validation for first grade
        while first_grade_normalized is None or first_grade_normalized < MIN_GRADE or first_grade_normalized > MAX_GRADE:
            first_grade = (input(f"Primeira nota inválida. Informe novamente a primeira nota entre 0 a 10: "))
            first_grade_normalized = normalize_number(first_grade, 2)

        ## Validation for second grade
        while second_grade_normalized is None or second_grade_normalized < MIN_GRADE or second_grade_normalized > MAX_GRADE:
            second_grade = (input(f"Segunda nota inválida. Informe novamente a segunda nota entre 0 a 10: "))
            second_grade_normalized = normalize_number(second_grade, 2)
        
        # Storage
        # As tuplas são imutáveis, garantindo que as notas não sejam alteradas após serem armazenadas.
        students_data[name_normalized] = first_grade_normalized, second_grade_normalized

    # Business Rules
    ## Calculate the average grade for each student and add it to the dictionary
    for student, grades in students_data.items():
        average_grade = round(mean(grades), 2)
        if average_grade >= 7:
            approved_students[student] = {
                "grades": grades,
                "average_grade": average_grade 
            }

    # Output
    if len(approved_students):
        print("\nLista de estudantes aprovados:")
        for student, student_grades in approved_students.items():
            print(f" - {student.title()}: Média {student_grades['average_grade']} - Notas: {student_grades['grades'][0]} e {student_grades['grades'][1]}")
    
    else:
        print("\n Nenhum estudante aprovado nessa turma.")
         
except KeyboardInterrupt:
    print("\nProgram finalizado pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")
