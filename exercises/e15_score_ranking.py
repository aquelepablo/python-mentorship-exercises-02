"""
Exercicio 15: Ranking de Pontuacao (Dict & List)

Objetivo:
Montar um ranking a partir de um dicionario convertido em lista de tuplas.

Enunciado:
1. Crie um sistema de ranking de um jogo.
2. Peca nomes e pontuações de jogadores e armazene em um Dicionario.
3. Converta o dicionario em uma List de tuplas para conseguir ordenar.
4. Exiba o Top 3 jogadores com as maiores pontuações em ordem decrescente.
"""
import re

from shared.text import normalize_number, normalize_text_without_accents_and_special_chars


try:
    print("---| Ranking de Pontuação |---\n")

    # Constants / Configuration
    END_KEYWORD = "sair"
    MAX_ATTEMPTS = 3
    SAFETY_LIMIT = 100

    # Variables
    game_rank = {}
    get_new_score = True

    # Inputs

    while get_new_score and len(game_rank) <= SAFETY_LIMIT:
        
        name_normalized = None
        name_attempts = 0
        while not name_normalized:
            if name_attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            if name_attempts == 0:
                prompt_message = f"Informe o nome do jogador (ou digite 'sair' para finalizar): "
            else:
                prompt_message = (
                    f"Entrada inválida {name_attempts}/{MAX_ATTEMPTS}. "
                    "Informe o nome do jogador (ou digite 'sair' para finalizar): "
                )
            
            raw_name = input(prompt_message).strip().lower()
            if END_KEYWORD in raw_name:
                get_new_score = False
                break

            name = normalize_text_without_accents_and_special_chars(raw_name)

            if name:
                name_normalized = name
                name = None
            else:
                name_attempts += 1
        
        if not get_new_score:
            break

        score_normalized = None
        score_attempts = 0
        while not score_normalized:
            if score_attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            if score_attempts == 0:
                prompt_message = f"Informe a pontuação do {name_normalized.title()}: "
            else:
                prompt_message = (
                    f"Entrada inválida {score_attempts}/{MAX_ATTEMPTS}. "
                    f"Informe a pontuação do {name_normalized.title()}: "
                )
            
            raw_score = input(prompt_message)

            score = normalize_number(raw_score)
            
            if score is not None:
                score_normalized = score
                score = None
            else:
                score_attempts += 1
        
        game_rank[name_normalized] = score_normalized
        name_normalized = None
        score_normalized = None
    
    if len(game_rank) > 0:

        sorted_game_rank = list(game_rank.items())
        sorted_game_rank.sort(key=lambda x: x[1], reverse=True)

        print("🏆 TOP 3 PLAYERS 🏆")
        for order, player in enumerate(sorted_game_rank[:3], 1):
            print(f" {order}. {player[0].title()} {player[1]: >10}")

    else:
        print("Nenhum score cadastrado.")


except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")