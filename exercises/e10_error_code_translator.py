"""
Exercicio 10: Tradutor de Codigos de Erro (Dict)

Objetivo:
Consultar e atualizar um dicionario de codigos de erro.

Enunciado:
1. Crie um dicionario fixo com 5 codigos de erro de servidor
   (ex: 404: "Not Found", 500: "Internal Server Error").
2. Peca ao usuario um codigo.
3. Se o codigo existir, exiba a mensagem.
4. Se nao existir, use um metodo do dicionario para retornar
   "Codigo de erro desconhecido".
5. Adicione esse novo codigo ao dicionario com uma mensagem padrao definida pelo usuario.
"""
import json
from pathlib import Path
from shared.text import normalize_text_without_accents_and_special_chars

def load_or_create_json(file_path: str, default_data: dict) -> dict:
      path = Path(file_path)
      
      if not path.exists():
         path.write_text(
            json.dumps(default_data, ensure_ascii=False, indent=2), 
            encoding="utf-8",
         )
         return default_data

      with path.open("r", encoding="utf-8") as file:
         return json.load(file)

def save_json(file_path: str, data: dict) -> dict:
   path = Path(file_path)

   with path.open("w", encoding="utf-8") as file:
      json.dump(data, file, ensure_ascii=False, indent=2)

   return data


try:
   print("---| Tradutor de Códigos de Erro |---\n")

   # Constants / Configuration
   FILE_PATH = "know_errors.json"
   
   NEW_ERROR_FOUND = "Código de erro desconhecido"

   # Variables
   know_errors = {
        "400": "Bad Request",
        "401": "Unauthorized",
        "403": "Forbidden",
        "404": "Not Found",
        "500": "Internal Server Error"
   }

   know_errors = load_or_create_json(FILE_PATH, know_errors)

   # Inputs
   raw_error_code = input("Informe o código do erro apresentado com 3 dígitos 100 e 599: ")

   # Sanitization
   error_code = normalize_text_without_accents_and_special_chars(raw_error_code)

   # Validation
   try:
      error_code_number = int(error_code)
   except ValueError:
      raise ValueError("Deve ser informado um número de erro (ex.: 400, 401, 500, ...)")

   if not (error_code_number >= 100 and error_code_number <= 599):
      raise ValueError("Deve ser informado um valor entre 100 e 599")
   
   error_description_found = know_errors.get(error_code, None)

   # Business Rules
   if error_description_found is None:
      print(NEW_ERROR_FOUND)
      raw_new_description = input(f"Informe uma mensagem padrão para o erro {error_code}: ")
      new_description = raw_new_description.strip()

      if not new_description:
         raise ValueError("Não é possível inserir uma descrição vazia")
      else:
         know_errors[error_code] = new_description
         save_json(FILE_PATH, know_errors)

         print(f"Erro cadastrado com sucesso: {error_code} - {new_description}")

   else:
      print(f"Erro: {error_code} - {error_description_found}")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")
