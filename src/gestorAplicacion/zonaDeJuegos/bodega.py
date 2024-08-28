from establecimiento import Establecimiento

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

