from establecimiento import Establecimiento

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

    def agregar_maquina(self, maquina):
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

    def get_cine(self):
        # Retorna el cine asociado a la zona de juegos
        return self.cine

    def set_cine(self, cine):
        # Asocia un cine a la zona de juegos
        self.cine = cine

    def aplicar_promocion(self):
        # Implementación específica de la promoción en ZonaDeJuegos
        return f"Aplicando promoción en la zona de juegos {self.get_nombre()}."

    def __str__(self):
        # Representación en cadena de la zona de juegos
        return f"ZonaDeJuegos: {self.nombre}, Horario: {self.horario}, Máquinas: {len(self.maquinas)}"
