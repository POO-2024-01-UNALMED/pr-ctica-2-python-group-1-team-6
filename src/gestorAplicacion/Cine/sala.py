class Sala:
    allSalas = []

    def __init__(self, numero, filas, columnas):
        # Inicializa la sala con el número, el tamaño y las sillas disponibles.
        self.numero = numero
        self.capacidad = filas * columnas
        self.sillas = [[True for _ in range(columnas)] for _ in range(filas)]
        self.cine = None
        
        if self not in Sala.allSalas:
            Sala.allSalas.append(self)
    
    def getNumero(self):
        return self.numero
    
    def setNumero(self, numero):
        self.numero = numero
    
    def getCine(self):
        return self.cine
    
    def setCine(self, cine):
        self.cine = cine
    
    def getSillas(self):
        return self.sillas
    
    def setSillas(self, sillas):
        self.sillas = sillas
    
    def hay_asientos_libres(self):
        # Verifica si hay al menos un asiento libre.
        for fila in self.sillas:
            if any(fila):
                return True
        return False
    
    def estado_silleteria(self):
        # Retorna una representación textual del estado de la silla en la sala.
        sala = ""
        columnas = "    " + "   ".join(str(i + 1) for i in range(len(self.sillas[0]))) + "\n"
        for j, fila in enumerate(self.sillas):
            sala += f"{j + 1}  " + " ".join("[ ]" if asiento else "[*]" for asiento in fila) + "\n"
        return columnas + sala
    
    def reservar_silla(self, fila, columna):
        # Intenta reservar un asiento en la fila y columna especificadas.
        if 0 <= fila < len(self.sillas) and 0 <= columna < len(self.sillas[fila]):
            if self.sillas[fila][columna]:
                self.sillas[fila][columna] = False
                return True
        return False
    
    def esta_disponible(self, fila, columna):
        # Verifica si el asiento en la fila y columna especificadas está disponible.
        if 0 <= fila < len(self.sillas) and 0 <= columna < len(self.sillas[fila]):
            return self.sillas[fila][columna]
        return False
    
    def __str__(self):
        return f"Sala: {self.numero}, Capacidad: {self.capacidad}"
