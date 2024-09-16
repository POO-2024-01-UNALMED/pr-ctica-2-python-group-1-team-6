from abc import ABC, abstractmethod
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador

class Establecimiento(ABC):
    def __init__(self, nombre):
        # Atributo para almacenar el nombre del establecimiento
        self.nombre = nombre
        # Atributo para almacenar el dinero recaudado, inicializado en 0
        self.dineroRecaudado = 0

    def setDineroRecaudado(self, dinero):
        # Método para establecer el dinero recaudado
        self.dineroRecaudado = dinero

    def getDineroRecaudado(self):
        # Método para obtener el dinero recaudado
        return self.dineroRecaudado

    def getNombre(self):
        # Método para obtener el nombre del establecimiento
        return self.nombre

    @abstractmethod
    def aplicarPromocion(self):
        # Método abstracto para aplicar una promoción, debe ser implementado en clases hijas
        pass

    def __str__(self):
        # Método para representar la clase como cadena, mostrando nombre y dinero recaudado
        return f"Establecimiento: {self.nombre}, Dinero Recaudado: {self.dineroRecaudado}"

class ZonaDeJuegos(Establecimiento):
    # Lista estática que almacena todas las instancias de ZonaDeJuegos
    zonasDeJuegos = []

    def __init__(self, nombre, horario):
        # Inicializa la clase padre Establecimiento
        super().__init__(nombre)
        self.horario = horario  # Horario de la zona de juegos
        self.maquinas = []  # Lista de máquinas en la zona de juegos
        self.cine = None  # Cine asociado a la zona de juegos
        if self not in ZonaDeJuegos.zonasDeJuegos:
            ZonaDeJuegos.zonasDeJuegos.append(self)

    def agregarMaquina(self, maquina):
        # Agrega una máquina a la lista y actualiza el dinero recaudado
        self.maquinas.append(maquina)
        maquina.setZonaDeJuegos(self)
        self.actualizarDineroRecaudado()

    def actualizarDineroRecaudado(self):
        # Actualiza el dinero recaudado sumando el de todas las máquinas
        totalRecaudado = sum(maquina.getDineroRecaudado() for maquina in self.maquinas)
        self.setDineroRecaudado(totalRecaudado)

    def getMaquinas(self):
        # Retorna la lista de máquinas
        return self.maquinas

    def getMaquinasDañadas(self):
        # Retorna una lista de máquinas que necesitan mantenimiento
        return [maquina for maquina in self.maquinas if maquina.necesitaMantenimiento()]

    def informeMaquinas(self):
        # Genera un informe con el estado de todas las máquinas en la zona de juegos
        informe = f"Informe de la Zona de Juegos: {self.getNombre()} {self.getCine().getNombre()}\n"
        informe += f"Horario: {self.horario}\n"
        for maquina in self.maquinas:
            if maquina.necesitaMantenimiento():
                estado="No Disponible"
            elif maquina.necesitaMantenimiento()==False:
                estado="Disponible"
            informe += f"{maquina.getNombre()} - {estado}\n"
        return informe

    def moverMaquina(self, zonaDestino, indiceMaquina):
        # Mueve una máquina a otra zona de juegos
        maquina = self.maquinas.pop(indiceMaquina)
        zonaDestino.agregarMaquina(maquina)
        return f"La máquina {maquina.getNombre()} ha sido movida a {zonaDestino.getNombre()}"

    def recomendarMovimiento(self, maquinaReparada):
        from src.gestorAplicacion.Cine.cine import Cine
        # Recomienda si se debe mover una máquina reparada a otra zona
        porcentajeDependencia = (maquinaReparada.getDineroRecaudado() / self.getDineroRecaudado()) * 100

        # Verifica si la máquina es crucial para la zona actual
        if porcentajeDependencia >= 70:
            return f"No se recomienda mover la máquina {maquinaReparada.getNombre()} ya que representa el {porcentajeDependencia:.2f}% de los ingresos de la zona actual."

        # Busca zonas candidatas para mover la máquina
        zonasCandidatas = [
        cine.zonaDeJuegos for cine in Cine.cines
        # Filtra zonas diferentes a la actual
        if self != cine.zonaDeJuegos and 
        # Filtra zonas que recaudan menos dinero que la zona actual
        cine.zonaDeJuegos.getDineroRecaudado() < self.getDineroRecaudado() and 
        # Filtra zonas que no tienen una máquina del mismo tipo que la máquina reparada
        not cine.zonaDeJuegos.tieneMaquinaDelTipo(maquinaReparada.getTipo())
        ]

        # Si hay zonas candidatas, recomienda la mejor opción
        if zonasCandidatas:
            mejorZonaDestino = min(zonasCandidatas, key=lambda z: z.getDineroRecaudado())
            return (f"Se recomienda mover la máquina {maquinaReparada.getNombre()} "
                    f"a la zona {mejorZonaDestino.getNombre()} ya que tiene menores ingresos "
                    f"y no cuenta con una máquina del tipo {maquinaReparada.getTipo()}.")
        else:
            return (f"No se recomienda mover la máquina {maquinaReparada.getNombre()}. "
                    "La zona actual tiene mejores ingresos o todas las otras zonas ya tienen una máquina del mismo tipo.")

    def tieneMaquinaDelTipo(self, tipo):
        # Verifica si la zona tiene una máquina del mismo tipo
        return any(maquina.getTipo() == tipo for maquina in self.getMaquinas())

    def obtenerPromedioIngresosMaquinas(self):
        # Calcula el promedio de ingresos de las máquinas en la zona actual
        totalDineroRecaudado = sum(maquina.getDineroRecaudado() for maquina in self.getMaquinas())
        numeroDeMaquinas = len(self.getMaquinas())
        return totalDineroRecaudado / numeroDeMaquinas if numeroDeMaquinas > 0 else 0

    def tieneMaquina(self, tipoMaquina):
        # Verifica si la zona tiene una máquina del tipo especificado
        return any(maquina.getTipo() == tipoMaquina for maquina in self.maquinas)

    def getCine(self):
        # Retorna el cine asociado a la zona de juegos
        return self.cine

    def setCine(self, cine):
        # Asocia un cine a la zona de juegos
        self.cine = cine

    def aplicarPromocion(self):
        # Implementación específica de la promoción en ZonaDeJuegos
        return f"Aplicando promoción en la zona de juegos {self.getNombre()}."
    
    @staticmethod
    def serializarZonasDeJuegos(file_name):
        Serializador.serializar(ZonaDeJuegos.zonasDeJuegos, file_name)

    @staticmethod
    def deserializarZonasDeJuegos(file_name):
        objetos = Deserializador.deserializar(file_name)
        if objetos is not None:
            ZonaDeJuegos.zonasDeJuegos = objetos
    def getHorario(self):
        return self.horario
    


    def __str__(self):
        # Representación en cadena de la zona de juegos
        return f"ZonaDeJuegos: {self.nombre}, Horario: {self.horario}, Máquinas: {len(self.maquinas)}"


