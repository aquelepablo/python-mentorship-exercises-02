"""
Exercicio 14: Validador de Tuplas em Conjuntos (Set & Tuple)

Objetivo:
Armazenar coordenadas unicas usando tuplas dentro de um conjunto.

Enunciado:
1. Peca ao usuario pares de coordenadas (x, y).
2. Armazene cada par em uma Tuple.
3. Adicione as tuplas a um Set.
4. Se o usuario tentar inserir uma coordenada que ja existe,
   o programa deve avisar: "Coordenada duplicada ignorada".
5. Ao final, exiba a distancia total percorrida entre todos os pontos unicos.
"""

import math

from shared.text import normalize_number, normalize_text_without_accents_and_special_chars

def convert_coordinates(coord_pair: str) -> tuple | None:

    coord_list = coord_pair.split(",")

    if len(coord_list) == 2:

        coord_x = normalize_number(coord_list[0])
        coord_y = normalize_number(coord_list[1])

        if coord_x and coord_y:
            return (coord_x, coord_y)

    return None

try:
    print("---| Validador de Tuplas em Conjuntos |---\n")

    # Constants / Configuration
    END_KEYWORD = "sair"
    MAX_ATTEMPTS = 3

    # Variables
    unique_coordinates = set()
    coordinates_list = []
    get_new_coordinate = True

    # Inputs

    while get_new_coordinate:
        coords = None
        coord_attempts = 0
        while not coords:
            if coord_attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            if coord_attempts == 0:
                prompt_message = f"Informe um par de coordenadas x, y (ou digite 'sair' para finalizar): "
            else:
                prompt_message = (
                    f"Entrada inválida {coord_attempts}/{MAX_ATTEMPTS}. "
                    "Informe um par de coordenadas x, y (ou digite 'sair' para finalizar): "
                )
            
            raw_coord = input(prompt_message).strip().lower()
            if END_KEYWORD in raw_coord:
                get_new_coordinate = False
                break

            coords = convert_coordinates(raw_coord)
            
            if coords:
                
                # Verifica se a coordenada já existe no conjunto
                if coords not in unique_coordinates:
                    coordinates_list.append(coords)
                    unique_coordinates.add(coords)
            else:
                coord_attempts += 1
        
    # Calcula a distancia total percorrida entre os pontos únicos
    total_distance = 0
    for i in range(len(coordinates_list) -1):
        actual_coord = coordinates_list[i]
        next_coord = coordinates_list[i + 1]

        total_distance += math.dist(actual_coord, next_coord)

    # Output
    # Exibe as coordenadas únicas e a distância total percorrida
    print(f"\nCoordenadas únicas inseridas: {unique_coordinates}")
    print(f"Distância total percorrida entre os pontos únicos: {total_distance:.2f}")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")