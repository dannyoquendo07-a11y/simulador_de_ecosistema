from dataclasses import dataclass
import random

@dataclass
class Especie:
    nombre:str
    poblacion_inicial:int
    tasa_reproduccion:float
    tasa_mortalidad:float
    
    def __post_init__(self):
        self._poblacion=self.poblacion_inicial

    @property
    def poblacion(self)->int:
        return self._poblacion
    @poblacion.setter
    def poblacion(self,valor:int):
        if valor<0:
            print(f"La especie: '{self.nombre}' se ha extinguido")
            self._poblacion=valor

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
    humedad:float
    temperatura:float
    dia_actual=int=0
    clima=str
    simulacion=False

    def aplicar_clima(self):
        evento=random.random()
        if evento<0.15:
            self.clima="LLuvia"
            self.humedad=min(100,self.humedad+20)
            self.temperatura-=5
            self.vegetacion*=1.1
        elif evento<0.25:
            self.clima="Sequia"
            self.humedad=max(0,self.humedad-15)
            self.temperatura+=8
            self.vegetacion*=0.8
        else:
            self.clima="Soleado"
            self.humedad=max(10,self.humedad-2)
        print(f"Estado del clima: {self.clima}\nTemperatura: {self.temperatura}°C\nHumedad: {self.humedad}%")

    def generar_vegetacion(self):
        crecimiento=self.temperatura*self.humedad
        self.vegetacion+=crecimiento
        print(f"Recursos generados a: {self.vegetacion}")
    
    def avanzar_dia(self):
        self.dia_actual+=1   
        print(f"Dia: {self.dia_actual}")