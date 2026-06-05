#variables 
from molde import Entorno,Presa,Depredador
#se me señalo hoy con los preparadores que para entender mejor el manejo de la instancia en 
# el main con las clases creara este settings y manejara los datos como 'variables'
TASA_NATALIDAD_CONEJOS=0.30  #0.30 representa un incremento del 30% 
TASA_MORTALIDAD_CONEJOS=0.10 
PROB_SOBREVIVIR_CLIMA_CONEJOS=0.40
FACTOR_OCULTAMIENTO_CONEJOS=0.20

TASA_NATALIDAD_ZORROS=0.15
TASA_MORTALIDAD_ZORROS=0.08
PROB_EXITO_CAZA_ZORROS=0.25

ecosistema_bosque=Entorno(vegetacion=120.0, 
    humedad=50.0,
    temperatura=24.0,
    clima="Soleado")
conejos=Presa(nombre="Conejos",
    poblacion_inicial=10, 
    tasa_reproduccion=TASA_NATALIDAD_CONEJOS,
    tasa_mortalidad=TASA_MORTALIDAD_CONEJOS,
    resistencia=PROB_SOBREVIVIR_CLIMA_CONEJOS,
    camuflaje=FACTOR_OCULTAMIENTO_CONEJOS)
zorros=Depredador(nombre="Zorros",
    poblacion_inicial=15,
    tasa_reproduccion=TASA_NATALIDAD_ZORROS,
    tasa_mortalidad=TASA_MORTALIDAD_ZORROS,
    eficacia_caza=PROB_EXITO_CAZA_ZORROS)