class Bodega(Establecimiento):
    # Lista estática para almacenar todas las instancias de Bodega
    allBodegas = []

    def __init__(self, nombre, materialesDisponibles):
        # Inicializa la clase padre Establecimiento
        super().__init__(nombre)
        # Atributo para almacenar la cantidad de materiales disponibles
        self.materialesDisponibles = materialesDisponibles
        # Agrega la instancia a la lista all_bodegas si no está ya presente
        if self not in Bodega.allBodegas:
            Bodega.allBodegas.append(self)

    def tieneMaterialesSuficientes(self, cantidadNecesaria):
        # Verifica si hay suficientes materiales disponibles
        return self.materialesDisponibles >= cantidadNecesaria

    def usarMateriales(self, cantidad):
        # Disminuye la cantidad de materiales disponibles si hay suficientes
        if self.tieneMaterialesSuficientes(cantidad):
            self.materialesDisponibles -= cantidad

    def recargarMateriales(self, cantidad, costo):
        # Recarga los materiales y descuenta el costo del dinero recaudado
        self.materialesDisponibles += cantidad
        self.setDineroRecaudado(self.getDineroRecaudado() - costo)

    def realizarMantenimiento(self, zona, indiceMaquina):
        # Obtiene la máquina seleccionada de la zona de juegos
        maquinaSeleccionada = zona.getMaquinasDañadas()[indiceMaquina]
        
        # Si hay suficientes materiales, repara la máquina
        if self.tieneMaterialesSuficientes(maquinaSeleccionada.getMaterialesNecesarios()):
            self.usarMateriales(maquinaSeleccionada.getMaterialesNecesarios())
            maquinaSeleccionada.reparar()
            return f"La máquina {maquinaSeleccionada.getNombre()} ha sido reparada."
        else:
            return f"No hay suficientes materiales para reparar la máquina {maquinaSeleccionada.getNombre()}."

    def aplicarPromocion(self):
        # Implementación específica de la promoción en Bodega
        return f"Aplicando promoción en la bodega {self.getNombre()}."
    
    @staticmethod
    def serializarBodegas(file_name):
        Serializador.serializar(Bodega.allBodegas, file_name)

    @staticmethod
    def deserializarBodegas(file_name):
        objetos = Deserializador.deserializar(file_name)
        if objetos is not None:
            Bodega.allBodegas = objetos


    def __str__(self):
        # Representación en cadena de la bodega
        return f"Bodega: {self.nombre}, Materiales disponibles {self.materialesDisponibles}"