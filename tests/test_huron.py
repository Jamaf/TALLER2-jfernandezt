import unittest
from huron import Huron

class TestHuron(unittest.TestCase):

    def setUp(self):
        self.my_huron = Huron('Buck', 3.5, 4, 'Brazil', 20.0)    

    def test_hacer_sonido(self):
        self.assertEqual(self.my_huron.hacer_sonido(), '¡Eek Eek!.')

    def test_calcular_flete(self):
        self.assertEqual(self.my_huron.calcular_flete(), 70)

if __name__ == '__main__':
    unittest.main()