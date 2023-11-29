import datetime
from tarefa import Tarefa

class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, data_vencimento=None):
        nova_tarefa = Tarefa(descricao, data_vencimento=data_vencimento)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self, status=None):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if not status or tarefa.status.lower() == status.lower()]
        for idx, tarefa in enumerate(tarefas_filtradas, start=1):
            print(f"{idx}. {tarefa.descricao} | {tarefa.status}")
            if tarefa.data_vencimento:
                data_formatada = tarefa.data_vencimento.strftime("%d/%m/%Y")
                print(f"   Data de Vencimento: {data_formatada}")
            print()
        return tarefas_filtradas

    def remover_tarefa(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        print("\nLista de Tarefas:")
        for idx, tarefa in enumerate(self.tarefas, start=1):
            print(f"{idx}. {tarefa.descricao} | {tarefa.status}")
            if tarefa.data_vencimento:
                data_formatada = tarefa.data_vencimento.strftime("%d/%m/%Y")
                print(f"   Data de Vencimento: {data_formatada}")
            print()

        indice = int(input("\nDigite o número referente à tarefa que você deseja remover: "))

        if 1 <= indice <= len(self.tarefas):
            del self.tarefas[indice - 1]
            print("Tarefa removida com sucesso.")
        else:
            print("O número digitado não corresponde a nenhuma tarefa cadastrada.")

    def filtrar_tarefas_nao_concluidas(self):
        return [idx + 1 for idx, tarefa in enumerate(self.tarefas) if tarefa.status.lower() == 'não concluída']

    def filtrar_tarefas_concluidas(self):
        return [idx + 1 for idx, tarefa in enumerate(self.tarefas) if tarefa.status.lower() == 'concluída']

    def marcar_como_concluida(self):
        tarefas_nao_concluidas = self.filtrar_tarefas_nao_concluidas()

        if not tarefas_nao_concluidas:
            print("Não há tarefas não concluídas para marcar.")
            return

        print("\nTarefas não concluídas:")
        for idx in tarefas_nao_concluidas:
            print(f"{idx}. {self.tarefas[idx - 1].descricao}")

        escolha = int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))

        if escolha in tarefas_nao_concluidas:
            self.tarefas[escolha - 1].status = 'Concluída'
            print("Tarefa marcada como concluída com sucesso.")
        else:
            print("Número de tarefa inválido.")

