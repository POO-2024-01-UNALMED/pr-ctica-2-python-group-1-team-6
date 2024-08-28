from abc import ABC, abstractmethod

class Establecimiento(ABC):
    def __init__(self, nombre):
        # Atributo para almacenar el nombre del establecimiento
        self.nombre = nombre
        # Atributo para almacenar el dinero recaudado, inicializado en 0
        self.dinero_recaudado = 0

    def set_dinero_recaudado(self, dinero):
        # Método para establecer el dinero recaudado
        self.dinero_recaudado = dinero

    def get_dinero_recaudado(self):
        # Método para obtener el dinero recaudado
        return self.dinero_recaudado

    def get_nombre(self):
        # Método para obtener el nombre del establecimiento
        return self.nombre

    @abstractmethod
    def aplicar_promocion(self):
        # Método abstracto para aplicar una promoción, debe ser implementado en clases hijas
        pass

    def __str__(self):
        # Método para representar la clase como cadena, mostrando nombre y dinero recaudado
        return f"Establecimiento: {self.nombre}, Dinero Recaudado: {self.dinero_recaudado}"
