from abc import ABC, abstractmethod

class Establecimiento(ABC):
    def __init__(self, nombre):
        # Atributo para almacenar el nombre del establecimiento
        self.nombre = nombre
        # Atributo para almacenar el dinero recaudado, inicializado en 0
        self.dinero_recaudado = 0

    def set_dinero_recaudado(self, dinero):
        # Método para establecer el dinero recaudado
        self.dinero_recaudado = dinero

    def get_dinero_recaudado(self):
        # Método para obtener el dinero recaudado
        return self.dinero_recaudado

    def get_nombre(self):
        # Método para obtener el nombre del establecimiento
        return self.nombre

    @abstractmethod
    def aplicar_promocion(self):
        # Método abstracto para aplicar una promoción, debe ser implementado en clases hijas
        pass

    def __str__(self):
        # Método para representar la clase como cadena, mostrando nombre y dinero recaudado
        return f"Establecimiento: {self.nombre}, Dinero Recaudado: {self.dinero_recaudado}"

class ZonaDeJuegos(Establecimiento):
    # Lista estática que almacena todas las instancias de ZonaDeJuegos
    zonas_de_juegos = []

    def __init__(self, nombre, horario):
        # Inicializa la clase padre Establecimiento
        super().__init__(nombre)
        self.horario = horario  # Horario de la zona de juegos
        self.maquinas = []  # Lista de máquinas en la zona de juegos
        self.cine = None  # Cine asociado a la zona de juegos
        if self not in ZonaDeJuegos.zonas_de_juegos:
            ZonaDeJuegos.zonas_de_juegos.append(self)

    def agregarMaquina(self, maquina):
        # Agrega una máquina a la lista y actualiza el dinero recaudado
        self.maquinas.append(maquina)
        maquina.set_zona_de_juegos(self)
        self.actualizar_dinero_recaudado()

    def actualizar_dinero_recaudado(self):
        # Actualiza el dinero recaudado sumando el de todas las máquinas
        total_recaudado = sum(maquina.get_dinero_recaudado() for maquina in self.maquinas)
        self.set_dinero_recaudado(total_recaudado)

    def get_maquinas(self):
        # Retorna la lista de máquinas
        return self.maquinas

    def get_maquinas_dañadas(self):
        # Retorna una lista de máquinas que necesitan mantenimiento
        return [maquina for maquina in self.maquinas if maquina.necesita_mantenimiento()]

    def informe_maquinas(self):
        # Genera un informe con el estado de todas las máquinas en la zona de juegos
        informe = f"Informe de la Zona de Juegos: {self.get_nombre()} {self.get_cine().get_nombre()}\n"
        informe += f"Horario: {self.horario}\n"
        for maquina in self.maquinas:
            estado = "Disponible" if maquina.esta_disponible() else "No Disponible"
            informe += f"{maquina.get_nombre()} - {estado}\n"
        return informe

    def mover_maquina(self, zona_destino, indice_maquina):
        # Mueve una máquina a otra zona de juegos
        maquina = self.maquinas.pop(indice_maquina)
        zona_destino.agregar_maquina(maquina)
        return f"La máquina {maquina.get_nombre()} ha sido movida a {zona_destino.get_nombre()}"

    def recomendar_movimiento(self, maquina_reparada):
        # Recomienda si se debe mover una máquina reparada a otra zona
        porcentaje_dependencia = (maquina_reparada.get_dinero_recaudado() / self.get_dinero_recaudado()) * 100

        # Verifica si la máquina es crucial para la zona actual
        if porcentaje_dependencia >= 70:
            return f"No se recomienda mover la máquina {maquina_reparada.get_nombre()} ya que representa el {porcentaje_dependencia:.2f}% de los ingresos de la zona actual."

        # Busca zonas candidatas para mover la máquina
        zonas_candidatas = [
            zona for zona in ZonaDeJuegos.zonas_de_juegos
            if self != zona and zona.get_dinero_recaudado() < self.get_dinero_recaudado() and
            not zona.tiene_maquina_del_tipo(maquina_reparada.get_tipo())
        ]

        # Si hay zonas candidatas, recomienda la mejor opción
        if zonas_candidatas:
            mejor_zona_destino = min(zonas_candidatas, key=lambda z: z.get_dinero_recaudado())
            return (f"Se recomienda mover la máquina {maquina_reparada.get_nombre()} "
                    f"a la zona {mejor_zona_destino.get_nombre()} ya que tiene menores ingresos "
                    f"y no cuenta con una máquina del tipo {maquina_reparada.get_tipo()}.")
        else:
            return (f"No se recomienda mover la máquina {maquina_reparada.get_nombre()}. "
                    "La zona actual tiene mejores ingresos o todas las otras zonas ya tienen una máquina del mismo tipo.")

    def tiene_maquina_del_tipo(self, tipo):
        # Verifica si la zona tiene una máquina del mismo tipo
        return any(maquina.get_tipo() == tipo for maquina in self.get_maquinas())

    def obtener_promedio_ingresos_maquinas(self):
        # Calcula el promedio de ingresos de las máquinas en la zona actual
        total_dinero_recaudado = sum(maquina.get_dinero_recaudado() for maquina in self.get_maquinas())
        numero_de_maquinas = len(self.get_maquinas())
        return total_dinero_recaudado / numero_de_maquinas if numero_de_maquinas > 0 else 0

    def tiene_maquina(self, tipo_maquina):
        # Verifica si la zona tiene una máquina del tipo especificado
        return any(maquina.get_tipo() == tipo_maquina for maquina in self.maquinas)

    def getCine(self):
        # Retorna el cine asociado a la zona de juegos
        return self.cine

    def setCine(self, cine):
        # Asocia un cine a la zona de juegos
        self.cine = cine

    def aplicar_promocion(self):
        # Implementación específica de la promoción en ZonaDeJuegos
        return f"Aplicando promoción en la zona de juegos {self.get_nombre()}."

    def __str__(self):
        # Representación en cadena de la zona de juegos
        return f"ZonaDeJuegos: {self.nombre}, Horario: {self.horario}, Máquinas: {len(self.maquinas)}"

