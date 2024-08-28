from zonaDeJuegos import ZonaDeJuegos

class Maquina:
    
    all_maquinas = []  # Lista para almacenar todas las instancias de Maquina
    
    def __init__(self, nombre, tipo, materiales_necesarios, precio_uso):
        self.nombre = nombre  # Nombre de la máquina
        self.usos = 0  # Contador de usos
        self.materiales_necesarios = materiales_necesarios  # Materiales necesarios para el mantenimiento
        self.disponible = True  # Estado de disponibilidad
        self.dinero_recaudado = 0.0  # Dinero recaudado por la máquina
        self.precio_uso = precio_uso  # Precio por uso
        self.tipo = tipo  # Tipo de la máquina (ej. Arcade, Dance Dance)
        self.zona_de_juegos = None  # Zona de juegos a la que pertenece la máquina
        self.bono_activo = False  # Indica si el bono está activo
        if self not in Maquina.all_maquinas:
            Maquina.all_maquinas.append(self)  # Agrega la máquina a la lista global
    
    def get_usos(self):
        return self.usos  # Devuelve el número de usos
    
    def set_usos(self, usos):
        self.usos = usos  # Establece el número de usos
    
    def get_nombre(self):
        return self.nombre  # Devuelve el nombre de la máquina
    
    def esta_disponible(self):
        # Verifica si la máquina está disponible para su uso
        return not self.necesita_mantenimiento()
    
    def necesita_mantenimiento(self):
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
            self.dinero_recaudado += self.precio_uso
        elif self.necesita_mantenimiento():
            self.disponible = False
    
    def set_precio_uso(self, precio):
        self.precio_uso = precio  # Establece el precio por uso
    
    def get_precio_uso(self):
        return self.precio_uso  # Devuelve el precio por uso
    
    def reparar(self):
        # Resetea el contador de usos y vuelve la máquina disponible
        self.usos = 0
        self.disponible = True
    
    def get_dinero_recaudado(self):
        return self.dinero_recaudado  # Devuelve el dinero recaudado por la máquina
    
    def get_materiales_necesarios(self):
        return self.materiales_necesarios  # Devuelve la cantidad de materiales necesarios para el mantenimiento
    
    def get_tipo(self):
        return self.tipo  # Devuelve el tipo de la máquina
    
    def set_tipo(self, tipo):
        self.tipo = tipo  # Establece el tipo de la máquina
    
    def get_zona_de_juegos(self):
        return self.zona_de_juegos  # Devuelve la zona de juegos a la que pertenece la máquina
    
    def set_zona_de_juegos(self, zona_de_juegos):
        self.zona_de_juegos = zona_de_juegos  # Establece la zona de juegos de la máquina
    
    def activar_bono(self):
        self.bono_activo = True  # Activa el bono de la máquina
    
    def asignar_bono(self, cliente):
        # Asigna un bono al cliente basado en su tipo si el bono está activo
        if self.bono_activo:
            if cliente.get_tipo() == "Generico":
                cliente.set_saldo(cliente.get_saldo() + 5)  # Bono para cliente genérico
            elif cliente.get_tipo() == "Preferencial":
                cliente.set_saldo(cliente.get_saldo() + 12)  # Bono para cliente preferencial
            elif cliente.get_tipo() == "VIP":
                cliente.set_saldo(cliente.get_saldo() + 20)  # Bono para cliente VIP
        return f"Bono {cliente.get_tipo()} asignado a {cliente.get_nombre()}"
    
    @staticmethod
    def obtener_dos_maquinas_menos_venden():
        # Devuelve las dos máquinas que menos dinero han recaudado
        todas_las_maquinas = []
        
        for zona in ZonaDeJuegos.zonas_de_juegos:
            todas_las_maquinas.extend(zona.get_maquinas())
        
        todas_las_maquinas.sort(key=lambda maquina: maquina.get_dinero_recaudado())
        
        return todas_las_maquinas[:2]  # Devuelve las dos primeras máquinas de la lista ordenada
    
    def __str__(self):
        return f"Maquina: {self.nombre} Tipo: {self.tipo}, Recaudado: {self.dinero_recaudado}"
