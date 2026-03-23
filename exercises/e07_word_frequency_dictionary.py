"""
Exercicio 7: Word Frequency Dictionary (Dict)

Objetivo:
Contar a frequencia de palavras em uma frase usando dicionario.

Enunciado:
1. Peca uma frase qualquer ao usuario.
2. Crie um dicionario que conte a frequencia de cada palavra na frase.
3. Exemplo: "python e bom python e top" -> {"python": 2, "e": 2, "bom": 1, "top": 1}.
4. Exiba apenas as palavras que apareceram mais de uma vez.
"""

from shared.text import normalize_text_without_accents_and_special_chars

try:
    # Constants / Configuration

    # Variables
    word_frequency = {}
    repeated_words = {}

    # Inputs
    sentence = input("Digite uma frase: ").strip()

    #Guard clause
    if len(sentence) == 0:
        raise ValueError("É preciso informar uma frase.")

    # Sanitization
    normalized_sentence = normalize_text_without_accents_and_special_chars(sentence)

    # Split the normalized sentence into words
    words = normalized_sentence.split()

    # Validation
    if len(words) == 0:
        raise ValueError("É preciso informar uma frase com palavras.")
    
    # Business Rules
    ## Count the frequency of each word
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    ## Identify repeated words
    for word, count in word_frequency.items():
        if count > 1:
            repeated_words[word] = count

    # Output
    ## Show frequent words
    if len(repeated_words) > 0:
        print("Palavras frequentes: ")
        for key, value in repeated_words.items():
            print(f"{key}: {value}")
    else:
        print("Não foram encontradas palavras frequentes na sua frase.")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")