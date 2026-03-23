"""
MAIN HUB - FirstExerciseList
Menu central que executa os ficheiros externos apenas quando solicitado.
------------------------------------------------------------------
"""
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    try:
        # Caminho do interpretador python atual para garantir que funciona em qualquer PC
        python_cmd = sys.executable
        base_dir = os.path.dirname(os.path.abspath(__file__))

        while True:
            clear_screen()
            print("=" * 40)
            print(f"{' MENU DE EXERCÍCIOS ' : ^40}")
            print("=" * 40)
            print("1. Gerenciador de Lista de Tarefas")
            print("2. Login com Tupla")
            print("3. Verificador de Clube")
            print("4. Classificador de Notas")
            print("5. Protocolo Sentinela de Dados")
            print("6. Sistema de Inventário Único")
            print("7. Frequência de Palavras")
            print("8. Registro Imutável de Notas")
            print("9. Otimizador de Rotas de Entrega")
            print("10. Tradutor de Códigos de Erro")
            print("11. Gestão de Candidatos")
            print("12. Histórico de Flutuação de Preços")
            print("13. Agrupamento por Categorias")
            print("14. Validador de Tupla e Set")
            print("15. Ranking de Pontuações")
            print("-" * 40)
            print("0. SAIR")
            print("-" * 40)

            choice = input("Escolha uma opção para 'brincar': ").strip()

            # Dicionário que mapeia a escolha ao nome do ficheiro real na tua pasta
            scripts = {
                "1": "e01_task_list_manager.py",
                "2": "e02_login_with_tuple.py",
                "3": "e03_vip_club_checker.py",
                "4": "e04_grade_classifier_dict.py",
                "5": "e05_data_sentinel_protocol.py",
                "6": "e06_unique_inventory_system.py",
                "7": "e07_word_frequency_dictionary.py",
                "8": "e08_immutable_grade_record.py",
                "9": "e09_delivery_route_optimizer.py",
                "10": "e10_error_code_translator.py",
                "11": "e11_candidate_management.py",
                "12": "e12_price_history_fluctuation.py",
                "13": "e13_category_grouping.py",
                "14": "e14_tuple_set_validator.py",
                "15": "e15_score_ranking.py",
            }

            if choice == "0":
                print("Programa finalizado... Até à próxima!")
                break
            
            elif choice in scripts:
                print(f"\n--- EXECUTANDO: {scripts[choice]} ---\n")
                # Executa o ficheiro como um processo separado
                script_path = os.path.join(base_dir, "exercises", scripts[choice])
                os.system(f'"{python_cmd}" "{script_path}"')
                print("\n" + "-" * 40)
                input("\nExercício terminado. Pressione ENTER para voltar ao menu...")
            
            else:
                print("Opção inválida! Tente novamente.")
                input("\nPressione ENTER...")

    except KeyboardInterrupt:
        print("\nPrograma finalizado... Até à próxima!")
    
    except Exception as e:
        print(f"\nErro: {e}!")

if __name__ == "__main__":
    main()
