import unittest
from models import Chamado

class TestChamado(unittest.TestCase):

    def test_criar_chamado(self):
        chamado = Chamado(
            titulo="computador não liga",
            descricao="o computador não liga ao pressionar o botão",
            prioridade="alta"
        )

        self.assertEqual(chamado.titulo, "computador não liga")
        self.assertEqual(chamado.descricao, "o computador não liga ao pressionar o botão")
        self.assertEqual(chamado.prioridade, "alta")
        self.assertEqual(chamado.status, "aberto")

    def test_fechar_chamado(self):
        chamado = Chamado(
            titulo="problema de internet",
            descricao="sem conexão com a internet"
        )

        chamado.fechar()

        self.assertEqual(chamado.status, "fechado")

if __name__ == "__main__":
    unittest.main()