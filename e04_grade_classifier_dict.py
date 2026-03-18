"""
Exercicio 4: Classificador de Notas (Dict + ELIF)

Objetivo:
Mapear dados e aplicar logica de classificacao sobre os valores.

Enunciado:
1. Crie um dicionario chamado boletim com 3 materias e suas respectivas notas
   (ex: {"Matematica": 8.5, "Portugues": 6.0, "Historia": 4.5}).
2. Peca para o usuario digitar o nome de uma materia.
3. Logica:
   - Se a materia existir no dicionario:
     - Se a nota for >= 7: exiba "Aprovado em [Materia]".
     - Se a nota for entre 5 e 6.9: exiba "Recuperacao em [Materia]".
     - Se for menor que 5: exiba "Reprovado em [Materia]".
   - Se a materia nao existir no dicionario, exiba "Materia nao encontrada".
"""

try:
   student_subject_grades = {
      "Matematica": 8.5, 
      "Portugues": 6.0, 
      "Historia": 4.5
   }

   subjects_list = ", ".join(map(lambda x: x, student_subject_grades.keys()))

   subject = input(f"Informe o nome de uma matéria ({subjects_list}) : ").strip()

   #normalized_subject_list = list(map(lambda t: t.strip().lower(), student_subject_grades))
   #Pensei nessa solução, mas isso gera o problema de não conseguir buscar a chave depois. Resolvi deixar a pesquisa literal.

   if subject not in student_subject_grades.keys():
      print("Matéria não encontrada")
   else:
      if student_subject_grades[subject] >= 7:
         print(f"Aprovado em {subject}")
      elif student_subject_grades[subject] >= 5:
         print(f"Recuperação em {subject}")
      else:
         print(f"Reprovado em {subject}")

except KeyboardInterrupt:
   print("\nAté logo")

except Exception as e:
   print(f"Erro: {e}")
