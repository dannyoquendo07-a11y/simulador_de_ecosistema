from molde import Entorno, Presa, Depredador

class SimuladorEcosistema:
    def __init__(self,entorno:Entorno,presa:Presa,depredador:Depredador):
        self.entorno=entorno
        self.presa=presa
        self.depredador=depredador
    
    def ejecutar(self,dias:int):
        for avance in range(dias):
            self.entorno.avanzar_dia()
            if self.presa.poblacion<=0 and self.depredador.poblacion<=0:
                print("Ecosistema colapsado. Fin del mundo")
                break