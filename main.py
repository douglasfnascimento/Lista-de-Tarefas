import datetime
from todolist import ToDoList

# Função para exibir o menu
def exibir_menu():
    print("\n===== Menu =====")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Filtrar Tarefas")
    print("5. Marcar Tarefa como Concluída")
    print("6. Sair")

if __name__ == "__main__":
    lista_de_tarefas = ToDoList()

    while True:
        exibir_menu()

        escolha = input("\nDigite o número referente à opção desejada: ")

        if escolha == '1':
            descricao = input("Descreva sua tarefa: ")
            data_vencimento_str = input("Você deseja definir uma data de vencimento para a tarefa? Caso sim, digite-a no formato DD/MM/YYYY; caso não, apenas digite Enter/Return: ")
            data_vencimento = datetime.datetime.strptime(data_vencimento_str, "%d/%m/%Y").date() if data_vencimento_str else None
            lista_de_tarefas.adicionar_tarefa(descricao, data_vencimento)
        elif escolha == '2':
            lista_de_tarefas.listar_tarefas()
        elif escolha == '3':
            lista_de_tarefas.remover_tarefa()
        elif escolha == '4':
            status_filtro = input("Digite [1] para mostrar apenas as tarefas Concluídas e [2] para mostrar as Não Concluídas: ")
            if status_filtro == '1':
                lista_de_tarefas.listar_tarefas(status='Concluída')
            elif status_filtro == '2':
                lista_de_tarefas.listar_tarefas(status='Não Concluída')
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        elif escolha == '5':
            lista_de_tarefas.marcar_como_concluida()
        elif escolha == '6':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

