import unittest
from molde import Especie,Presa,Depredador

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

    def test_extincion(self):
        dodo=Especie("Dodo",0,0.5,0.1)
        dodo.actualizar(recursos_disponibles=100)
        self.assertEqual(dodo.poblacion,0)

class EcosistemaTests(unittest.TestCase):

    def test_comer_vegetacion(self):
        # que un herviboro pueda comer vegetacion

        # crear un herviboro
        conejo=Presa(nombre="Conejo", poblacion_inicial=20, tasa_reproduccion=0.3, tasa_mortalidad=0.1, resistencia=0.5, camuflaje=0.2)
        conejo.hambre=50.0
        # crear la vegetacion
        vegetacion_disponible = 100.0
        # probar la interaccion
        conejo.comer(vegetacion_disponible)
        self.assertEqual(conejo.hambre, 0.0) # El hambre baja de 50.0 a 0.0

    def test_carnivoro_vegetacion(self):
        lobo=Depredador(nombre="Lobo", poblacion_inicial=5, tasa_reproduccion=0.1, tasa_mortalidad=0.05, eficacia_caza=1.0)
        lobo.hambre=40.0
        vegetacion_disponible=100.0
        if hasattr(lobo,'comer_vegetacion'): 
            lobo.comer_vegetacion(vegetacion_disponible)
        self.assertEqual(lobo.hambre,40.0)

    def test_caza_carnivoro(self):
        lobo = Depredador(nombre="Lobo", poblacion_inicial=10, tasa_reproduccion=0.0, tasa_mortalidad=0.0, eficacia_caza=1.5)
        conejo = Presa(nombre="Conejo", poblacion_inicial=40, tasa_reproduccion=0.0, tasa_mortalidad=0.0, resistencia=0.0, camuflaje=0.0)
        lobo.cazar(conejo, clima_actual="Soleado")
        self.assertEqual(conejo.poblacion, 25)
    
    def test_clima_lluvia_reduce_caza(self):
        lobo = Depredador(nombre="Lobo",poblacion_inicial=10,eficacia_caza=1.0)
        conejo = Presa(nombre="Conejo",poblacion_inicial=30,resistencia=0.0,camuflaje=0.0)
        lobo.cazar(conejo,clima_actual="Lluvia")
        self.assertEqual(conejo.poblacion,23)
    
    def test_buscar_refugio(self):
        conejo=Presa(nombre="Conejo",poblacion_inicial=10,tasa_reproduccion=0.0,tasa_mortalidad=0.5,resistencia=0.0,camuflaje=0.0)
        conejo.buscar_refugio()
        self.assertTrue(conejo.escondido)
        self.assertAlmostEqual(conejo.tasa_mortalidad,0.4)

    def test_salir_de_refugio(self):
        conejo = Presa(nombre="Conejo",poblacion_inicial=10,tasa_reproduccion=0.0,tasa_mortalidad=0.4,resistencia=0.0,camuflaje=0.0)
        conejo.escondido=True
        conejo.salir_de_refugio()
        self.assertFalse(conejo.escondido)
        self.assertAlmostEqual(conejo.tasa_mortalidad,0.5)


if __name__ == "__main__":
    unittest.main()