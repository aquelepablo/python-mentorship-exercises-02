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

try:
   products_in_warehouse = input("Digite os nomes dos produtos que chegaram ao armazém (separados por vírgula): ")
   
   #Transforma a string em uma lista, removendo espaços extras
   products_list = list(map(lambda x: x.strip(), products_in_warehouse.split(",")))

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

except KeyboardInterrupt:
   print("\nPrograma finalizado.")
except Exception as e:
   print(f"\nErro: {e}")