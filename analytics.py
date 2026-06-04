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
    
    df=pd.DataFrame(datos_crudos)
    print("RESUMEN ESTADISTICO")
    print(df.describe())
    print("TABLA DE EVOLUCION")
    print(df.to_string(index=False))
    
    plt.figure(figsize=(10,6))
    plt.plot(df["Día"],df["Conejos"],label="Conejos(Presas)",color="pink",linewidth=2.5,marker="o")
    plt.plot(df["Día"],df["Zorros"],label="Zorros(Depredadores)",color="orange",linewidth=2.5,marker="s")
    plt.plot(df["Día"],df["Vegetación"],label="Vegetación",color="green",linestyle="--")

    plt.title("Evolución Temporal del Ecosistema",fontsize=14,fontweight='bold')
    plt.xlabel("Días",fontsize=12)
    plt.ylabel("Población / Recursos",fontsize=12)

    plt.grid(True,linestyle=":",alpha=0.6)
    plt.legend(fontsize=11)
    