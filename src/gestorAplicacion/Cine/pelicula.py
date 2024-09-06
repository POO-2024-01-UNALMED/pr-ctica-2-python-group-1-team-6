import sys
from datetime import time
from typing import List

sys.path.append("gestorAplicacion/Cine")

class Pelicula:
    # Lista estática para almacenar todas las películas
    totalPeliculas: List['Pelicula'] = []

    def __init__(self, titulo: str, genero: str, duracion: time):
        from src.gestorAplicacion.Cine.cine import Cine
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.calificacionPromedio = 0.0
        self.numeroCalificaciones = 0
        self.funciones = []
        self.bonoActivo = False
        
        if self not in Pelicula.totalPeliculas:
            Pelicula.totalPeliculas.append(self)
        # Asumiendo que Cine.peliculas es una lista estática de películas
        Cine.peliculas.append(self)

    def getDuracion(self) -> time:
        return self.duracion

    def setDuracion(self, duracion: time):
        self.duracion = duracion

    def getTitulo(self) -> str:
        return self.titulo

    def setTitulo(self, titulo: str):
        self.titulo = titulo

    def getGenero(self) -> str:
        return self.genero

    def setGenero(self, genero: str):
        self.genero = genero

    def getCalificacionPromedio(self) -> float:
        return self.calificacionPromedio

    def setCalificacionPromedio(self, calificacionPromedio: float):
        self.calificacionPromedio = calificacionPromedio

    def getNumeroCalificaciones(self) -> int:
        return self.numeroCalificaciones

    def setNumeroCalificaciones(self, numeroCalificaciones: int):
        self.numeroCalificaciones = numeroCalificaciones

    def actualizarCalificacion(self, nuevaCalificacion: float):
        a = self.getCalificacionPromedio()
        b = self.getNumeroCalificaciones()
        self.setCalificacionPromedio((a * b + nuevaCalificacion) / (b + 1))
        self.setNumeroCalificaciones(b + 1)

    @staticmethod
    def getListado() -> List['Pelicula']:
        return Pelicula.totalPeliculas

    def __str__(self) -> str:
        return f"Pelicula: {self.titulo}, Género: {self.genero}, Calificacion: {self.calificacionPromedio}"

    @staticmethod
    def recomendarIntercambio(peliculaSeleccionada: 'Pelicula') -> str:
        from src.gestorAplicacion.Cine.funcion import Funcion
        funcionesPosibles = []

        funcionesSeleccionadas = peliculaSeleccionada.funciones

        for funcionSeleccionada in funcionesSeleccionadas:
            posicionSeleccionadaEnDia = Funcion.obtenerIndiceEnDia(funcionSeleccionada)

            for funcionIntercambio in Funcion.allFunciones:
                peliculaIntercambio = funcionIntercambio.getPelicula()
                if peliculaIntercambio is None:
                    continue

                if peliculaIntercambio.getGenero() == peliculaSeleccionada.getGenero():
                    continue

                posicionIntercambioEnDia = Funcion.obtenerIndiceEnDia(funcionIntercambio)
                if posicionSeleccionadaEnDia == posicionIntercambioEnDia:
                    continue

                # Verificar si la película seleccionada cumple con los criterios de horario en la función candidata
                cumpleCriteriosHorarioParaSeleccionada = Pelicula.cumpleCriteriosHorario(peliculaSeleccionada, posicionIntercambioEnDia)
                if not cumpleCriteriosHorarioParaSeleccionada:
                    continue

            # Verificar si la película candidata cumple con los criterios de horario en la función original
                cumpleCriteriosHorarioParaIntercambio = Pelicula.cumpleCriteriosHorario(peliculaIntercambio, posicionSeleccionadaEnDia)
                if not cumpleCriteriosHorarioParaIntercambio:
                    continue

                funcionesPosibles.append(funcionIntercambio)

        if not funcionesPosibles:
            return ("No se encontró ninguna película adecuada para el intercambio. Razones posibles:\n"
                    "- Todas las películas disponibles son del mismo género que la película seleccionada.\n"
                    "- No hay funciones en horarios compatibles para la película seleccionada o para el destino de intercambio.\n"
                    "- Las posiciones de las funciones para el intercambio no cumplen con los criterios.")

        mejorFuncion = max(funcionesPosibles, key=lambda f: f.getPelicula().getCalificacionPromedio())
        mejorPelicula = mejorFuncion.getPelicula()
        cine = Funcion.encontrarCine(mejorFuncion)
        dia = Funcion.encontrarDia(mejorFuncion, cine)
        horario = mejorFuncion.getHoraInicio()

        return (f"Se recomienda intercambiar la película seleccionada con: {mejorPelicula.getTitulo()} "
                f"(Calificación: {mejorPelicula.getCalificacionPromedio()}).\n"
                f"Esta película se proyecta en el cine: {cine.getNombre()}, el día: {dia} "
                f"a las: {horario}.")

    @staticmethod
    def cumpleCriteriosHorario(pelicula: 'Pelicula', posicionEnDia: int) -> bool:
        if pelicula.getGenero() == "Infantil":
            return posicionEnDia <= 3
        elif pelicula.getGenero() == "Terror":
            return posicionEnDia >= 4
        elif pelicula.getGenero() in {"Acción", "Drama"}:
            return True
        elif pelicula.getGenero() == "+18":
            return posicionEnDia >= 3
        else:
            return False

    def isBonoActivo(self) -> bool:
        return self.bonoActivo

    def activarBono(self):
        self.bonoActivo = True

    def getFunciones(self) :
        return self.funciones

    def setFunciones(self, nuevasFunciones):
        self.funciones = nuevasFunciones

    def asignarBono(self, cliente) -> str:
        if self.bonoActivo:
            if cliente.getTipo() == "Generico":
                cliente.setSaldo(cliente.getSaldo() + 5)
            elif cliente.getTipo() == "Preferencial":
                cliente.setSaldo(cliente.getSaldo() + 12)
            elif cliente.getTipo() == "VIP":
                cliente.setSaldo(cliente.getSaldo() + 20)
        return f"Bono {cliente.getTipo()} asignado a {cliente.getNombre()}"

