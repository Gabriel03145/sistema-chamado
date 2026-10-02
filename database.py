import sqlite3
from models import Chamado

def conectar():
    return sqlite3.connect('chamados.db')

def criar_tabela():
    with conectar() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS chamados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                status TEXT DEFAULT 'aberto' 
            )
        ''')

def inserir(chamado):
    with conectar() as conn:
        conn.execute(
            'INSERT INTO chamados (titulo, descricao, status) VALUES (?, ?, ?)',
            (chamado.titulo, chamado.descricao, chamado.status)
        )

def listar():
    with conectar() as conn:
        linhas = conn.execute('SELECT id, titulo, descricao, status FROM chamados').fetchall()
    return [Chamado(i[1], i[2], i[3], i[0]) for i in linhas]

def fechar(id):
    with conectar() as conn:
        conn.execute("UPDATE chamados SET status = 'fechado' WHERE id = ?", (id,))