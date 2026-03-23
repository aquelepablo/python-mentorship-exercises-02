"""
Exercicio 6: Sistema de Inventario Unico (Set & List)

Objetivo:
Trabalhar com listas, conjuntos e remocao de itens duplicados.

Enunciado:
1. Peca ao usuario para digitar uma lista de nomes de produtos que chegaram ao armazem
   (separados por virgula).
2. Converta essa entrada em uma List.
3. Remova automaticamente todos os itens duplicados usando um Set.
4. Exiba a lista final ordenada alfabeticamente.
5. Mostre quantos itens "piratas" (repetidos) foram removidos.
"""

import unicodedata

try:
   # Constants / Configuration

   # Variables
   warehouse = {
      "products" : [],
      "unique_products": [],
      "qty_counterfeit_products": 0
   }

   # Inputs
   raw_user_input = input("Digite os nomes dos produtos que chegaram ao armazém (separados por vírgula): ").strip()


   #Guard clause
   if len(raw_user_input) == 0:
      raise ValueError("É preciso informar ao menos um produto")

   else:
      # Sanitization
      normalized_products_input = raw_user_input.lower().replace(" e ", ", ")
      normalized_products_input = unicodedata.normalize("NFD", normalized_products_input)
      normalized_products_input = "".join(char for char in normalized_products_input if not unicodedata.combining(char))

      warehouse["products"] = [
            item.strip()
            for item in normalized_products_input.split(",")
            if item.strip()
         ]

      #Guard clause
      if len(warehouse["products"]) == 0:
         raise ValueError("É preciso informar ao menos um produto")

      # Validation
      #Remover itens duplicados
      warehouse["unique_products"] = sorted(set(warehouse["products"]))

      #Identifica quantidade de produtos piratas
      warehouse["qty_counterfeit_products"] = len(warehouse["products"]) - len(warehouse["unique_products"])

      # Business Rules

      # Data Transformation
      unique_products = ", ".join(map(lambda x: x.capitalize(), warehouse["unique_products"]))

      # Output
      print(f"Produtos únicos no armazém: {unique_products}")

      if warehouse["qty_counterfeit_products"] > 0:
         print(f"Número de itens \"piratas\" removidos: {warehouse['qty_counterfeit_products']}")
      else:
        print(f"Não foram encontrados produtos piratas") 

except KeyboardInterrupt:
   print("\nPrograma finalizado.")

except ValueError as e:
   print(f"\nEntrada inválida: {e}")