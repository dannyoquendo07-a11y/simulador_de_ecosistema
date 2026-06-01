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
    
    def test_hambre_extrema_aumente_mortalidad(self):
        """Verifica que si el hambre supera 70 la mortalidad aumente y mueran mas"""
        #Especie con hambre normal '0'
        ciervo_sano = Especie("Ciervo Sano", 100, tasa_reproduccion=0.0, tasa_mortalidad=0.1)
        ciervo_sano.actualizar(recursos_disponibles=100)
        #Muertes esperadas:100*0.1=10. Quedan 90
        
        #Especie con hambre extrema '80'
        ciervo_hambriento = Especie("Ciervo Hambriento", 100, tasa_reproduccion=0.0, tasa_mortalidad=0.1)
        ciervo_hambriento.hambre = 80.0
        ciervo_hambriento.actualizar(recursos_disponibles=100)
        #Muertes esperadas:100*(0.1+0.25)=35. Quedan 65
        
        self.assertEqual(ciervo_sano.poblacion, 90)
        self.assertEqual(ciervo_hambriento.poblacion, 65)

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