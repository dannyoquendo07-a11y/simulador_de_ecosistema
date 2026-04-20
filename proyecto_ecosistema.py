class Especies:
    def __init__(self,nombre,poblacion,tasa_reproduccion,tasa_mortalidad):
        self.nombre=nombre
        self.poblacion=poblacion
        self.tasa_reproduccion=tasa_reproduccion
        self.tasa_mortalidad=tasa_mortalidad
    
    def actualizar(self,recursos_disponibles):
        nacimientos=self.poblacion*self.tasa_reproduccion*(recursos_disponibles/100)
       
        muertes=self.poblacion*self.tasa_mortalidad
        
        self.poblacion+=nacimientos-muertes
       
        if self.poblacion<0:
            self.poblacion=0
        self.poblacion=int(self.poblacion)

class Depredador(Especies):
    def __init__(self,nombre,poblacion,tasa_reproduccion,tasa_mortalidad,eficacia_caza):
        super().__init__(nombre,poblacion,tasa_reproduccion,tasa_mortalidad)
        self.eficacia_caza=eficacia_caza
    def cazar(self,presa):
        if presa.poblacion>0:
            capturas=self.poblacion*self.eficacia_caza
            if capturas>presa.poblacion:
                capturas=presa.poblacion
            presa.poblacion-=capturas
            return capturas
        return 0
    def actualizar_depredador(self,presas_capturadas):
        hambre=presas_capturadas
class Presa(Especies):
    def __init__(self,nombre,poblacion,tasa_reproduccion,tasa_mortalidad,resistencia):
        super().__init__(nombre,poblacion,tasa_reproduccion,tasa_mortalidad)
        self.resistencia=resistencia
    def 