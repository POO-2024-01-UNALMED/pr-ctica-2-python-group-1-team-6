from typing import Optional, List
from pelicula import Pelicula
from cine import Cine

class Cliente:
    allClientes: List['Cliente'] = []  # Lista estática de todos los clientes

    def __init__(self, nombre: str, saldo: float, tipo: str, identificacion: int):
        self.nombre = nombre
        self.saldo = saldo
        self.tipo = tipo
        self.identificacion = identificacion
        self.tarjeta = False
        self.puntosTarjeta = 0
        self.saldoTarjeta = 0
        self.tipoTarjeta = ""
        Cliente.allClientes.append(self)

    def __init__(self, nombre: str, saldo: float, identificacion: int):
        self.__init__(nombre, saldo, "Generico", identificacion)

    def getSaldo(self) -> float:
        return self.saldo

    def setSaldo(self, saldo: float):
        self.saldo = saldo

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def getTarjeta(self) -> bool:
        return self.tarjeta

    def setTarjeta(self, tarjeta: bool):
        self.tarjeta = tarjeta

    def getPuntosTarjeta(self) -> int:
        return self.puntosTarjeta

    def setPuntosTarjeta(self, puntos: int):
        self.puntosTarjeta = puntos

    def getSaldoTarjeta(self) -> int:
        return self.saldoTarjeta

    def setSaldoTarjeta(self, saldo: int):
        self.saldoTarjeta = saldo

    def getTipoTarjeta(self) -> str:
        return self.tipoTarjeta

    def setTipoTarjeta(self, tarjeta: str):
        self.tipoTarjeta = tarjeta

    def calificarPelicula(self, pelicula: 'Pelicula', calificacion: float):
        if calificacion < 0 or calificacion > 5:
            raise ValueError("La calificación debe estar entre 0 y 5.")
        pelicula.actualizarCalificacion(calificacion)

    @staticmethod
    def buscarClientePorId(id: int) -> Optional['Cliente']:
        for cliente in Cliente.allClientes:
            if cliente.identificacion == id:
                return cliente
        return None  # Si no existe

    def utilizarCupon(self, precio: int, descuento: int) -> float:
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        return precio - ((precio / 100) * descuento)

    def comprarBoleta(self, cine: 'Cine', pelicula: 'Pelicula') -> bool:
        return cine.hayPelicula(pelicula)

    def pagarConSaldo(self, monto: float) -> bool:
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        return False

    def pagarSaldoTarjeta(self, costo: float) -> bool:
        if self.saldoTarjeta >= costo:
            self.saldoTarjeta -= costo
            return True
        return False

    def pagarPuntosTarjeta(self, costo: float) -> bool:
        costoPuntos = int(costo / 100)
        if self.puntosTarjeta >= costoPuntos:
            self.puntosTarjeta -= costoPuntos
            return True
        return False

    def recargarTarjeta(self, cantidad: float) -> bool:
        if self.saldo >= cantidad:
            self.saldoTarjeta += cantidad
            self.pagarConSaldo(cantidad)
            return True
        return False

    def agregarPuntos(self) -> int:
        aumento = 0
        if self.tipoTarjeta.lower() == "platino":
            aumento = 200
        elif self.tipoTarjeta.lower() == "oro":
            aumento = 150
        elif self.tipoTarjeta.lower() == "bronce":
            aumento = 100
        self.puntosTarjeta += aumento
        return aumento

    def adquirirTarjeta(self, costoTarjeta: int) -> bool:
        if costoTarjeta == 10000:
            tipo = "Bronce"
        elif costoTarjeta == 17000:
            tipo = "Oro"
        elif costoTarjeta == 25000:
            tipo = "Platino"
        else:
            return False

        if self.saldo >= costoTarjeta:
            self.pagarConSaldo(costoTarjeta)
            self.setTarjeta(True)
            self.setTipoTarjeta(tipo)
            return True
        return False

    def getTipo(self) -> str:
        return self.tipo

    def setTipo(self, tipo: str):
        self.tipo = tipo

    def getIdentificacion(self) -> int:
        return self.identificacion

    def __str__(self) -> str:
        return f"Cliente: {self.nombre}, Saldo: {self.saldo}, Tipo: {self.tipo}"
