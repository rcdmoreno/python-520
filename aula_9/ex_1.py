
import unittest

def calcular_media(lista):
    return sum(lista) / len(lista)

class CalcularMediaTestCase(unittest.TestCase):

    def test_calcular_media(self):
        lista = [1,1,1,1,1]
        media = calcular_media(lista)
        self.assertEqual(1, media)
    
    def test_calcular_lista_vazia(self):
        lista_vazia = []
        with self.assertRaises(ZeroDivisionError):
            calcular_media(lista_vazia)


if __name__ == '__main__':
    #calcular_media([])
    unittest.main()
