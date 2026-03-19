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


def remove_accents(value):
   normalized = unicodedata.normalize("NFD", value)
   return ''.join([char for char in normalized if not unicodedata.combining(char)])

try:
   # Constants / Configuration

   # Variables
   warehouse = {
      "products" : [],
      "unique_products": [],
      "qty_counterfeit_products": 0
   }

   # Inputs
   raw_user_input = input("Digite os nomes dos produtos que chegaram ao armazém (separados por vírgula): ").strip().lower()

   #Guard clause
   if len(raw_user_input) == 0:
      raise ValueError("É preciso informar ao menos um produto")

   else:
      # Sanitization
      products_list = raw_user_input.split(",").split(" e ")
      warehouse["products"] = [map(lambda x: remove_accents(x.strip().lower()), products_list)]

      # Validation
      if len(warehouse["products"]) == 1:
         print(f"Armazém possui apenas o produto {warehouse["products"][0].title()}")

      else:
         #Remover itens duplicados
         warehouse["unique_products"] = sorted(set(products_list))

         #Identifica quantidade de produtos piratas
         warehouse["qty_counterfeit_products"] = warehouse["products"] - warehouse["unique_products"]

   # Business Rules
         
   # Data Transformation
         unique_products = ", ".join(map(lambda x: x.capitalize(), warehouse["unique_products"]))

   # Output
         print(f"Produtos únicos no armazém: {', '.join(unique_products)}")

         if len(warehouse["qty_counterfeit_products"]) > 0:
            print(f"Número de itens \"piratas\" removidos: {warehouse["qty_counterfeit_products"]}")
         else:
            print(f"Não foram encontrados produtos piratas")

   """
      #Transforma a string em uma lista, removendo espaços extras
      products_list = list(map(lambda x: x.strip().lower(), raw_products_list.split(",")))

      #Cria um set para remover duplicatas
      unique_products = set(products_list)

      #Ordena a lista final
      sorted_products_list = sorted(unique_products, key=str.lower)
      sorted_products_list = [item.title() for item in sorted_products_list]

      #Calcula quantos itens duplicados foram removidos
      duplicates_removed = len(products_list) - len(unique_products)

      #Cria uma nova variável com nome consistente em string formatada para exibir os produtos únicos
      final_products_list = ", ".join(map(lambda x: x.capitalize(), sorted_products_list))

      #Exibe os resultados
      print(f"Produtos únicos no armazém: {', '.join(sorted_products_list)}")
      print(f"Número de itens \"piratas\" removidos: {duplicates_removed}")
   """

except KeyboardInterrupt:
   print("\nPrograma finalizado.")

except ValueError as e:
   print(f"\nEntrada inválida: {e}")

except Exception as e:
   print(f"\nErro: {e}")