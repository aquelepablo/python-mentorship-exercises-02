"""
Exercicio 11: Gestao de Candidatos (Set)

Objetivo:
Praticar operacoes entre conjuntos.

Enunciado:
1. Considere os conjuntos:
   - vaga_python = {"Ana", "Bruno", "Caio"}
   - vaga_analista = {"Caio", "Duda", "Elena"}
2. Exiba os candidatos que se inscreveram para ambas as vagas (intersecao).
3. Exiba todos os candidatos unicos inscritos no processo seletivo (uniao).
4. Exiba os candidatos que estao apenas na vaga de Python e nao na de Analista.
"""
print("---| Gestão de Candidatos |---\n")

# Variables
python_jobs = {"Ana", "Bruno", "Caio"}
analyst_jobs = {"Caio", "Duda", "Elena"}

# Output

print(f"Candidatos da vaga de Python: {python_jobs}")
print(f"Candidatos da vaga de Analista: {analyst_jobs}")

# Candidatos inscritos para ambas as vagas (interseção)
print(f"Candidatos inscritos em ambas as vagas: {python_jobs & analyst_jobs}")

# Candidatos únicos inscritos no processo seletivo (união)
print(f"Candidatos únicos inscritos no processo seletivo: {python_jobs | analyst_jobs}")

# Candidatos apenas na vaga de Python e nao na de Analista
print(f"Candidatos apenas na vaga de Python e não de Analista: {python_jobs - analyst_jobs}")

