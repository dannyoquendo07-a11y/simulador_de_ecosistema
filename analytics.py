""" Recibi un consejo de los preparadores que en lugar de ver muñequitos moviéndose, 
transformara la simulación en un laboratorio que muestra graficos con las curvas de poblacion. Esto usando
la libreria pandas y matplotlib. Referencias: - https://pandas.pydata.org/docs/reference/index.html 
- https://www.tutorialesprogramacionya.com/cienciadedatos/matplotlib/tema9.html"""

import pandas as pd
import matplotlib.pyplot as plt
from main import SimuladorEcosistema
from molde import Entorno, Presa, Depredador

def generar_reporte(dias_simulacion=1):
    ecosistema_bosque=Entorno(vegetacion=150.0,humedad=50.0,temperatura=24.0,clima="Soleado")
    conejos=Presa(nombre="Conejos",poblacion_inicial=80,tasa_reproduccion=0.3,tasa_mortalidad=0.1,resistencia=0.4,camuflaje=0.2)
    zorros=Depredador(nombre="Zorros",poblacion_inicial=15,tasa_reproduccion=0.15,tasa_mortalidad=0.08,eficacia_caza=0.25)
    
    simulador=SimuladorEcosistema(entorno=ecosistema_bosque,presa=conejos,depredador=zorros)
    datos_crudos=simulador.ejecutar(dias=dias_simulacion)
    
    if not datos_crudos:
        print("Error: La simulacion no guardo datos en el dia 1")
        return
    
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

    plt.show()

if __name__ == "__main__":
    generar_reporte(dias_simulacion=1)