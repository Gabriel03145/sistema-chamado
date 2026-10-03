from datetime import datetime

class Chamado:
    def __init__(self, titulo, descricao, prioridade='média', status='aberto', id=None, data_chamado=None):
        self._prioridade = prioridade
        self._data_chamado = data_chamado or datetime.now().strftime('%d/%m/%Y %H:%M')
        self._titulo = titulo
        self._descricao = descricao
        self._status = status
        self._id = id

    def __str__(self):
        return f'#{self.id} [status:{self.status}] titulo: {self.titulo} | prioridade: {self.prioridade} | {self.data_chamado}'


    @property
    def titulo(self):
        return self._titulo

    @property
    def descricao(self):
        return self._descricao

    @property
    def prioridade(self):
        return self._prioridade

    @property
    def status(self):
        return self._status

    @property
    def id(self):
        return self._id

    @property
    def data_chamado(self):
        return self._data_chamado

    def fechar(self):
        self._status = 'fechado'