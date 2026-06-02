from dataclasses import dataclass, field
import random
from typing import List
from excepciones import (ExcepcionDePoblacionInvalida,
                        ExcepcionDeEspecieExtinta,
                        ExcepcionDeRecursoInsuficiente,
                        ExcepcionDeEstadoRefugioInvalido)

@dataclass
class Entorno:
    vegetacion:float
    humedad:float
    temperatura:float
    clima:str
    dia_actual:int=0
    simulacion:bool=False
    especies:list['Especie']=field(default_factory=list)
    
    def __post_init__(self):
        if self.especies is None:
            self.especies = []
    
    def aplicar_clima(self):
        evento=random.random()
        if evento<0.15:
            self.clima="Lluvia"
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
        crecimiento=(self.temperatura*self.humedad)*0.05
        self.vegetacion=max(0.0,self.vegetacion+crecimiento)
        print(f"Vegetacion disponible: {self.vegetacion}")
    
    def avanzar_dia(self):
        self.dia_actual+=1   
        print(f"Dia: {self.dia_actual}")
        self.aplicar_clima()
        self.generar_vegetacion()

@dataclass
class Especie:
    nombre:str
    poblacion_inicial:int
    tasa_reproduccion:float=0.0
    tasa_mortalidad:float=0.0
    hambre:float=0.0
    
    def __post_init__(self):
        if self.poblacion_inicial<0:
            raise ExcepcionDePoblacionInvalida(f"La población inicial de: {self.nombre} no puede ser negativa")
        self._poblacion=self.poblacion_inicial

    @property
    def poblacion(self)->int:
        return self._poblacion
    @poblacion.setter
    def poblacion(self,valor:int):
        if valor<0:
            raise ExcepcionDePoblacionInvalida("No se puede asignar una población negativa.")
        self._poblacion=valor

    def actualizar(self,recursos_disponibles:float):
        if self.poblacion<=0:
            return
        self.hambre+=15
        tasa_mortalidad_efectiva=self.tasa_mortalidad
        if self.hambre>70:
            print(f"{self.nombre} esta sufriendo por hambre extrema")
            tasa_mortalidad_efectiva+=0.25
        factor_recursos = min(1.0, recursos_disponibles / 100)
        nacimientos=self.poblacion*self.tasa_reproduccion*factor_recursos
        muertes=self.poblacion*tasa_mortalidad_efectiva
        
        self.poblacion=int(self.poblacion+nacimientos-muertes)
        if self.poblacion==0:
            print(f"La especie esta extinguida")

@dataclass
class Presa(Especie):
    resistencia:float=0.0
    camuflaje:float=0.0
    escondido:bool=False
    
    def intentar_huir(self)->bool:
        if self.poblacion<=0:
            raise ExcepcionDeEspecieExtinta(f"La presa {self.nombre} está extinta y no puede huir.")
        self.hambre+=10
        return random.random()<self.resistencia
    
    def comer(self,abundancia_recursos:float):
        if abundancia_recursos>20:
            self.hambre=max(0.0,self.hambre-(abundancia_recursos*0.5))
        else:
            print("Hay escazes no se encontro comida")
            if self.hambre>80:
                raise ExcepcionDeEspecieExtinta(f"La presa {self.nombre} está extinta y no puede comer.")
    
    def buscar_refugio(self):
        if not self.escondido:
            self.escondido=True
            self.tasa_mortalidad*=0.8
            print(f"La poblacion de: {self.nombre} se ha escondido")
    
    def salir_de_refugio(self):
        if self.escondido:
            self.escondido=False
            self.tasa_mortalidad/=0.8
            print(f"{self.nombre} ha salido del refugio.")

@dataclass
class Depredador(Especie):
    eficacia_caza:float=0.0

    def cazar(self,presa:Especie,clima_actual:str):
        
        if self.poblacion<=0 or presa.poblacion<=0:
            return
        
        eficacia_caza_real=self.eficacia_caza
        if clima_actual=="Lluvia":
            eficacia_caza_real*=0.7
            print(f"La lluvia afecta la caza")
        capturas=self.poblacion*eficacia_caza_real
        if isinstance(presa,Presa) and presa.intentar_huir():
            capturas*=(1-presa.camuflaje)
            print("Caza fallida, presa escondida")
        if capturas>presa.poblacion:
            capturas=presa.poblacion
        presa.poblacion-=int(capturas)
        self.comer(int(capturas))
    
    def comer(self,presas_capturadas:int):
        por_depredador=presas_capturadas/max(1, self.poblacion)
        self.hambre=max(0.0,self.hambre-(por_depredador*50))
        print(f"Los depredadores cazaron {presas_capturadas}. \nHambre actual: {self.hambre}")
