""" Recibi un consejo de los preparadores que en lugar de ver muñequitos moviéndose, 
transformara la simulación en un laboratorio que muestra graficos con las curvas de poblacion. Esto usando
la libreria pandas y matplotlib. Referencias: - https://pandas.pydata.org/docs/reference/index.html 
- https://www.tutorialesprogramacionya.com/cienciadedatos/matplotlib/tema9.html"""

import pandas as pd
import matplotlib.pyplot as plt
from main import SimuladorEcosistema
from settings import ecosistema_bosque,conejos,zorros

def generar_reporte(dias_simulacion=1):
    simulador=SimuladorEcosistema(entorno=ecosistema_bosque,presa=conejos,depredador=zorros)
    datos_crudos=simulador.ejecutar(dias=dias_simulacion)
