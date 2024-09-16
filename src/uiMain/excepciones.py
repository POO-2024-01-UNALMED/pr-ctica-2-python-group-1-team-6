class ErrorAplicacion(Exception):
    def __init__(self, mensaje=""):
        super().__init__(f"Manejo de errores de la Aplicación: {mensaje}")

# Excepción de la Rama 1
class ExcepcionC1(ErrorAplicacion):
    def __init__(self, mensaje=""):
        super().__init__(f"ExceptionC1: {mensaje}")

# Excepción de la Rama 2
class ExcepcionC2(ErrorAplicacion):
    def __init__(self, mensaje=""):
        super().__init__(f"ExceptionC2: {mensaje}")

# Excepciones inventadas personalizadas para la Rama 1
class SaldoInsuficienteExcepcion(ExcepcionC1):
    def __init__(self,nombreU,cantidad):
        super().__init__(f"Saldo insuficiente para completar la operación.No tienes {cantidad}")
        self.nombreU=nombreU
        self.cantidad=cantidad
    
    def mensaje(self):
        print(f"{self.nombreU} no tines {self.cantidad}")

class AtributoNoneExcepcion(ExcepcionC1):
    def __init__(self):
        super().__init__("Intentaste acceder a un atributo con valor 'None'.")
    
    def manejar_error(self):
        print("Rutina de manejo para AtributoNoneException: Verifica que el atributo esté correctamente inicializado.")

# Excepciones inventadas personalizadas para la Rama 2
class DatoErroneoExcepcion(ExcepcionC2):
    def __init__(self,datosValidos,entrada):
        super().__init__(f"Ingresaste un dato erróneo en el criterio {entrada}")
        self.datosValidos=datosValidos
        self.entrada=entrada
    def mensaje(self):
        print(f"Ingresaste un dato erroneo en el criterio {self.entrada}, los datos adecuados son {self.datosValidos}")

# Excepción inventada adicional para la Rama 2
class ExcepcionInventada4(ExcepcionC2):
    def __init__(self):
        super().__init__("Error en la consulta de la base de datos.")
    
    def manejar_error(self):
        print("Rutina de manejo para ExceptionInventada4: Revisando consulta en la base de datos...")

# Excepciones sugeridas como parte de la Rama 1
class IndiceFueraDeRangoError(ExcepcionC1):
    def __init__(self):
        super().__init__("Se intentó acceder a un índice fuera del rango válido.")

# Excepciones sugeridas como parte de la Rama 2
class ExcepcionSugerida2(ExcepcionC2):
    def __init__(self):
        super().__init__("Excepción sugerida 2.")
    
    def manejarError(self):
        print("Rutina para ExceptionSugerida2.")