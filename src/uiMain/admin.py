import sys
from gestorAplicacion.Cine.cine import Cine
from interfaz import Interfaz
class Admin:
    @staticmethod
    def main():
        # Simula la entrada de datos del usuario
        def input_int(prompt):
            try:
                return int(input(prompt))
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                return -1
        
        Interfaz.crear_objetos()
        finalizar = False
        
        while not finalizar:
            print("-------Sistema para la compra de boletos de cine-----------")
            print("1.- Comprar boletos para un cine")
            print("2.- Gestionar Zona de Juegos")
            print("3.- Gestionar Peliculas")
            print("6. Comprar boleta para jugar maquinitas")
            print("7. Menu de Creacion")
            print("8. Asignaciones")
            print("9.- Terminar")
            print("Por favor elija la operación que desea hacer")
            
            opcion = input_int("Ingrese su opción: ")

            if opcion == 1:
                Interfaz.primera_operacion()
            elif opcion == 2:
                Interfaz.gestionar_zona_de_juegos()
            elif opcion == 3:
                Interfaz.gestionar_peliculas()
            elif opcion == 6:
                Interfaz.comprar_boleta_juegos()
            elif opcion == 7:
                Interfaz.creacion()
            elif opcion == 8:
                Interfaz.asignacion()
            elif opcion == 9:
                print("Hasta la próxima")
                sys.exit(0)
            else:
                print("El número ingresado debe estar entre 1 y 9")

# Asegúrate de que la clase `Interfaz` esté definida con los métodos necesarios.
class Interfaz:
    @staticmethod
    def crear_objetos():
        pass
    
    @staticmethod
    def primera_operacion():
        print("Has elegido la opción de comprar boleta.\nPor favor elige el cine:")
        cines = Cine.cines
        for i in range(len(cines)):
            print(str(i+1) + ".- " + cines[i].getNombre())
        cine = None
        while True:
            opcion = int(input("Ingrese su opción: "))
            if opcion > 0 and opcion <= len(cines):
                cine = cines[opcion-1]
                print("Has elegido el cine: " + cine.getNombre())
                break
            else:
                print("Opción inválida. Por favor ingrese un número válido.")
                continue
        print("Estas son las películas que están en nuestro poder:")
        peliculas = Cine.peliculas
        for i in range(len(peliculas)):
            print(str(i+1) + ".- " + peliculas[i].getNombre())
        print("Elige la que deseas ver")
        pelicula = None
        while True:
            opcion = int(input("Ingrese su opción: "))
            if opcion > 0 and opcion <= len(peliculas):
                pelicula = peliculas[opcion-1]
                print("Has elegido la película: " + pelicula.getNombre())
                break
            else:
                print("Opción inválida. Por favor ingrese un número válido.")
                continue
        
            
                
    @staticmethod
    def gestionar_zona_de_juegos():
        pass
    
    @staticmethod
    def gestionar_peliculas():
        pass
    
    @staticmethod
    def comprar_boleta_juegos():
        pass
    
    @staticmethod
    def creacion():
        pass
    
    @staticmethod
    def asignacion():
        pass

# Llama al método principal para ejecutar la aplicación
if __name__ == "__main__":
    Admin.main()
