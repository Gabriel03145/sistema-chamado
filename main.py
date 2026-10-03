import database
from models import Chamado

def menu():
    database.criar_tabela()

    while True:
        print('\n1 - Abrir chamado\n2 - Listar\n3 - Fechar\n4 - buscar ID\n0 - sair')
        op = input('Opção: ')

        if op == '1':
            titulo = (input('Título: ')).strip()
            desc = (input('Descrição: ')).strip()
            prioridade = (input('Prioridade(baixa/média/alta): ')).lower().strip()
            if titulo == '' or desc == '':
                print('título/descrição em branco.')
            elif prioridade not in ('baixa', 'média', 'alta'):
                print('prioridade inválida')
            else:
                database.inserir(Chamado(titulo, desc, prioridade))
                print('requisito de chamado realizado')

        elif op == '2':
            chamado = database.listar()
            if not chamado:
                print('nenhum cadastro encontrado')
            else:
                for c in chamado:
                    print(c)

        elif op == '3':
            try:
                chamado_id = (int(input('ID: ')))
                chamado = database.buscar_id(chamado_id)
                if chamado is None:
                    print('ID inexistente')
                elif chamado.status == 'fechado':
                    print('chamado já está fechado')
                else:
                    database.fechar(chamado_id)
                    print('chamado fechado')
            except ValueError:
                print('digite um valor válido')

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