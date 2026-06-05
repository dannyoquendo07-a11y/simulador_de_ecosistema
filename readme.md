# observaciones

- documentacion: diagramas, texto.

ARCHIVOS:
'molde.py': Es el nucleo del sistema, contiene las clases Entorno, Presa y Depredador que definen el comportamiento esencial del proyecto
'main.py': es el motor de la simulacion, controla los ciclos diarios y evalua las condiciones limites de colapso
'settings.py': funciona para inicializar los parametros del ecosistema y facilitar la mutacion de poblaciones iniciales o climas en un unico archivo
'excepciones.py': define los errores encargados de alterar eventos ciriticos en el entorno
'tests.py': coloca pruebas para ver el comportamiento del ecosistema a borde y aegura la tolerancia de ellas
'analytics.py': Recibe los datos resultantes del main y los trasnforma en estructuras tabulares gracias a pandas y se visualiza esta curva en una ventana grafica de matplotlib
'prompts.md': almacena bitacoras del desarrollo del proyecto junto a la ia

DIAGRAMA DE LAS CLASES:
Las clases Presa y Depredador heredan directamente de la clase base Especie, reutilizando atributos comunes (nombre, poblacion, hambre) y sus metodos de ciclo de vida (actualizar). 
Se utiliza @property y @poblacion.setter para proteger la variable interna _poblacion asi se impide la asignación erronea (como poblaciones negativas) y arrojan excepciones personalizadas.
Aunque ambas especies comen, Presa consume directamente la variable vegetacion del Entorno, mientras que Depredador usa el metodo comer() basado en las presas capturadas.

- sincerar las intenciones
No diseñe el programa como un videojuego recreativo ni posee interfaz grafica, el proposito es que sirva como una herramienta de simulación computacional para observar como variables (clima, tasas de reproducción, mortalidad y escasez) afectan la estabilidad biologica a lo largo del tiempo.

- si usas paquetes externos, como configurar el entorno virtual

1. Crear el entorno
python -m venv venv
2. Activar el entorno
.\venv\Scripts\Activate.ps1
3. Instalar los paquetes
pip install pandas matplotlib
4. Ejecutar
python analytics.py

- no hacer un espaguetti ( no combinar parte grafica con parte logica )