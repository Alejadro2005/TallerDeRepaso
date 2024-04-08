from dataclasses import dataclass

class Elemento:
    nombre: str

    def __eq__(self, other: "Elemento") -> bool:
        """Compara si dos objetos de la clase Elemento tienen el mismo nombre."""
        return self.nombre == other.nombre


class Conjunto:
    contador: int = 0

    def __init__(self, nombre: str):
        Conjunto.contador += 1
        self.elementos: list[Elemento] = []
        self.nombre: str = nombre
        self.__id = Conjunto.contador

    @property
    def _id(self) -> int:
        """Propiedad de solo lectura para el atributo __id."""
        return self.__id

    def contiene(self, elemento: Elemento) -> bool
        