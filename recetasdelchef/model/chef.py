from enum import StrEnum


class UnidadMedida(StrEnum):
    GRAMO = "gr"
    KILOGRAMO = "kg"
    LITRO = "l"
    MILILITRO = "ml"
    TAZA = "taza"
    CUCHARADA = "cda"
    CUCHARADITA = "cdita"
    UNIDAD = "unidad"

    @classmethod
    def list(cls) -> list[str]:
        return list(map(lambda c: c.value, cls))


# TODO: Implementar la clase Ingrediente
class Ingrediente:
    def __init__(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        self.alimento: str = alimento
        self.cantidad: float = cantidad
        self.unidad: UnidadMedida = unidad

    def __str__(self) -> str:
        return f"<{self.cantidad}> <{self.unidad.value}> de <{self.alimento}>"

# TODO: Implementar la clase Receta
class Receta:
    def __init__(self, nombre: str, descripcion: str, etiquetas: None):
        if etiquetas == None:
            etiquetas: list = []
        self.nombre: str = nombre
        self.ingredientes: list[Ingrediente] = []
        self.descripcion: str = descripcion
        self.etiquetas: list[str] = etiquetas

    def agregar_ingrediente(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        ingrediente = Ingrediente(alimento, cantidad, unidad)
        self.ingredientes.append(ingrediente)













# TODO: Implementar la clase Chef
class Chef:
    def __init__(self):
        self.recetas: list[Receta] = []

    def registrar_receta(self, nombre: str, ingredientes: list[(str, float, UnidadMedida)], descripcion: str, etiquetas: list[str]= None):
        receta = Receta(nombre, ingredientes, descripcion, etiquetas)
        for ingrediente in ingredientes:
            receta.agregar_ingrediente(ingrediente.alimento, ingrediente.cantidad, ingrediente.unidad)
        pass

    def buscar_receta(self, nombre: str) -> Receta or None :
        for receta in self.recetas:
            pass

    def  recetas_vegetarianas(self) -> Receta:






