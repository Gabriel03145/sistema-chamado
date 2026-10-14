# Sistema de Chamados (Help Desk)

Sistema de chamados em terminal, feito em Python com POO e SQLite.
Simula o registro e o acompanhamento de chamados de suporte técnico.

## Tecnologias
Python 3 · SQLite · POO

## Funcionalidades
- Abrir chamado
- Listar chamados
- Buscar chamado por ID
- Fechar chamado (o chamado não é apagado, só muda o status)

## Como rodar
```bash
git clone https://github.com/Gabriel03145/sistema_chamado
cd sistema_chamado
python main.py
```

## Prints
### Menu principal
![Menu](prints/menu.png)

### Abrindo um chamado
![Abrir](prints/abrir.png)

### Listando chamados
![Listar](prints/listar.png)

### Fechando um chamado
![Fechar](prints/fechar.png)

### Tratamento de erro (ID inválido)
![Erro](prints/erro_id.png)

## Estrutura
- `main.py`: menu e fluxo do programa
- `models.py`: classe `Chamado`
- `database.py`: comandos SQL

## Próximos passos
- Prioridade e data de abertura
- Testes com pytest
- API com FastAPI