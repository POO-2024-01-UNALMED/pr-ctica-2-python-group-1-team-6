import sys
from typing import List, Optional
from datetime import time
from copy import deepcopy
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador

sys.path.append("gestorAplicacion/Cine")  # Ajusta el path según sea necesario

#La clase cine es el eje de todo, ya que contiene funciones y zonas de juegos. 
class Cine:
    peliculas: List = []  # Lista estática de películas
    cines: List['Cine'] = []  # Lista estática de cines
    LIMITE_TARJETAS = 10  # Constante de límite de tarjetas

    def __init__(self, nombre, zonaDeJuegos = None):
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
        def contienePelicula(dia: List[Optional['Funcion']]) -> bool:
            return any(
                funcion is not None and funcion.getPelicula() is not None and
                funcion.getPelicula().getTitulo() == pelicula.getTitulo()
                for funcion in dia
            )

        return (
            contienePelicula(self.lunes) or
            contienePelicula(self.martes) or
            contienePelicula(self.jueves) or
            contienePelicula(self.viernes) or
            contienePelicula(self.sabado)
        )

    def enseñarFunciones(self) -> str:
        from src.gestorAplicacion.Cine.funcion import Funcion
        
        # Muestra las funciones de cada día
        def procesarDia(dia: List[Optional['Funcion']], nombreDia: str) -> str:
            peliculasMostradas = []
            resultado = f"{nombreDia}:\n"
            for funcion in dia:
                if funcion and funcion.getPelicula():
                    pelicula = funcion.getPelicula()
                    if pelicula not in peliculasMostradas:
                        resultado += f"{pelicula.getTitulo()}\n"
                        peliculasMostradas.append(pelicula)
            if not peliculasMostradas:
                resultado += "No hay películas\n"
            return resultado + "\n"

        return (
            procesarDia(self.lunes, "Lunes") +
            procesarDia(self.martes, "Martes") +
            procesarDia(self.jueves, "Jueves") +
            procesarDia(self.viernes, "Viernes") +
            procesarDia(self.sabado, "Sábado")
        )
    def totalFunciones(self):
        # Combina todas las funciones, evitando las que sean None
        todasLasFunciones = (
            self.lunes + self.martes + self.jueves + self.viernes + self.sabado
        )
        # Filtra las funciones que no son None
        funciones_validas = [funcion for funcion in todasLasFunciones if funcion is not None]
        return funciones_validas

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
        def funcionesDia(dia: List[Optional['Funcion']]) -> List['Funcion']:
            return [
                funcion for funcion in dia
                if funcion and funcion.getPelicula() and
                   funcion.getPelicula().getTitulo().lower() == pelicula.getTitulo().lower() and
                   funcion.getSala().hayAsientosLibres()
            ]

        return (
            funcionesDia(self.lunes) +
            funcionesDia(self.martes) +
            funcionesDia(self.jueves) +
            funcionesDia(self.viernes) +
            funcionesDia(self.sabado)
        )

    def ajustarFunciones(self):
        from src.gestorAplicacion.Cine.funcion import Funcion
        
        # Ajusta la información de cada función en el cine
        def ajustarDia(dia: List[Optional['Funcion']], nombre_dia: str):
            for funcion in dia:
                if funcion:
                    funcion.setDia(nombre_dia)
                    funcion.definirMomentoDelDia()

        ajustarDia(self.lunes, "Lunes")
        ajustarDia(self.martes, "Martes")
        ajustarDia(self.jueves, "Jueves")
        ajustarDia(self.viernes, "Viernes")
        ajustarDia(self.sabado, "Sábado")

    def obtenerCalificacionesPeliculas(self) -> List[str]:
        from src.gestorAplicacion.Cine.funcion import Funcion
        
        # Obtiene las calificaciones de las películas en las funciones del cine
        def calificacionesDia(dia: List[Optional['Funcion']], nombreDia: str) -> List[str]:
            return [
                f"Película: {funcion.getPelicula().getTitulo()} Sala: {funcion.getSala()} - Calificación: {funcion.getPelicula().getCalificacionPromedio()} - Día: {nombreDia}"
                for funcion in dia if funcion and funcion.getPelicula()
            ]

        return (
            calificacionesDia(self.lunes, "Lunes") +
            calificacionesDia(self.martes, "Martes") +
            calificacionesDia(self.jueves, "Jueves") +
            calificacionesDia(self.viernes, "Viernes") +
            calificacionesDia(self.sabado, "Sábado")
        )

    def getZonaDeJuegos(self):
        return self.zonaDeJuegos

    def setZonaDeJuegos(self, zonaDeJuegos):
        self.zonaDeJuegos = zonaDeJuegos

    def agregarFuncion(self, nuevaFuncion, funciones):
    # Obtiene la película de la nueva función
        nuevaPelicula = nuevaFuncion.getPelicula()
    
    # Encuentra la posición adecuada para la nueva función según su género
        posicionApropiada = self.encontrarPosicionApropiada(nuevaPelicula, funciones)

    # Si no se encuentra una posición adecuada, avisa y no hace nada
        if posicionApropiada == -1:
            print("No se encontró una posición adecuada para la función. El día está lleno o no hay un sitio apropiado.")
            return

    # Si la posición adecuada está ocupada, reorganiza para hacer espacio
        if funciones[posicionApropiada] is not None:
            if not self.reorganizarFunciones(funciones, posicionApropiada):
                print("No se pudo reorganizar las funciones para hacer espacio.")
                return

    # Asigna la nueva función en la posición adecuada
        funciones[posicionApropiada] = nuevaFuncion
        nuevaFuncion.definirMomentoDelDia()
        print(f"Función agregada en la posición {posicionApropiada} para la película {nuevaPelicula.getTitulo()}.")

    def encontrarPosicionApropiada(self, nuevaPelicula, funciones) -> int:
    # Definir los rangos de posiciones según el género de la película
        if nuevaPelicula.getGenero() == "Infantil":
        # Rango de posiciones para películas infantiles (posiciones tempranas)
            rango = range(0, 3)
        elif nuevaPelicula.getGenero() == "Terror":
        # Rango de posiciones para películas de terror (posiciones tardías)
            rango = range(4, len(funciones))
        elif nuevaPelicula.getGenero() == "+18":
        # Rango de posiciones para películas +18 (funciones no tempranas)
            rango = range(3, len(funciones))
        else:
        # Géneros de Acción y Drama o cualquier otro (cualquier posición disponible)
            rango = range(0, len(funciones))

    # Buscar la primera posición vacía en el rango adecuado
        for i in rango:
            if funciones[i] is None:
                return i
    
    # Si no se encuentra una posición adecuada, devolver -1
        return -1

    def reorganizarFunciones(self, funciones, posicion: int) -> bool:
    # Verificar si hay espacio al final para mover las funciones
        if funciones[-1] is not None:
            return False

    # Mover las funciones hacia adelante para hacer espacio
        for i in range(len(funciones) - 1, posicion, -1):
            funciones[i] = funciones[i - 1]
        funciones[posicion] = None
        return True
    #Se encargar de serializar Todos lo objetos de la clase cine      
    @staticmethod
    def serializarCines(file_name):
        Serializador.serializar(Cine.cines, file_name)
    #Se encargar de deserializar Todos lo objetos de la clase cine  
    @staticmethod
    def deserializarCines(file_name):
        objetos = Deserializador.deserializar(file_name)
        if objetos is not None:
            Cine.cines = objetos

    def __str__(self) -> str:
        return f"Cine: {self.nombre}\nZona de Juegos: {self.zonaDeJuegos}\n" + self.enseñarFunciones()