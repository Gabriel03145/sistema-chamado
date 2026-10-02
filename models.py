class Chamado:
    def __init__(self, titulo, descricao, status='aberto', id=None):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id = id

    def __str__(self):
        return f'#{self.id} [status:{self.status}] titulo: {self.titulo}'