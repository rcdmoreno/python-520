
import unittest
import requests


def get_endereco(cep):
    return requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()

class TestGeEndereco(unittest.TestCase):

    def test_get_endereco(self):
        cep = '04942050'
        resposta = get_endereco(cep)
        self.assertEqual(
            resposta['logradouro'], 'Rua João Ribeiro Peixoto'
        )

if __name__ == '__main__':
    unittest.main()