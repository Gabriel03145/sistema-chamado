import sqlite3
from pathlib import Path
from models import Chamado

DB_PATH = Path(__file__).parent / 'chamados.db'

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    with conectar() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS chamados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                status TEXT DEFAULT 'aberto',
                prioridade TEXT DEFAULT 'média',
                data_chamado TEXT
            )
        ''')

def inserir(chamado):
    with conectar() as conn:
        conn.execute(
            'INSERT INTO chamados (titulo, descricao, prioridade, status, data_chamado) VALUES (?, ?, ?, ?, ?)',
            (chamado.titulo, chamado.descricao, chamado.prioridade, chamado.status, chamado.data_chamado)
        )

def listar():
    with conectar() as conn:
        linhas = conn.execute('SELECT id, titulo, descricao, prioridade, status, data_chamado FROM chamados').fetchall()
    return [Chamado(titulo=i[1], descricao=i[2], prioridade=i[3], status=i[4], id=i[0], data_chamado=i[5]) for i in linhas]

def buscar_id(id):
    with conectar() as conn:
        linha = conn.execute(
            'SELECT id, titulo, descricao, prioridade, status, data_chamado FROM chamados WHERE id = ?', (id, )
        ).fetchone()
    if linha is None:
        return None
    id, titulo, descricao, prioridade, status, data_chamado = linha
    return Chamado(titulo=titulo, descricao=descricao, prioridade=prioridade, status=status, id=id, data_chamado=data_chamado)

def fechar(id):
    with conectar() as conn:
        conn.execute("UPDATE chamados SET status = 'fechado' WHERE id = ?", (id,))