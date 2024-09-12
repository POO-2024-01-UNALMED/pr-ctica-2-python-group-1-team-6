import sys
from interfaz import Interfaz
class Admin:
    @staticmethod
    def main():
        print("uwu")
        # Simula la entrada de datos del usuario
        def input_int(prompt):
            try:
                return int(input(prompt))
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                return -1
        
        
        finalizar = False
        
        while not finalizar:
            print("-------Sistema para la compra de boletos de cine-----------")
            print("1.- Comprar boletos para un cine")
            print("2.- Gestionar Zona de Juegos")
            print("3.- Gestionar Peliculas")
            print("5. Calificar Pelicula")
            print("6. Comprar boleta para jugar maquinitas")
            print("7. Menu de Creacion")
            print("8. Asignaciones")
            print("9.- Terminar")
            print("Por favor elija la operación que desea hacer")
            
            opcion = input_int("Ingrese su opción: ")

            if opcion == 1:
                Interfaz.primeraOperacion()
            elif opcion == 2:
                Interfaz.gestionarZonaDeJuegos()
            elif opcion == 3:
                Interfaz.gestionarPeliculas()
            elif opcion ==5:
                Interfaz.calificarPelicula()
            elif opcion == 6:
                Interfaz.comprarBoletaJuegos()
            elif opcion == 7:
                Interfaz.creacion()
            elif opcion == 8:
                Interfaz.asignacion()
            elif opcion == 9:
                print("Hasta la próxima")
                Interfaz.serializarTodo()
                sys.exit(0)
            else:
                print("El número ingresado debe estar entre 1 y 9")

if __name__ == "__main__":
    Interfaz.deserializarTodo()
    
    Admin.main()