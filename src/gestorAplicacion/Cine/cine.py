from typing import List, Optional, Union
from zonaDeJuegos.zonaDeJuegos import ZonaDeJuegos
from funcion import Funcion
from pelicula import Pelicula

class Cine:
    peliculas: List['Pelicula'] = []  # Lista estática de películas
    cines: List['Cine'] = []  # Lista estática de cines
    LIMITE_TARJETAS = 10  # Constante de límite de tarjetas

    def __init__(self, nombre: str, zonaDeJuegos: Optional['ZonaDeJuegos'] = None):
        self.nombre = nombre
        self.zonaDeJuegos = zonaDeJuegos
        if zonaDeJuegos is not None:
            self.zonaDeJuegos.setCine(self)
        if self not in Cine.cines:
            Cine.cines.append(self)
        
        # Inicializar funciones para cada día
        self.lunes: List[Optional['Funcion']] = [None] * 7
        self.martes: List[Optional['Funcion']] = [None] * 7
        self.jueves: List[Optional['Funcion']] = [None] * 7
        self.viernes: List[Optional['Funcion']] = [None] * 7
        self.sabado: List[Optional['Funcion']] = [None] * 7

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def getLunes(self) -> List[Optional['Funcion']]:
        return self.lunes

    def setLunes(self, lunes: List[Optional['Funcion']]):
        if len(lunes) == 7:
            self.lunes = lunes
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getMartes(self) -> List[Optional['Funcion']]:
        return self.martes

    def setMartes(self, martes: List[Optional['Funcion']]):
        if len(martes) == 7:
            self.martes = martes
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getJueves(self) -> List[Optional['Funcion']]:
        return self.jueves

    def setJueves(self, jueves: List[Optional['Funcion']]):
        if len(jueves) == 7:
            self.jueves = jueves
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getViernes(self) -> List[Optional['Funcion']]:
        return self.viernes

    def setViernes(self, viernes: List[Optional['Funcion']]):
        if len(viernes) == 7:
            self.viernes = viernes
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getSabado(self) -> List[Optional['Funcion']]:
        return self.sabado

    def setSabado(self, sabado: List[Optional['Funcion']]):
        if len(sabado) == 7:
            self.sabado = sabado
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def hayPelicula(self, pelicula: 'Pelicula') -> bool:
        # Verifica si una película está en las funciones de cualquier día
        def contiene_pelicula(dia: List[Optional['Funcion']]) -> bool:
            return any(
                funcion is not None and funcion.getPelicula() is not None and
                funcion.getPelicula().getTitulo() == pelicula.getTitulo()
                for funcion in dia
            )

        return (
            contiene_pelicula(self.lunes) or
            contiene_pelicula(self.martes) or
            contiene_pelicula(self.jueves) or
            contiene_pelicula(self.viernes) or
            contiene_pelicula(self.sabado)
        )

    def enseñarFunciones(self) -> str:
        # Muestra las funciones de cada día
        def procesar_dia(dia: List[Optional['Funcion']], nombre_dia: str) -> str:
            peliculas_mostradas = []
            resultado = f"{nombre_dia}:\n"
            for funcion in dia:
                if funcion and funcion.getPelicula():
                    pelicula = funcion.getPelicula()
                    if pelicula not in peliculas_mostradas:
                        resultado += f"{pelicula.getTitulo()}\n"
                        peliculas_mostradas.append(pelicula)
            if not peliculas_mostradas:
                resultado += "No hay películas\n"
            return resultado + "\n"

        return (
            procesar_dia(self.lunes, "Lunes") +
            procesar_dia(self.martes, "Martes") +
            procesar_dia(self.jueves, "Jueves") +
            procesar_dia(self.viernes, "Viernes") +
            procesar_dia(self.sabado, "Sábado")
        )

    def peliculasActivas(self) -> List['Pelicula']:
        # Obtiene la lista de películas activas en el cine
        peliculas = set()
        for dia in [self.lunes, self.martes, self.jueves, self.viernes, self.sabado]:
            for funcion in dia:
                if funcion and funcion.getPelicula():
                    peliculas.add(funcion.getPelicula())
        return list(peliculas)

    def obtenerFunciones(self, pelicula: 'Pelicula') -> List['Funcion']:
        # Obtiene las funciones disponibles para una película
        def funciones_dia(dia: List[Optional['Funcion']]) -> List['Funcion']:
            return [
                funcion for funcion in dia
                if funcion and funcion.getPelicula() and
                   funcion.getPelicula().getTitulo().lower() == pelicula.getTitulo().lower() and
                   funcion.getSala().hayAsientosLibres()
            ]

        return (
            funciones_dia(self.lunes) +
            funciones_dia(self.martes) +
            funciones_dia(self.jueves) +
            funciones_dia(self.viernes) +
            funciones_dia(self.sabado)
        )

    def ajustarFunciones(self):
        # Ajusta la información de cada función en el cine
        def ajustar_dia(dia: List[Optional['Funcion']], nombre_dia: str):
            for funcion in dia:
                if funcion:
                    funcion.setDia(nombre_dia)
                    funcion.definirMomentoDelDia()

        ajustar_dia(self.lunes, "Lunes")
        ajustar_dia(self.martes, "Martes")
        ajustar_dia(self.jueves, "Jueves")
        ajustar_dia(self.viernes, "Viernes")
        ajustar_dia(self.sabado, "Sábado")

    def obtenerCalificacionesPeliculas(self) -> List[str]:
        # Obtiene las calificaciones de las películas en las funciones del cine
        def calificaciones_dia(dia: List[Optional['Funcion']], nombre_dia: str) -> List[str]:
            return [
                f"Película: {funcion.getPelicula().getTitulo()} - Calificación: {funcion.getPelicula().getCalificacionPromedio()} - Día: {nombre_dia}"
                for funcion in dia if funcion and funcion.getPelicula()
            ]

        return (
            calificaciones_dia(self.lunes, "Lunes") +
            calificaciones_dia(self.martes, "Martes") +
            calificaciones_dia(self.jueves, "Jueves") +
            calificaciones_dia(self.viernes, "Viernes") +
            calificaciones_dia(self.sabado, "Sábado")
        )

    def getZonaDeJuegos(self) -> Optional['ZonaDeJuegos']:
        return self.zonaDeJuegos

    def setZonaDeJuegos(self, zonaDeJuegos: Optional['ZonaDeJuegos']):
        self.zonaDeJuegos = zonaDeJuegos

    def agregarFuncion(self, nuevaFuncion: 'Funcion', funciones: List[Optional['Funcion']]):
        # Agrega una nueva función a la lista de funciones
        nuevaPelicula = nuevaFuncion.getPelicula()
        posicionApropiada = self.encontrarPosicionApropiada(nuevaPelicula, funciones)

        if posicionApropiada == -1:
            # No hay posiciones adecuadas disponibles
            print("Error: No hay posiciones adecuadas disponibles.")
            return

        if funciones[posicionApropiada] is not None:
            # Reorganizar las funciones para hacer espacio
            if not self.reorganizarFunciones(funciones, posicionApropiada):
                # Si no es posible reorganizar las funciones, no se puede agregar la nueva
                print("Error: No se pudo reorganizar las funciones.")
                return

        # Agregar la nueva función a la posición adecuada
        funciones[posicionApropiada] = nuevaFuncion

    def encontrarPosicionApropiada(self, pelicula: 'Pelicula', funciones: List[Optional['Funcion']]) -> int:
        # Buscar una posición apropiada para la película
        for i, funcion in enumerate(funciones):
            if funcion is None:
                return i
        return -1  # No hay posición adecuada

    def reorganizarFunciones(self, funciones: List[Optional['Funcion']], posicion: int) -> bool:
        # Reorganiza las funciones para hacer espacio
        for i in range(len(funciones) - 1, posicion, -1):
            funciones[i] = funciones[i - 1]
        funciones[posicion] = None
        return True

    def __str__(self) -> str:
        return f"Cine: {self.nombre}\nZona de Juegos: {self.zonaDeJuegos}\n" + self.enseñarFunciones()
