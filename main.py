from molde import Entorno, Presa, Depredador
from excepciones import (ExcepcionDePoblacionInvalida,
                        ExcepcionDeEspecieExtinta,
                        ExcepcionDeRecursoInsuficiente,
                        ExcepcionDeEstadoRefugioInvalido)

class SimuladorEcosistema:
    def __init__(self,entorno:Entorno,presa:Presa,depredador:Depredador):
        self.entorno=entorno
        self.presa=presa
        self.depredador=depredador
        self.historial_datos=[]
    
    def ejecutar(self,dias:int):
        for avance in range(dias):
            try:
                self.entorno.avanzar_dia()
                #comportamiento de la presa
                if self.entorno.clima=="Lluvia" and not self.presa.escondido:
                    self.presa.buscar_refugio()
                elif self.entorno.clima=="Soleado" and self.presa.escondido:
                    self.presa.salir_de_refugio()
                #alimentacion de las presas
                if self.presa.poblacion>0:
                    self.presa.comer(self.entorno.vegetacion)
                #caza de deprepadores
                if self.depredador.poblacion > 0 and self.presa.poblacion > 0:
                    self.depredador.cazar(self.presa, self.entorno.clima)
                #ciclo de vida
                if self.presa.poblacion>0:
                    self.presa.actualizar(recursos_disponibles=self.entorno.vegetacion)
                if self.depredador.poblacion>0:
                    self.depredador.actualizar(recursos_disponibles=self.presa.poblacion)
                    print(f"Fin del Día {self.entorno.dia_actual} \n{self.presa.nombre}: {self.presa.poblacion} \n{self.depredador.nombre}: {self.depredador.poblacion}")
                self.historial_datos.append({
                    "Día": self.entorno.dia_actual,
                    "Vegetación": self.entorno.vegetacion,
                    "Conejos": max(0, self.presa.poblacion),
                    "Zorros": max(0, self.depredador.poblacion)
                })
                #evaluacion de colapso
                if self.presa.poblacion<=0 and self.depredador.poblacion<=0:
                    print("Ecosistema colapsado. Fin del mundo")
                    break
                elif self.presa.poblacion<=0:
                    print(f"Presas extintas, los depredadores pronto moriran de hambre")
                    break
            except ExcepcionDeRecursoInsuficiente as e:
                print(f"Alerta ambiental: {e}, la escasez afectara el proximo dia")
                break
            except ExcepcionDeEspecieExtinta as e:
                print(f"Fin de la simulacion: {e}")
                break
            except ExcepcionDeEstadoRefugioInvalido as e:
                print(f"Error en refugio: {e}")
                #no detiene la simulacion
            except ExcepcionDePoblacionInvalida as e:
                print(f"Error critico de poblacion: {e}")
                break

if __name__ == "__main__":
    from settings import ecosistema_bosque,conejos,zorros
    simulador=SimuladorEcosistema(entorno=ecosistema_bosque,presa=conejos,depredador=zorros)
    simulador.ejecutar(1)