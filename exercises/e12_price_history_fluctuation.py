"""
Exercício 12: Histórico de Preços com Flutuação (List & Dict)

Objetivo:
Atualizar uma lista de preços e analisar variação.

Enunciado:
1. Crie um dicionario para um produto (ex: "Smartphone").
2. A chave é o nome e o valor é uma List com os últimos 4 preços praticados.
3. Peca ao usuário um novo preço.
4. Remova o preço mais antigo da lista e adicione o novo.
5. Exiba a maior alta e a maior baixa registradas naquela lista de preços.
"""

import random

from shared.text import normalize_number


print("---| Histórico de Preços com Flutuação |---\n")

try:
    pass
    # Constants / Configuration

    # Variables

    #A variable receive a list with 4 product prices using the random function:
    
    product_name = "Smartphone"
    product_prices = {
        product_name: [round(random.uniform(100, 1000), 2) for _ in range(4)]
    }

    formatted_prices = f"{', '.join(f'€ {price:.2f}' for price in product_prices[product_name])}"

    # Inputs
    raw_new_price = input("Digite o preço atual do Smartphone: € ")

    # Sanitization
    new_price = normalize_number(raw_new_price)
    if new_price is None or new_price <= 0:
        raise ValueError("O preço deve ser um número válido positivo.")

    # Validation
    
    # Business Rules
    
    # Data Transformation
    
    # Atualiza histórico de preços
    product_prices["Smartphone"].pop(0)
    product_prices["Smartphone"].append(new_price)
    
    # Analyze price fluctuation
    price_history = product_prices["Smartphone"]
    
    # Calcula a flutuação de preços
    price_fluctuation = [
        price_history[i] - price_history[i - 1]
        for i in range(1, len(price_history))
    ]

    formatted_prices = f"{', '.join(f'€ {price:.2f}' for price in product_prices[product_name])}"

    # Calcula a maior alta e a maior baixa
    max_fluctuation = max(price_fluctuation)
    min_fluctuation = min(price_fluctuation)

    # Output
    print(f"\nHistórico de  preços de {product_name}: {formatted_prices}")
    print(f"\nMaior variação histórica de preços para {product_name}:")

    #Maior alta registrada: Se não houver alta, deve tratar isso na mensagem:
    if max_fluctuation > 0:
        print(f"Maior alta registrada: € {max_fluctuation:.2f}")
    else:
        print("Não houve alta registrada.")

    #Maior baixa registrada: Se não houver baixa, deve tratar isso na mensagem:
    if min_fluctuation < 0:
        print(f"Maior baixa registrada: € {min_fluctuation:.2f}")
    else:
        print("Não houve baixa registrada.")


except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")
