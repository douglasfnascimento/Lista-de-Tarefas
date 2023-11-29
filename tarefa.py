class Tarefa:
    def __init__(self, descricao, status='Não Concluída', data_vencimento=None):
        self.descricao = descricao
        self.status = status
        self.data_vencimento = data_vencimento

