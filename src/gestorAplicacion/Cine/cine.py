import sys
from typing import List, Optional

sys.path.append("gestorAplicacion/Cine")  # Ajusta el path según sea necesario

class Cine:
    peliculas: List = []  # Lista estática de películas
    cines: List['Cine'] = []  # Lista estática de cines
    LIMITE_TARJETAS = 10  # Constante de límite de tarjetas

    def __init__(self, nombre: str, zonaDeJuegos = None):
        self.nombre = nombre
        self.zonaDeJuegos = zonaDeJuegos
        if zonaDeJuegos is not None:
            self.zonaDeJuegos.setCine(self)
        if self not in Cine.cines:
            Cine.cines.append(self)
        
        # Inicializar funciones para cada día
        self.lunes: List = [None] * 7
        self.martes: List = [None] * 7
        self.jueves: List = [None] * 7
        self.viernes: List = [None] * 7
        self.sabado: List = [None] * 7

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def getLunes(self):
        return self.lunes

    def setLunes(self, lunes):
        if len(lunes) == 7:
            self.lunes = lunes
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getMartes(self) :
        return self.martes

    def setMartes(self, martes):
        if len(martes) == 7:
            self.martes = martes
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getJueves(self):
        return self.jueves

    def setJueves(self, jueves):
        if len(jueves) == 7:
            self.jueves = jueves
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getViernes(self) :
        return self.viernes

    def setViernes(self, viernes):
        if len(viernes) == 7:
            self.viernes = viernes
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def getSabado(self):
        return self.sabado

    def setSabado(self, sabado):
        if len(sabado) == 7:
            self.sabado = sabado
        else:
            raise ValueError("El arreglo debe tener exactamente 7 elementos.")

    def hayPelicula(self, pelicula) -> bool:
        from src.gestorAplicacion.Cine.funcion import Funcion  
        
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
        from src.gestorAplicacion.Cine.funcion import Funcion
        
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

    def peliculasActivas(self):
        # Obtiene la lista de películas activas en el cine
        peliculas = set()
        for dia in [self.lunes, self.martes, self.jueves, self.viernes, self.sabado]:
            for funcion in dia:
                if funcion and funcion.getPelicula():
                    peliculas.add(funcion.getPelicula())
        return list(peliculas)

    def obtenerFunciones(self, pelicula):
        from src.gestorAplicacion.Cine.funcion import Funcion
        
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
        from src.gestorAplicacion.Cine.funcion import Funcion
        
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
        from src.gestorAplicacion.Cine.funcion import Funcion
        
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

    def getZonaDeJuegos(self):
        return self.zonaDeJuegos

    def setZonaDeJuegos(self, zonaDeJuegos):
        self.zonaDeJuegos = zonaDeJuegos

    def agregarFuncion(self, nuevaFuncion, funciones):
        
        # Agrega una nueva función a la lista de funciones
        nuevaPelicula = nuevaFuncion.getPelicula()
        posicionApropiada = self.encontrarPosicionApropiada(nuevaPelicula, funciones)

        if posicionApropiada == -1:
            # No hay posiciones adecuadas disponibles
            
            return

        if funciones[posicionApropiada] is not None:
            # Reorganizar las funciones para hacer espacio
            if not self.reorganizarFunciones(funciones, posicionApropiada):
                
                return

        funciones[posicionApropiada] = nuevaFuncion
        nuevaFuncion.definirMomentoDelDia()
        

    def encontrarPosicionApropiada(self, nuevaPelicula, funciones) -> int:
        
        # Encuentra la posición adecuada para la nueva función
        for i, funcion in enumerate(funciones):
            if funcion is None:
                return i
            peliculaExistente = funcion.getPelicula()
            if peliculaExistente.getGenero() != nuevaPelicula.getGenero():
                return i
        return -1

    def reorganizarFunciones(self, funciones, posicion: int) -> bool:
        # Reorganiza las funciones para hacer espacio
        for i in range(len(funciones) - 1, posicion, -1):
            funciones[i] = funciones[i - 1]
        funciones[posicion] = None
        return True

    def __str__(self) -> str:
        return f"Cine: {self.nombre}\nZona de Juegos: {self.zonaDeJuegos}\n" + self.enseñarFunciones()
