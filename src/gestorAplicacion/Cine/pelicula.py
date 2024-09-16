import sys
from datetime import time, datetime
from typing import List
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador
from cine import Cine



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
        from src.gestorAplicacion.Cine.cine import Cine
        funcionesPosibles = []

        funcionesSeleccionadas = peliculaSeleccionada.funciones

        for funcionSeleccionada in funcionesSeleccionadas:
            posicionSeleccionadaEnDia = Funcion.obtenerIndiceEnDia(funcionSeleccionada)

            for cine in Cine.cines:
                for funcionIntercambio in cine.totalFunciones():
                    peliculaIntercambio = funcionIntercambio.getPelicula()
                    if peliculaIntercambio is None:
                        continue
                    if Funcion.encontrarCine(funcionIntercambio)==Funcion.encontrarCine(funcionSeleccionada):
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

        return (f"Se recomienda intercambiar la película seleccionada con: {mejorPelicula.getTitulo()} "
                f"(Calificación: {mejorPelicula.getCalificacionPromedio()}).\n"
                f"Esta película se proyecta en el cine: {cine.getNombre()}, el día: {dia} "
                )

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

    #Este método recibe un horario, dia y cine con los cuales determina las películas que pueden ser elegidas para programar una función, tiene en cuenta el género de la película, el horario, la duración y el orden de acuerdo a su calificación.
    @classmethod
    def ObtenerPeliculasElegibles(cls, horario, dia, cine):
        #Listas necesarias para almacenar la información
        peliculasTotales = Pelicula.totalPeliculas #Todas las pelìculas que pertenecen al cine.
        peliculasElegibles = [] 
        peliculasDelDia=cine.obtenerPeliculasDelDia(dia) #Las filtramos para no tenerlas en cuenta en una nueva función.
        categoriasPermitidas = []
        calificaciones = []
        duracion = None

        #Convertimos el string horario en un objeto time para poder compararlo con mayor facilidad.
        if horario.find("p") != -1:
          if (horario[:2] == "12"):
            horario = horario.replace(horario[:2], "00")
          else:
            horario = horario.replace(horario[:2], str(int(horario[:2]) + 12))
          horario = datetime.strptime(horario[:5], "%H:%M").time()
        elif horario.find("a") != -1:
          horario = datetime.strptime(horario[:5], "%H:%M").time()

        if horario == time(20,0): #Solo si el horario es el de 8pm, nos preocuparemos por la duración de la pelícuka.
            duracion = False
        else:
            duracion = True

        #Definimos cuáles son las categorías que nos importan según el período del día
        if horario >= time(8,0) and horario <= time(16,0):
            categoriasPermitidas.append("Acción")
            categoriasPermitidas.append("Infantil")
        else:
            categoriasPermitidas.append("Terror")
            categoriasPermitidas.append("+18")

        #Ahora agregaremos a la lista de películas elegibles aquellas que no estén programadas en otro momento del día y que su duración no sobrepase el límite de 4 horas.
        for pelicula in peliculasTotales:
            if pelicula in peliculasDelDia:
                continue
            if pelicula.getGenero() in categoriasPermitidas:
                if duracion:
                    duracionPelicula = pelicula.getDuracion()
                    if duracionPelicula > time(2,0,0): #Tiempo que no se puede superar
                        continue
                    else:
                        peliculasElegibles.append(pelicula)
                        calificaciones.append(pelicula.getCalificacionPromedio())
                else:
                    peliculasElegibles.append(pelicula)
                    calificaciones.append(pelicula.getCalificacionPromedio())

        #Ordenaremos la lista de películas elegibles según su calificación, de la que tiene más a la que tiene menos.
        iteracion  = 0
        if len(peliculasElegibles) == 1:
            return peliculasElegibles
        for calificacion in calificaciones:
            calificacionMayor = max(calificaciones)
            for pelicula in peliculasElegibles:
                if pelicula.getCalificacionPrimedio() == calificacionMayor and len(calificaciones) != 1:
                    if peliculasElegibles[iteracion] != pelicula:
                        peliculaAuxiliar = peliculasElegibles[iteracion]
                        index = peliculasElegibles.index(pelicula)
                        peliculasElegibles[iteracion] = pelicula
                        peliculasElegibles[index] = peliculaAuxiliar
                        calificaciones.remove(calificacionMayor)
                        iteracion += 1
                        break
                    else:
                        calificaciones.remove(calificacionMayor)
                        iteracion += 1
        return peliculasElegibles

    
    @staticmethod
    def serializarPeliculas(file_name):
        Serializador.serializar(Pelicula.totalPeliculas, file_name)

    @staticmethod
    def deserializarPeliculas(file_name):
        objetos = Deserializador.deserializar(file_name)
        if objetos is not None:
            Pelicula.totalPeliculas = objetos


