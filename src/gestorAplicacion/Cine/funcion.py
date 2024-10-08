import sys
from typing import List, Optional
from datetime import datetime, timedelta
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador

# Ajusta el sys.path para facilitar las importaciones
sys.path.append("gestorAplicacion/Cine")
#La clase funcion esa la que utiliza la clase pelicula y clase sala en este sistema, cada funcion debe tener su pelicula y su sala, Las hay de tipo Normal y VIP

class Funcion:
    # Lista estática para almacenar todas las funciones
    allFunciones: List['Funcion'] = []

    def __init__(self, tipo, pelicula=None, sala=None, precio=0):
        self.pelicula = pelicula
        self.tipo = tipo
        self.sala = sala
        self.precio = precio
        self.momentoDelDia = ""

        if self not in Funcion.allFunciones:
            Funcion.allFunciones.append(self)

        if self.pelicula:
            self.pelicula.getFunciones().append(self)
    
    #Permite cambiar la pelicula de la funcion
    def setPelicula(self, nuevaPelicula):

        if self.pelicula == nuevaPelicula:
            return

        if self.pelicula:
            self.pelicula.getFunciones().remove(self)

        self.pelicula = nuevaPelicula

        if nuevaPelicula and self not in nuevaPelicula.getFunciones():
            nuevaPelicula.getFunciones().append(self)

    def getPelicula(self):
        return self.pelicula
    def getTipo(self) -> str:
        return self.tipo

    def setTipo(self, tipo: str):
        self.tipo = tipo

    def getSala(self) :
        return self.sala

    def setSala(self, sala):
        self.sala = sala

    def getPrecio(self) -> float:
        return self.precio

    def setPrecio(self, precio: float):
        self.precio = precio
    def getMomentoDelDia(self) -> str:
        return self.momentoDelDia

    def setMomentoDelDia(self, momentoDelDia: str):
        self.momentoDelDia = momentoDelDia
    #Realiza el intercambio de peliculas entre 2 funciones a partir de sus peliculas y los cines a los que pertenecen
    @staticmethod
    def realizarIntercambio(cineOrigen,cineNuevo,peliculaAIntercambiar, peliculaRecomendada) -> str:
        from src.gestorAplicacion.Cine.cine import Cine
        # Buscar la función de la película recomendada
        for funcion in cineNuevo.totalFunciones():
            if funcion.getPelicula()==peliculaRecomendada:
                funcionDestino=funcion
                if funcionDestino:
                    break
    
        if not funcionDestino:
            return "No se encontró una función con la película recomendada."

        # Buscar la función de la película a intercambiar
        for funcion in cineOrigen.totalFunciones():
            if funcion.getPelicula()==peliculaAIntercambiar:
                funcionOrigen=funcion
                if funcionOrigen:
                    break
    
        if not funcionOrigen:
            return "No se encontró una función con la película a intercambiar."

        # Realizar el intercambio de películas
        funcionOrigen.setPelicula(peliculaRecomendada)
        funcionDestino.setPelicula(peliculaAIntercambiar)

        return "Intercambio realizado exitosamente."
    #Devuelve la posicion que ocupa una funcion dentro del intinerario del dia
    @staticmethod
    def obtenerIndiceEnDia(funcionBuscada: 'Funcion') -> int:
        from src.gestorAplicacion.Cine.cine import Cine

        for cine in Cine.cines:
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
        return -1

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

    #Perimite hayar el cine al cual pertenece una funcion
    @staticmethod
    def encontrarCine(funcion: 'Funcion'):
        from src.gestorAplicacion.Cine.cine import Cine
        for cine in Cine.cines:
            for f in cine.totalFunciones():
                if funcion==f:
                    return cine
        return None
        
    #Permite hayar el dia al cual pertenece uan funcion dentro de su cine
    @staticmethod
    def encontrarDia(funcion: 'Funcion', cine) -> str:
        for f in cine.getLunes():
            if f!=None:
                if funcion.getPelicula().getTitulo()==f.getPelicula().getTitulo() and funcion.getSala().getNumero()==f.getSala().getNumero():
                    return "Lunes"
        for f in cine.getMartes():
            if f!=None:
                if funcion.getPelicula().getTitulo()==f.getPelicula().getTitulo() and funcion.getSala().getNumero()==f.getSala().getNumero():
                    return "Martes"
        for f in cine.getJueves():
            if f!=None:
                if funcion.getPelicula().getTitulo()==f.getPelicula().getTitulo() and funcion.getSala().getNumero()==f.getSala().getNumero():
                    return "Jueves"
        for f in cine.getViernes():
            if f!=None:
                if funcion.getPelicula().getTitulo()==f.getPelicula().getTitulo() and funcion.getSala().getNumero()==f.getSala().getNumero():
                    return "Viernes"
        for f in cine.getSabado():
            if f!=None:
                if funcion.getPelicula().getTitulo()==f.getPelicula().getTitulo() and funcion.getSala().getNumero()==f.getSala().getNumero():
                    return "Sábado"
        return "Día no encontrado"
        
    #Serializa todas las funciones
    @staticmethod
    def serializarFunciones(file_name):
        Serializador.serializar(Funcion.allFunciones, file_name)
    #Deserializa todas las funciones
    @staticmethod
    def deserializarFunciones(file_name):
        objetos = Deserializador.deserializar(file_name)
        if objetos is not None:
            Funcion.allFunciones = objetos
    
    def __str__(self) -> str:
        return f"Funcion: {self.tipo} Sala: {self.sala} {self.pelicula}"      
