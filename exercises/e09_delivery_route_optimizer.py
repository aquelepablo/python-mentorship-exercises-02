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
from shared.text import normalize_number, normalize_text_without_accents_and_special_chars


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
    print("---| Otimizador de Rotas de Entrega |---\n")

    # Constants / Configuration
    MAX_DESTINIES = 5
    MAX_ATTEMPTS = 3

    # Variables
    destinies_list = []
    city = None
    distance = 0.0
    city_normalized = None
    distance_normalized = None


    # Inputs
    for count in range (0, MAX_DESTINIES):

        city_attempts = 0
        while not city_normalized:
            if city_attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            if city_attempts == 0:
                prompt_message = "Informe a cidade: "
            else:
                prompt_message = (
                    f"Entrada inválida {city_attempts}/{MAX_ATTEMPTS}. "
                    "Informe um nome de cidade: "
                )
            
            raw_city = input(prompt_message)
            city = normalize_text_without_accents_and_special_chars(raw_city)
            
            if city:
                city_normalized = city
                city = None
            else:
                city_attempts += 1
        
        destiny_attempts = 0
        while distance_normalized is None:
            if destiny_attempts > MAX_ATTEMPTS:
                raise ValueError("Limite de tentativas alcançado.")

            if destiny_attempts == 0:
                prompt_message = "Informe a distância: "
            else:
                prompt_message = (
                    f"Entrada inválida {destiny_attempts}/{MAX_ATTEMPTS}. "
                    "Informe uma distância válida: "
                )

            raw_distance = input(prompt_message).strip()
            distance = convert_distance(raw_distance)

            if distance is not None:
                distance_normalized = distance
                distance = None
            else:
                destiny_attempts += 1
        
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
