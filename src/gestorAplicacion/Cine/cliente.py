from typing import Optional, List
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador

#La clase cliente es la que instancia a los clientes para que puedan acceder a los servicios del sistema
class Cliente:
    allClientes: List['Cliente'] = []  # Lista estática de todos los clientes

    def __init__(self, nombre: str, saldo: float, identificacion: int, tipo: str = "Generico"):
        self.nombre = nombre
        self.saldo = saldo
        self.identificacion = identificacion
        
        Cliente.allClientes.append(self)


    def getSaldo(self) -> float:
        return self.saldo

    def setSaldo(self, saldo: float):
        self.saldo = saldo

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre

    
    # No se utiliza
    def calificarPelicula(self, pelicula, calificacion: float):
        if calificacion < 0 or calificacion > 5:
            raise ValueError("La calificación debe estar entre 0 y 5.")
        pelicula.actualizarCalificacion(calificacion)
    #Al recibir la id de un cliente la busca y devuelve el objeto cliente
    @staticmethod
    def buscarClientePorId(id: int) -> Optional['Cliente']:
        for cliente in Cliente.allClientes:
            if cliente.identificacion == id:
                return cliente
        return None  # Si no existe
    #No se usa
    def comprarBoleta(self, cine, pelicula) -> bool:
        return cine.hayPelicula(pelicula)
    #No se usa
    def pagarConSaldo(self, monto: float) -> bool:
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        return False


    def getIdentificacion(self) -> int:
        return self.identificacion
    
    #Serializa todas las instancias de tipo cliente
    @staticmethod
    def serializarClientes(file_name):
        Serializador.serializar(Cliente.allClientes, file_name)
    # Deserializa todas las instancias de tipo cliente
    @staticmethod
    def deserializarClientes(file_name):
        objetos = Deserializador.deserializar(file_name)
        if objetos is not None:
            Cliente.allClientes = objetos

    def __str__(self) -> str:
        return f"Cliente: {self.nombre}, Saldo: {self.saldo}"
