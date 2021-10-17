"""Clases para objetos relacionados
"""


class Opcion():
    def __init__(self, codigo, descripcion):
        """
        Parameters
        ----------
        codigo: str
            Codigo unico de la opción. Ejm: 01
        descripcion: str
            Descripción de la opción
        """
        self._codigo = codigo
        self._descripcion = descripcion

    # setters y getters
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    def __str__(self):
        return "{0} {1}".format(self.codigo, self.descripcion)
