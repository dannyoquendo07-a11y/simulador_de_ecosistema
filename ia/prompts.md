#yo
revisa y corrige errores en:  
    especies=list=None

    def __post_init__(self):
        if self.especies is None:
            self.especies = []
#ia
# Usamos field(default_factory=list) para inicializar listas vacías en dataclasses
    especies: List['Especie'] = field(default_factory=list)