class Bodega(Establecimiento):
    # Lista estática para almacenar todas las instancias de Bodega
    all_bodegas = []

    def __init__(self, nombre, materiales_disponibles):
        # Inicializa la clase padre Establecimiento
        super().__init__(nombre)
        # Atributo para almacenar la cantidad de materiales disponibles
        self.materiales_disponibles = materiales_disponibles
        # Agrega la instancia a la lista all_bodegas si no está ya presente
        if self not in Bodega.all_bodegas:
            Bodega.all_bodegas.append(self)

    def tiene_materiales_suficientes(self, cantidad_necesaria):
        # Verifica si hay suficientes materiales disponibles
        return self.materiales_disponibles >= cantidad_necesaria

    def usar_materiales(self, cantidad):
        # Disminuye la cantidad de materiales disponibles si hay suficientes
        if self.tiene_materiales_suficientes(cantidad):
            self.materiales_disponibles -= cantidad

    def recargar_materiales(self, cantidad, costo):
        # Recarga los materiales y descuenta el costo del dinero recaudado
        self.materiales_disponibles += cantidad
        self.set_dinero_recaudado(self.get_dinero_recaudado() - costo)

    def realizar_mantenimiento(self, zona, indice_maquina):
        # Obtiene la máquina seleccionada de la zona de juegos
        maquina_seleccionada = zona.get_maquinas_dañadas()[indice_maquina]
        
        # Si hay suficientes materiales, repara la máquina
        if self.tiene_materiales_suficientes(maquina_seleccionada.get_materiales_necesarios()):
            self.usar_materiales(maquina_seleccionada.get_materiales_necesarios())
            maquina_seleccionada.reparar()
            return f"La máquina {maquina_seleccionada.get_nombre()} ha sido reparada."
        else:
            return f"No hay suficientes materiales para reparar la máquina {maquina_seleccionada.get_nombre()}."

    def aplicar_promocion(self):
        # Implementación específica de la promoción en Bodega
        return f"Aplicando promoción en la bodega {self.get_nombre()}."

    def __str__(self):
        # Representación en cadena de la bodega
        return f"Bodega: {self.nombre}, Materiales disponibles {self.materiales_disponibles}"