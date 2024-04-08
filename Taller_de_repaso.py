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

    def contiene(self, elemento: Elemento) -> bool:
        """Verifica si el conjunto contiene un elemento con el mismo nombre."""
        for e in self.elementos:
            if e.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento: Elemento)-> None:
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self,otro_conjunto: "Conjunto") -> "Conjunto":
        """Agrega los elementos de otro conjunto a este conjunto sin duplicados."""
        nuevo_conjunto = Conjunto(f"{self.nombre}_unido_{otro_conjunto.nombre}")
        for elem in self.lista_elementos:
            nuevo_conjunto.agregar_elemento(elem)
        for elem in otro_conjunto.lista_elementos:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto

    def __add__(self, otro_conjunto: 'Conjunto') -> 'Conjunto':
        """Sobrecarga del operador + para unir dos conjuntos."""
        return self.unir(otro_conjunto)