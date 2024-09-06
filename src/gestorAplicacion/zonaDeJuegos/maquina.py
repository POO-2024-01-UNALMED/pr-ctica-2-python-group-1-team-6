import sys
sys.path.append("gestorAplicacion/zonaDeJuegos")


class Maquina:
    
    allMaquinas = []  # Lista para almacenar todas las instancias de Maquina
    
    def __init__(self, nombre, tipo, materialesNecesarios, precioUso):
        self.nombre = nombre  # Nombre de la máquina
        self.usos = 0  # Contador de usos
        self.materialesNecesarios = materialesNecesarios  # Materiales necesarios para el mantenimiento
        self.disponible = True  # Estado de disponibilidad
        self.dineroRecaudado = 0.0  # Dinero recaudado por la máquina
        self.precioUso = precioUso  # Precio por uso
        self.tipo = tipo  # Tipo de la máquina (ej. Arcade, Dance Dance)
        self.zonaDeJuegos = None  # Zona de juegos a la que pertenece la máquina
        self.bonoActivo = False  # Indica si el bono está activo
        if self not in Maquina.allMaquinas:
            Maquina.allMaquinas.append(self)  # Agrega la máquina a la lista global
    
    def getUsos(self):
        return self.usos  # Devuelve el número de usos
    
    def setUsos(self, usos):
        self.usos = usos  # Establece el número de usos
    
    def getNombre(self):
        return self.nombre  # Devuelve el nombre de la máquina
    
    def estaDisponible(self):
        # Verifica si la máquina está disponible para su uso
        return not self.necesitaMantenimiento()
    
    def necesitaMantenimiento(self):
        # Revisa si la máquina necesita mantenimiento después de 12 usos
        if self.usos >= 12:
            self.disponible = False
            return True
        else:
            self.disponible = True
            return False
    
    def usar(self):
        # Incrementa los usos y el dinero recaudado si la máquina está disponible
        if self.disponible:
            self.usos += 1
            self.dineroRecaudado += self.precioUso
        elif self.necesitaMantenimiento():
            self.disponible = False
    
    def setPrecioUso(self, precio):
        self.precioUso = precio  # Establece el precio por uso
    
    def getPrecioUso(self):
        return self.precioUso  # Devuelve el precio por uso
    
    def reparar(self):
        # Resetea el contador de usos y vuelve la máquina disponible
        self.usos = 0
        self.disponible = True
    
    def getDineroRecaudado(self):
        return self.dineroRecaudado  # Devuelve el dinero recaudado por la máquina
    
    def getMaterialesNecesarios(self):
        return self.materialesNecesarios  # Devuelve la cantidad de materiales necesarios para el mantenimiento
    
    def getTipo(self):
        return self.tipo  # Devuelve el tipo de la máquina
    
    def setTipo(self, tipo):
        self.tipo = tipo  # Establece el tipo de la máquina
    
    def getZonaDeJuegos(self):
        return self.zonaDeJuegos  # Devuelve la zona de juegos a la que pertenece la máquina
    
    def setZonaDeJuegos(self, zonaDeJuegos):
        self.zonaDeJuegos = zonaDeJuegos  # Establece la zona de juegos de la máquina
    
    def activarBono(self):
        self.bonoActivo = True  # Activa el bono de la máquina
    
    def asignarBono(self, cliente):
        # Asigna un bono al cliente basado en su tipo si el bono está activo
        if self.bono_activo:
            if cliente.getTipo() == "Generico":
                cliente.setSaldo(cliente.getSaldo() + 15)  # Bono para cliente genérico
            elif cliente.getTipo() == "Preferencial":
                cliente.setSaldo(cliente.getSaldo() + 20)  # Bono para cliente preferencial
            elif cliente.getTipo() == "VIP":
                cliente.setSaldo(cliente.getSaldo() + 30)  # Bono para cliente VIP
        return f"Bono {cliente.getTipo()} asignado a {cliente.getNombre()}"
    
    @staticmethod
    def obtenerDosMaquinasMenosVenden():
        from src.gestorAplicacion.zonaDeJuegos.establecimiento import ZonaDeJuegos
        # Devuelve las dos máquinas que menos dinero han recaudado
        todas_las_maquinas = []
        
        for zona in ZonaDeJuegos.zonasDeJuegos:
            todas_las_maquinas.extend(zona.getMaquinas())
        
        todas_las_maquinas.sort(key=lambda maquina: maquina.getDineroRecaudado())
        
        return todas_las_maquinas[:2]  # Devuelve las dos primeras máquinas de la lista ordenada
    
    def __str__(self):
        return f"Maquina: {self.nombre} Tipo: {self.tipo}, Recaudado: {self.dineroRecaudado} perteneciente a la zona {self.zonaDeJuegos}"
