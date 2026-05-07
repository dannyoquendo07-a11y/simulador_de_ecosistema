from dataclasses import dataclass
import random

@dataclass
class Especies:
    nombre:str
    poblacion:int
    tasa_reproduccion:float
    tasa_mortalidad:float
    
    @property
    def poblacion(self):
        return self.poblacion
    @poblacion.setter
    def poblacion(self,valor):
        if valor<0:
            print(f"La especie: {self.nombre} se ha extinguido")
            self.poblacion=valor

    def actualizar(self,recursos_disponibles:float):
        nacimientos=self.poblacion*self.tasa_reproduccion*(recursos_disponibles/100)
        muertes=self.poblacion*self.tasa_mortalidad
        self.poblacion+=nacimientos-muertes
        
        if self.poblacion<0:
            self.poblacion=0
        self.poblacion=int(self.poblacion)

@dataclass
class Depredador(Especies):
    eficacia_caza:float
    hambre:float

    def cazar(self,presa):
        if presa.poblacion>0:
            capturas=self.poblacion*self.eficacia_caza
            if capturas>presa.poblacion:
                capturas=presa.poblacion
            presa.poblacion-=int(capturas)
            return capturas
        return 0
    
    def comer(self,presas_capturadas:int):
        self.hambre-=presas_capturadas

@dataclass
class Presa(Especies):
    resistencia:float
    camuflaje:float
    
    def intentar_huir(self)->bool:
        return random.random()<self.resistencia
    
    def comer(self,abundancia_recursos:float):
        if abundancia_recursos>50:
            self.poblacion+=int(self.poblacion*0.05)
    
    def buscar_refugio(self):
        self.tasa_mortalidad*=0.8
        print(f"La poblacion de: {self.nombre} se ha escondido")

@dataclass
class Entorno:
    vegetacion:float
    capacidad_comida:int
    humedad:float
    temperatura:float
    capacidad_especies:int

    def generar_vegetacion(self):
        crecimiento=self.temperatura*self.humedad
        self.vegetacion+=crecimiento
        print(f"Recursos generados a: {self.vegetacion}")
    
    def aplicar_clima(self):
        if self.temperatura>40 or self.temperatura<-5:
            print("Clima extremo detectado")
    
