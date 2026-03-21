"""
Exercicio 9: Otimizador de Rotas de Entrega (List & Tuple)

Objetivo:
Usar tuplas dentro de listas e ordenar dados por distancia.

Enunciado:
1. O usuario deve inserir 5 destinos de entrega (cidades).
2. Armazene cada cidade com sua distancia da central em uma Tuple: ("Cidade", distancia).
3. Coloque todas as tuplas em uma List.
4. Ordene a lista pela distancia, da mais proxima para a mais distante.
5. Exiba o roteiro de entrega otimizado.
"""

from dis import disco
from typing import List

from shared.text import normalize_number, normalize_text_without_accent, normalize_text_without_accents_and_special_chars


def convert_distance(value: str) -> float | None:
    """
    Converte uma string de distância para um valor numérico em quilômetros, considerando diferentes unidades de medida.
    """
    convert_factor = 1.0

    if "km" in value or "quilometro" in value:
        value = value.replace("quilometros", "").replace("quilometro", "").replace("km","")
    
    elif "cm" in value or "centimetro" in value:
        value = value.replace("centimetros", "").replace("centimetro", "").replace("cm","")
        convert_factor /= 100000.0

    elif "mi" in value or "milha" in value:
        value = value.replace("milhas", "").replace("milha", "").replace("mi","")
        convert_factor = 1.60934

    elif "m" in value or "metro" in value:
        value = value.replace("metros", "").replace("metro", "").replace("m","")
        convert_factor /= 1000.0
    
    #value = normalize_text_without_accents_and_special_chars(value)
    distance = normalize_number(value)

    if distance:
        distance *= convert_factor
        distance = round(distance, 2)

    return distance
    

try:

    print(len("ROTEIRO DE ENTREGA OTIMIZADO"))
    print("---| Otimizador de Rotas de Entrega |---\n")

    # Constants / Configuration
    MAX_DESTINIES = 5
    MAX_ATTEMPTS = 3

    # Variables
    destinies_list = []
    attempts = 0
    input_count = 1
    city = None
    distance = 0.0
    city_normalized = None
    distance_normalized = None
    convert_to = ""


    # Inputs
    for count in range (0, MAX_DESTINIES):
        while not city_normalized:
            if attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            city = normalize_text_without_accents_and_special_chars(
                input(
                    f"{'Informe a cidade: ' if not city else 'Entrada inválida ' + str(attempts) + '/' + str(MAX_ATTEMPTS) + '. Informe um nome de cidade: '}"
                        ).strip())
            if city:
                city_normalized = city
                city = None
                attempts = 0
            else:
                attempts += 1
                city = " "
        
        while not distance_normalized:
            if attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            distance = convert_distance(
                input(
                    f"{'Informe a distância: ' if not city else 'Entrada inválida ' + str(attempts) + '/' + str(MAX_ATTEMPTS) + '. Informe uma distância válida: '}"
                        ).strip())
            if distance:
                distance_normalized = distance
                distance = None
            else:
                attempts += 1
                distance = " "
        
        destinies_list.append((city_normalized, distance_normalized))
        city_normalized = None
        distance_normalized = None
        
    # Business Rules
    ## Sort the list of destinies by distance
    destinies_list.sort(key=lambda x: x[1])

    # Data Transformation

    # Output
    print(f"\n{'-' * 10} {'ROTEIRO DE ENTREGA OTIMIZADO'} {'-' * 10}")
    print(f"  | {'CIDADE': ^30} | {'DISTÂNCIA': ^13}")
    
    for num, destiny in enumerate(destinies_list, 1):
        print(f"{str(num)} | {destiny[0].title(): ^30} | {str(destiny[1]): >10} km")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")
