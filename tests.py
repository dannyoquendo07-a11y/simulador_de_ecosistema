import unittest
from molde import Especie

class TestEspecies(unittest.TestCase):
    def test_inicializacion_poblacion(self):
        lobo=Especie("Lobo",50,0.1,0.05)
        self.assertEqual(lobo.poblacion,50)
    
    def test_poblacion_no_negativa(self):
        conejo=Especie("Conejo",10,0.2,0.1)
        conejo.poblacion=-10
        self.assertEqual(conejo.poblacion, 0)


class EcosistemaTests(unittest.TestCase):

    def test_comer_vegetacion(self):
        # que un herviboro pueda comer vegetacion

        # crear un herviboro

        # crear la vegetacion

        # probar la interaccion
        ...

    def test_carnivoro_vegetacion(self):
        #
        #
        #
        #
        ...
if __name__ == "__main__":
    unittest.main()