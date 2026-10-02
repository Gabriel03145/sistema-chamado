import database
from models import Chamado

def menu():
    database.criar_tabela()

    while True:
        print('\n1 - Abrir chamado\n2 - Listar\n3 - Fechar\n4 - buscar ID\n0 - sair')
        op = input('Opção: ')

        if op == '1':
            titulo = input('Título: ')
            desc = input('Descrição: ')
            database.inserir(Chamado(titulo, desc))

        elif op == '2':
            for c in database.listar():
                print(c)

        elif op == '3':
            try:
                database.fechar(int(input('ID: ')))
            except ValueError:
                print('Digite um número válido')

        elif op == '4':
            try:
                chamado_id = int(input('id: '))
                chamado = database.buscar_id(chamado_id)
                if chamado is None:
                    print('ID inexistente')
                else:
                    print(chamado)
            except ValueError:
                print('Digite um valor válido')

        elif op == '0':
            break
        else:
            print('opção inválida')

if __name__ == '__main__':
    menu()