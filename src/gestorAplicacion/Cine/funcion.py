from typing import List, Optional
from datetime import datetime, timedelta
from pelicula import Pelicula
from sala import Sala
from cine import Cine

class Funcion:
    # Lista estática para almacenar todas las funciones
    allFunciones: List['Funcion'] = []

    def __init__(self, pelicula: Optional['Pelicula'], tipo: str, sala: Optional['Sala'], precio: float):
        self.pelicula = pelicula
        self.tipo = tipo
        self.sala = sala
        self.precio = precio
        self.dia = ""
        self.momentoDelDia = ""

        # Agrega la función a la lista de todas las funciones si no está ya presente
        if self not in Funcion.allFunciones:
            Funcion.allFunciones.append(self)

        # Añade esta función a la lista de funciones de la película, si la película no es None
        if self.pelicula:
            self.pelicula.getFunciones().append(self)

    def setPelicula(self, nuevaPelicula: Optional['Pelicula']):
        if self.pelicula == nuevaPelicula:
            return  # Si la película es la misma, no hacer nada

        # Si hay una película anterior, quitar esta función de la lista de funciones de la película anterior
        if self.pelicula:
            self.pelicula.getFunciones().remove(self)

        # Establecer la nueva película
        self.pelicula = nuevaPelicula

        # Añadir esta función a la lista de funciones de la nueva película si no está ya presente
        if nuevaPelicula and self not in nuevaPelicula.getFunciones():
            nuevaPelicula.getFunciones().append(self)

    def getTipo(self) -> str:
        return self.tipo

    def setTipo(self, tipo: str):
        self.tipo = tipo

    def getSala(self) -> Optional['Sala']:
        return self.sala

    def setSala(self, sala: Optional['Sala']):
        self.sala = sala

    def getDia(self) -> str:
        return self.dia

    def setDia(self, dia: str):
        self.dia = dia

    def getMomentoDelDia(self) -> str:
        return self.momentoDelDia

    def setMomentoDelDia(self, momentoDelDia: str):
        self.momentoDelDia = momentoDelDia

    def getPrecio(self) -> float:
        return self.precio

    def setPrecio(self, precio: float):
        self.precio = precio

    @staticmethod
    def realizarIntercambio(peliculaAIntercambiar: 'Pelicula', peliculaRecomendada: 'Pelicula') -> str:
        # Buscar la función que muestra la película recomendada
        funcionDestino = next((f for f in Funcion.allFunciones if f.getPelicula() == peliculaRecomendada), None)

        if funcionDestino is None:
            return "No se encontró una función con la película recomendada."

        # Buscar una función que muestra la película a intercambiar
        funcionOrigen = next((f for f in Funcion.allFunciones if f.getPelicula() == peliculaAIntercambiar), None)

        if funcionOrigen is None:
            return "No se encontró una función con la película a intercambiar."

        # Realizar el intercambio de películas
        funcionOrigen.setPelicula(peliculaRecomendada)
        funcionDestino.setPelicula(peliculaAIntercambiar)

        return "Intercambio realizado exitosamente."

    @staticmethod
    def obtenerIndiceEnDia(funcionBuscada: 'Funcion') -> int:
        # Recorre todos los cines
        for cine in Cine.cines:
            # Recorre todos los días de la semana para el cine actual
            for i, f in enumerate(cine.getLunes()):
                if f and f == funcionBuscada:
                    return i
            for i, f in enumerate(cine.getMartes()):
                if f and f == funcionBuscada:
                    return i
            for i, f in enumerate(cine.getJueves()):
                if f and f == funcionBuscada:
                    return i
            for i, f in enumerate(cine.getViernes()):
                if f and f == funcionBuscada:
                    return i
            for i, f in enumerate(cine.getSabado()):
                if f and f == funcionBuscada:
                    return i
        return -1  # Retorna -1 si no se encontró la función en ninguna lista de días

    def getHoraInicio(self) -> str:
        indice = Funcion.obtenerIndiceEnDia(self)
        horas = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
        return horas[indice] if 0 <= indice < len(horas) else ""

    def definirMomentoDelDia(self) -> datetime:
        inicio = self.getHoraInicio()
        medioDia = datetime.strptime("12:00", "%H:%M")
        horaReal = datetime.strptime(inicio, "%H:%M")
        
        if medioDia > horaReal:
            self.setMomentoDelDia("am")
        else:
            self.setMomentoDelDia("pm")

        return horaReal

    @staticmethod
    def encontrarCine(funcion: 'Funcion') -> Optional['Cine']:
        for cine in Cine.cines:
            for f in cine.getLunes():
                if f and f == funcion:
                    return cine
            for f in cine.getMartes():
                if f and f == funcion:
                    return cine
            for f in cine.getJueves():
                if f and f == funcion:
                    return cine
            for f in cine.getViernes():
                if f and f == funcion:
                    return cine
            for f in cine.getSabado():
                if f and f == funcion:
                    return cine
        return None  # Si no se encuentra el cine

    @staticmethod
    def encontrarDia(funcion: 'Funcion', cine: 'Cine') -> str:
        for i, f in enumerate(cine.getLunes()):
            if f and f == funcion:
                return "Lunes"
        for i, f in enumerate(cine.getMartes()):
            if f and f == funcion:
                return "Martes"
        for i, f in enumerate(cine.getJueves()):
            if f and f == funcion:
                return "Jueves"
        for i, f in enumerate(cine.getViernes()):
            if f and f == funcion:
                return "Viernes"
        for i, f in enumerate(cine.getSabado()):
            if f and f == funcion:
                return "Sábado"
        return "Día no encontrado"  # Si no se encuentra el día
