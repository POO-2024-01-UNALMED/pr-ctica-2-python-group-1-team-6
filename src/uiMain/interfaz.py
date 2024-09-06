import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.gestorAplicacion.Cine.cine import Cine
from src.gestorAplicacion.Cine.cliente import Cliente
from src.gestorAplicacion.Cine.sala import Sala
from src.gestorAplicacion.Cine.pelicula import Pelicula
from src.gestorAplicacion.Cine.funcion import Funcion
from src.gestorAplicacion.zonaDeJuegos.establecimiento import *
from src.gestorAplicacion.zonaDeJuegos.maquina import Maquina




from datetime import time,datetime

class Interfaz:

    
    def crearObjetos(cls):
        print("1")
        # Crear instancias de máquinas
        cls.arcade1 = Maquina("Arcade1", "Arcade", 10, 20)
        cls.arcade2 = Maquina("Arcade2", "Arcade", 10, 20)
        cls.danceDance1 = Maquina("Dance Dance1", "Dance Dance", 12, 20)
        cls.mesaDeDiscos1 = Maquina("Mesa de discos1", "Mesa de discos", 12, 20)
        cls.mesaDeDiscos2 = Maquina("Mesa de discos2", "Mesa de discos", 12, 20)
        cls.boxing1 = Maquina("Boxing1", "Boxing", 8, 20)
        cls.basket1 = Maquina("Basket1", "Basket", 11, 20)

        # Crear instancias de zonas de juegos
        cls.zona1 = ZonaDeJuegos("Zona 1", "08:00 AM - 07:00 PM")
        cls.zona2 = ZonaDeJuegos("Zona 2", "09:00 AM - 08:00 PM")
        cls.zona3 = ZonaDeJuegos("Zona 3", "08:00 AM - 08:00 PM")
        cls.zona4 = ZonaDeJuegos("Zona 4", "10:00 AM - 07:00 PM")

        # Crear una instancia de bodega
        cls.bodega = Bodega("Bodega Central", 100)

        # Crear instancias de películas
        cls.pelicula1 = Pelicula("Intensamente", "Infantil", time(1, 35))
        cls.pelicula2 = Pelicula("Spiderman", "Acción", time(2, 10))
        cls.pelicula3 = Pelicula("Jason Vorhees", "Terror", time(1, 45))
        cls.pelicula4 = Pelicula("Deadpool", "+18", time(1, 50))
        cls.pelicula5 = Pelicula("Oppenheimer", "Drama", time(3, 0))
        cls.pelicula6 = Pelicula("Los Minions", "Infantil", time(1, 30))
        cls.pelicula7 = Pelicula("Toy Story", "Infantil", time(1, 40))
        cls.pelicula8 = Pelicula("El Conjuro", "Terror", time(1, 52))
        cls.pelicula9 = Pelicula("Inception", "Acción", time(2, 28))

        # Crear instancias de salas
        cls.sala1 = Sala(1, 6, 5)
        cls.sala2 = Sala(2, 8, 6)
        cls.sala3 = Sala(3, 9, 8)
        cls.sala4 = Sala(4, 7, 6)
        cls.sala5 = Sala(5, 9, 7)
        cls.sala6 = Sala(6, 5, 5)
        cls.sala7 = Sala(7, 8, 5)
        cls.sala8 = Sala(8, 9, 9)
        cls.sala9 = Sala(9, 7, 8)
        cls.sala10 = Sala(10, 9, 8)
        cls.sala11 = Sala(11, 6, 6)
        cls.sala12 = Sala(12, 8, 7)
        cls.sala13 = Sala(13, 8, 9)
        cls.sala14 = Sala(14, 7, 7)
        cls.sala15 = Sala(15, 9, 9)
        cls.sala16 = Sala(16, 9, 8)
        cls.sala17 = Sala(17, 8, 6)
        cls.sala18 = Sala(18, 5, 5)
        cls.sala19 = Sala(19, 7, 6)
        cls.sala20 = Sala(20, 8, 8)
        cls.sala21 = Sala(21, 6, 6)
        cls.sala22 = Sala(22, 8, 7)
        cls.sala23 = Sala(23, 8, 9)
        cls.sala24 = Sala(24, 9, 8)
        cls.sala25 = Sala(25, 9, 9)

        # Crear instancias de funciones
        cls.funcion1 = Funcion("Normal",cls.pelicula1, cls.sala1, 45000)
        cls.funcion2 = Funcion("Normal",cls.pelicula2,cls.sala2, 25000)
        cls.funcion3 = Funcion("Normal",cls.pelicula3, cls.sala3, 30000)
        cls.funcion4 = Funcion("Normal",cls.pelicula4, cls.sala4, 40000)
        cls.funcion5 = Funcion("Normal",cls.pelicula5, cls.sala5, 50000)
        cls.funcion6 = Funcion("Normal",cls.pelicula6, cls.sala6, 12000)
        cls.funcion7 = Funcion("Normal",cls.pelicula7, cls.sala7, 22000)
        cls.funcion8 = Funcion("Normal",cls.pelicula8,cls.sala8, 280)
        cls.funcion9 = Funcion("Normal",cls.pelicula9, cls.sala9, 350)
        cls.funcion10 = Funcion("Normal",cls.pelicula1, cls.sala10, 190)
        cls.funcion11 = Funcion("Normal",cls.pelicula3, cls.sala11, 270)
        cls.funcion12 = Funcion("Normal",cls.pelicula7, cls.sala12, 230)
        cls.funcion13 = Funcion("Normal",cls.pelicula4, cls.sala13, 410)
        cls.funcion14 = Funcion("Normal",cls.pelicula2, cls.sala14, 260)
        cls.funcion15 = Funcion("Normal",cls.pelicula5, cls.sala15, 500)
        cls.funcion16 = Funcion("Normal",cls.pelicula8, cls.sala16, 300)
        cls.funcion17 = Funcion("Normal",cls.pelicula9, cls.sala17, 340)
        cls.funcion18 = Funcion("Normal",cls.pelicula6, cls.sala18, 130)
        cls.funcion19 = Funcion("Normal",cls.pelicula7, cls.sala19, 200)
        cls.funcion20 = Funcion("Normal",cls.pelicula9, cls.sala20, 330)
        cls.funcion21 = Funcion("Normal",cls.pelicula6, cls.sala21, 140)
        cls.funcion22 = Funcion("Normal",cls.pelicula7, cls.sala22, 210)
        cls.funcion23 = Funcion("Normal",cls.pelicula3, cls.sala23, 300)
        cls.funcion24 = Funcion("Normal",cls.pelicula4, cls.sala24, 420)
        cls.funcion25 = Funcion("Normal",cls.pelicula5, cls.sala25, 480)

        # Crear instancias de cines
        cls.cine1 = Cine("Cine A", cls.zona1)
        cls.cine2 = Cine("Cine B", cls.zona2)
        cls.cine3 = Cine("Cine C", cls.zona3)
        cls.cine4 = Cine("Cine D", cls.zona4)
        
    
    def asignarObjetos(cls):
        print("2")
        # Asignación de salas a cines
        cls.sala1.setCine(cls.cine1)
        cls.sala2.setCine(cls.cine2)
        cls.sala3.setCine(cls.cine3)

        # Asignación de funciones a días específicos en cine1
        cls.cine1.agregarFuncion(cls.funcion1, cls.cine1.getLunes())  # Infantil: "Intensamente"
        cls.cine1.agregarFuncion(cls.funcion6, cls.cine1.getLunes())  # Infantil: "Los Minions"
        cls.cine1.agregarFuncion(cls.funcion7, cls.cine1.getLunes())  # Infantil: "Toy Story"
        cls.cine2.agregarFuncion(cls.funcion2, cls.cine2.getLunes())  # Acción: "Spiderman" (8 am)

        cls.cine2.agregarFuncion(cls.funcion4, cls.cine2.getMartes())  # +18: "Deadpool" (8 am)
        cls.cine2.agregarFuncion(cls.funcion5, cls.cine2.getMartes())  # Drama: "Oppenheimer" (10 am)

        cls.cine2.agregarFuncion(cls.funcion3, cls.cine2.getJueves())  # Terror: "Jason Vorhees" (8 am)
        cls.cine3.agregarFuncion(cls.funcion8, cls.cine3.getJueves())  # Terror: "El Conjuro" (10 am)

        cls.cine3.agregarFuncion(cls.funcion9, cls.cine3.getViernes())  # Acción: "Inception" (8 am)
        cls.cine3.agregarFuncion(cls.funcion5, cls.cine3.getViernes())  # Drama: "Oppenheimer" (12 pm)
        cls.cine3.agregarFuncion(cls.funcion4, cls.cine3.getViernes())  # +18: "Deadpool" (4 pm)

        cls.cine4.agregarFuncion(cls.funcion9, cls.cine4.getSabado())  # Acción: "Inception" (8 am)
        cls.cine4.agregarFuncion(cls.funcion3, cls.cine4.getSabado())  # Terror: "Jason Vorhees" (11 am)

        print(Funcion.obtenerIndiceEnDia(cls.funcion1))
        print(Funcion.obtenerIndiceEnDia(cls.funcion6))
        print(Funcion.obtenerIndiceEnDia(cls.funcion7))
        print(Funcion.obtenerIndiceEnDia(cls.funcion2))
        print(Funcion.obtenerIndiceEnDia(cls.funcion4))
        print(Funcion.obtenerIndiceEnDia(cls.funcion5))
        print(Funcion.obtenerIndiceEnDia(cls.funcion3))
        print(Funcion.obtenerIndiceEnDia(cls.funcion8))
        print(Funcion.obtenerIndiceEnDia(cls.funcion9))
        
        # Asignación de máquinas a zonas de juegos
        cls.zona1.agregarMaquina(cls.arcade1)
        cls.zona1.agregarMaquina(cls.danceDance1)
        cls.zona1.agregarMaquina(cls.mesaDeDiscos1)
        cls.zona2.agregarMaquina(cls.arcade2)
        cls.zona2.agregarMaquina(cls.boxing1)
        cls.zona2.agregarMaquina(cls.mesaDeDiscos2)
        cls.zona3.agregarMaquina(cls.basket1)

        for i in range(0, 13):
             cls.arcade1.usar()
        for i in range(0, 11):
            cls.danceDance1.usar()
        for i in range(0, 11):
            cls.basket1.usar()
        
        cls.funcion1.getPelicula().setCalificacionPromedio(4.0)
        cls.funcion2.getPelicula().setCalificacionPromedio(3.0)
        cls.funcion3.getPelicula().setCalificacionPromedio(2.0)
        cls.funcion4.getPelicula().setCalificacionPromedio(1.5)
        cls.funcion5.getPelicula().setCalificacionPromedio(4.5)
        cls.funcion6.getPelicula().setCalificacionPromedio(5.0)
        cls.funcion7.getPelicula().setCalificacionPromedio(3.5)
        cls.funcion8.getPelicula().setCalificacionPromedio(2.5)
        cls.funcion9.getPelicula().setCalificacionPromedio(4.0)
        cls.funcion10.getPelicula().setCalificacionPromedio(3.0)
        cls.funcion11.getPelicula().setCalificacionPromedio(2.8)
        cls.funcion12.getPelicula().setCalificacionPromedio(3.9)
        cls.funcion13.getPelicula().setCalificacionPromedio(1.8)
        cls.funcion14.getPelicula().setCalificacionPromedio(3.4)
        cls.funcion15.getPelicula().setCalificacionPromedio(4.2)
        cls.funcion16.getPelicula().setCalificacionPromedio(2.9)
        cls.funcion17.getPelicula().setCalificacionPromedio(4.1)
        cls.funcion18.getPelicula().setCalificacionPromedio(4.3)
        cls.funcion19.getPelicula().setCalificacionPromedio(3.8)
        cls.funcion20.getPelicula().setCalificacionPromedio(3.1)
        cls.funcion21.getPelicula().setCalificacionPromedio(4.4)
        cls.funcion22.getPelicula().setCalificacionPromedio(4.6)
        cls.funcion23.getPelicula().setCalificacionPromedio(2.7)
        cls.funcion24.getPelicula().setCalificacionPromedio(2.6)
        cls.funcion25.getPelicula().setCalificacionPromedio(4.5)
                
        


    @staticmethod
    def error():
     print("Error")

# Gestiona la zona de juegos
    @staticmethod
    def gestionarZonaDeJuegos():
    # Simula la entrada del usuario
        entrada = input

    # Actualización de dinero recaudado en todas las zonas
        for zona in ZonaDeJuegos.zonasDeJuegos:
            zona.actualizarDineroRecaudado()

    # Mostrar informe de máquinas dañadas en cada zona
        print("Informe de máquinas dañadas:")
        for zona in ZonaDeJuegos.zonasDeJuegos:
            print(zona.informeMaquinas())

    # Selección de zona y máquina para reparar
        print("Seleccione el número de la zona de la máquina que desea reparar: ")
        for i, zona in enumerate(ZonaDeJuegos.zonasDeJuegos):
            print(f"{i + 1}. {zona.getNombre()}")
        zonaSeleccionada = int(entrada()) - 1

        zonaActual = ZonaDeJuegos.zonasDeJuegos[zonaSeleccionada]
        maquinasDañadas = zonaActual.getMaquinasDañadas()
        if not maquinasDañadas:
            print("No hay máquinas dañadas en la zona seleccionada.")
            return

        print("Seleccione el número de la máquina que desea reparar:")
        for i, maquina in enumerate(maquinasDañadas):
            print(f"{i + 1}. {maquina.getNombre()}")
        seleccionMaquina = int(entrada()) - 1

    # Realizar reparación
        print(Interfaz.bodega.realizarMantenimiento(zonaActual, seleccionMaquina))

    # Recomendación de movimiento
        maquinaReparada = maquinasDañadas[seleccionMaquina]
        print(zonaActual.recomendarMovimiento(maquinaReparada))

    # Selección de zona de destino para mover la máquina reparada
        print("Seleccione la zona a la que desea mover la máquina:")
        for i, zona in enumerate(ZonaDeJuegos.zonasDeJuegos):
            print(f"{i + 1}. {zona.getNombre()}")
        seleccionZona = int(entrada()) - 1

        zonaDestino = ZonaDeJuegos.zonasDeJuegos[seleccionZona]
        if zonaActual != zonaDestino:
            print(zonaActual.moverMaquina(zonaDestino, seleccionMaquina))
        else:
            print(f"La máquina permanecerá en {zonaActual.getNombre()}")

    # Aplicar incentivos
        print("¿Desea aplicar algún incentivo en una zona de juegos?")
        print("1. Sí")
        print("2. No")
        opcionIncentivo = int(entrada())

        if opcionIncentivo == 1:
            print("Seleccione el tipo de incentivo:")
            print("1. Rebajar el precio de una máquina")
            print("2. Regalar un bono por el uso de una máquina")
            tipoIncentivo = int(entrada())

        if tipoIncentivo == 1:
            dosMenosVenden = Maquina.obtenerDosMaquinasMenosVenden()

            if not dosMenosVenden:
                print("No hay máquinas disponibles para recomendar.")
            else:
                print("Recomendación de cambio de precio:")
                for maquina in dosMenosVenden:
                    print(maquina)

            print("Seleccione la zona donde aplicar la rebaja:")
            for i, zona in enumerate(ZonaDeJuegos.zonasDeJuegos):
                print(f"{i + 1}. {zona.getNombre()}")
            seleccionZonaRebaja = int(entrada()) - 1

            zonaRebaja = ZonaDeJuegos.zonasDeJuegos[seleccionZonaRebaja]

            print("Seleccione la máquina para rebajar su precio:")
            maquinasEnZona = zonaRebaja.getMaquinas()
            for i, maquina in enumerate(maquinasEnZona):
                print(f"{i + 1}. {maquina.getNombre()}")
            seleccionMaquinaRebaja = int(entrada()) - 1

            maquinaRebajada = maquinasEnZona[seleccionMaquinaRebaja]
            nuevoPrecio = float(input(f"Introduzca el nuevo precio para la máquina {maquinaRebajada.getNombre()}: "))
            maquinaRebajada.setPrecioUso(nuevoPrecio)

            print(f"El precio de la máquina {maquinaRebajada.getNombre()} ha sido rebajado a {nuevoPrecio}")

        elif tipoIncentivo == 2:
            print("Seleccione la zona de juegos:")
            for i, zona in enumerate(ZonaDeJuegos.zonasDeJuegos):
                print(f"{i + 1}. {zona.getNombre()}")
            zonaSeleccionada1 = int(entrada()) - 1

            zona = ZonaDeJuegos.zonasDeJuegos[zonaSeleccionada1]

            print("Seleccione la máquina a la que desea aplicar el bono:")
            for i, maquina in enumerate(zona.getMaquinas()):
                print(f"{i + 1}. {maquina.getNombre()}")
            maquinaSeleccionada = int(entrada()) - 1

            maquina = zona.getMaquinas()[maquinaSeleccionada]
            maquina.activarBono()

            print(f"El bono ha sido activado para la máquina {maquina.getNombre()}")

        else:
            print("No se aplicarán incentivos.")

    # Actualización final de dinero recaudado
        for zona in ZonaDeJuegos.zonasDeJuegos:
            zona.actualizarDineroRecaudado()
            print(f"Dinero recaudado por {zona.getNombre()}: {zona.getDineroRecaudado()}")
    

    @staticmethod
    def gestionarPeliculas():
        # Paso 1: Ver las calificaciones
        print("Calificaciones de las películas en los cines:")
        for cine in Cine.cines:
            print("Cine:", cine.getNombre())
            calificaciones = cine.obtenerCalificacionesPeliculas()
            for calificacion in calificaciones:
                print(calificacion)

        # Paso 2: Selección de cine y película por parte del usuario
        print("Seleccione el cine de la película que desea intercambiar:")
        for i, cine in enumerate(Cine.cines):
            print(f"{i + 1}. {cine.getNombre()}")
        cineSeleccionado = int(input()) - 1
        cineOrigen = Cine.cines[cineSeleccionado]

        # Mostrar películas en el cine seleccionado
        print("Seleccione la película que desea intercambiar:")
        peliculas = cineOrigen.peliculasActivas()
        for i, pelicula in enumerate(peliculas):
            print(f"{i + 1}. {pelicula.getTitulo()}")
        peliculaSeleccionada = int(input()) - 1
        peliculaAIntercambiar = peliculas[peliculaSeleccionada]

        # Paso 3: Recomendar una película para intercambio basada en la selección
        print(Pelicula.recomendarIntercambio(peliculaAIntercambiar))

        # Paso 4: Selección del nuevo cine para el intercambio
        print("Seleccione el nuevo cine (omitido el cine actual):")
        for i, cine in enumerate(Cine.cines):
            if i != cineSeleccionado:
                print(f"{i + 1}. {cine.getNombre()}")
        nuevoCineSeleccionado = int(input()) - 1
        nuevoCine = Cine.cines[nuevoCineSeleccionado]

        # Mostrar películas en el nuevo cine seleccionado
        print("Seleccione la película con la que desea intercambiar:")
        peliculasNuevoCine = nuevoCine.peliculasActivas()
        for i, pelicula in enumerate(peliculasNuevoCine):
            print(f"{i + 1}. {pelicula.getTitulo()}")
        peliculaIntercambioSeleccionada = int(input()) - 1

        # Manejar la opción de no intercambiar
        if peliculaIntercambioSeleccionada == -1:
            print("No se realizará el intercambio.")
            return

        peliculaIntercambio = peliculasNuevoCine[peliculaIntercambioSeleccionada]

        # Confirmar el intercambio
        print(f"¿Desea realizar el intercambio entre {peliculaAIntercambiar.getTitulo()} y {peliculaIntercambio.getTitulo()}? (1. Sí / 2. No)")
        realizarIntercambio = int(input())

        if realizarIntercambio == 1 and peliculaAIntercambiar and peliculaIntercambio and peliculaAIntercambiar != peliculaIntercambio:
            resultadoIntercambio = Funcion.realizarIntercambio(peliculaAIntercambiar, peliculaIntercambio)
            print(resultadoIntercambio)
        else:
            print("No se realizó el intercambio.")

        # Paso 5: Aplicar bonos o descuentos
        print("¿Desea aplicar algún incentivo para la nueva película?")
        print("1. Rebajar el precio de la entrada")
        print("2. Regalar un bono")
        print("3. No aplicar incentivos")
        tipoIncentivo = int(input())

        if tipoIncentivo == 1:
            # Aplicar rebaja en el precio de la entrada
            print("Seleccione la función para la película a la que desea aplicar el nuevo precio:")
            funciones = peliculaIntercambio.getFunciones()
            for i, funcion in enumerate(funciones):
                print(f"{i + 1}. {funcion}")  # Asumiendo que la función tiene un método __str__ para mostrar información relevante
            funcionSeleccionada = int(input()) - 1

            if 0 <= funcionSeleccionada < len(funciones):
                funcion = funciones[funcionSeleccionada]
                nuevoPrecio = float(input("Introduzca el nuevo precio para la entrada: "))
                funcion.setPrecio(nuevoPrecio)
                print(f"El precio de entrada ha sido rebajado a {nuevoPrecio}")
            else:
                print("Selección de función inválida.")

        elif tipoIncentivo == 2:
            # Aplicar bono
            print("Seleccione el cine para aplicar el bono:")
            for i, cine in enumerate(Cine.cines):
                print(f"{i + 1}. {cine.getNombre()}")
            cineSeleccionado = int(input()) - 1
            cine = Cine.cines[cineSeleccionado]

            # Seleccionar la película en la que se desea aplicar el bono
            print("Seleccione la película a la que desea aplicar el bono:")
            peliculas = cine.peliculasActivas()
            for i, pelicula in enumerate(peliculas):
                print(f"{i + 1}. {pelicula.getTitulo()}")
            peliculaSeleccionada = int(input()) - 1
            pelicula = peliculas[peliculaSeleccionada]

            # Activar el bono en la película seleccionada
            pelicula.activarBono()
            print(f"El bono ha sido activado para la película {pelicula.getTitulo()}")

        elif tipoIncentivo == 3:
            print("No se aplicarán incentivos.")
        else:
            print("Opción no válida.")
    @staticmethod
    def comprarBoletaJuegos():
    # Paso 1: Identificación del cliente
        idCliente = int(input("Ingrese su número de identificación: "))
        cliente = Cliente.buscarClientePorId(idCliente)

        if cliente is None:
            respuesta = int(input("Cliente no encontrado. ¿Desea crear uno nuevo? (1)Sí/(2)No: "))
            if respuesta == 1:
                nombre = input("Ingresa tu nombre: ")  # Captura el nombre completo
                saldoInicial = float(input("Ingresa tu saldo inicial: "))  # Captura el saldo inicial
                cliente = Cliente(nombre, saldoInicial, idCliente)  # Crea el nuevo cliente
                print("Cliente creado exitosamente.")

            elif respuesta == 2:
                return
            else:
                print("Selección inválida. Por favor, seleccione un número válido.")
                return  # Sale del método si la selección es inválida

        # Paso 2: Selección del cine
        print("Seleccione el cine:")
        for i, cine in enumerate(Cine.cines):
         print(f"{i + 1}. {cine.getNombre()}")  # Lista los cines disponibles
        cineSeleccionadoIndex = int(input()) - 1
        cineSeleccionado = Cine.cines[cineSeleccionadoIndex]

    # Paso 3: Selección de la máquina en la zona de juegos
        zonaDeJuegosSeleccionada = cineSeleccionado.getZonaDeJuegos()  # Obtener la zona de juegos del cine
        maquinasDisponibles = zonaDeJuegosSeleccionada.getMaquinas()

        print("Seleccione la máquina para comprar la boleta:")
        for i, maquina in enumerate(maquinasDisponibles):
            print(f"{i + 1}. {maquina.getNombre()} - Precio: {maquina.getPrecioUso()}")  # Lista las máquinas disponibles
        maquinaSeleccionadaIndex = int(input()) - 1
        maquinaSeleccionada = maquinasDisponibles[maquinaSeleccionadaIndex]

    # Verificar si la máquina requiere mantenimiento
        if maquinaSeleccionada.necesitaMantenimiento():
            print(f"La máquina {maquinaSeleccionada.getNombre()} no está disponible debido a que requiere mantenimiento.")
            return

    # Paso 4: Realizar la compra
        if cliente.getSaldo() >= maquinaSeleccionada.getPrecioUso():
            cliente.setSaldo(cliente.getSaldo() - maquinaSeleccionada.getPrecioUso())  # Descuenta el precio de la máquina del saldo del cliente
            maquinaSeleccionada.usar()  # Registra el uso de la máquina
            print("Compra realizada exitosamente.")

        # Paso 5: Asignar bono si está activo
            print(maquinaSeleccionada.asignarBono(cliente))  # Asigna un bono si es aplicable

        # Paso 6: Imprimir recibo
            print("Recibo:")
            print(f"Cliente: {cliente.getIdentificacion()}")
            print(f"Tipo de cliente: {cliente.getTipo()}")
            print(f"Máquina: {maquinaSeleccionada.getNombre()}")
            print(f"Precio pagado: {maquinaSeleccionada.getPrecioUso()}")
            print(f"Saldo restante: {cliente.getSaldo()}")
        else:
            print("Saldo insuficiente.")
    
    @staticmethod
    def creacion():
        continuar = True
        while continuar:
            print("Menú de creación de instancias:")
            print("1. Crear Zona de Juegos")
            print("2. Crear Bodega")
            print("3. Crear Máquina")
            print("4. Crear Cliente")
            print("5. Crear Cine")
            print("6. Crear Película")
            print("7. Crear Sala")
            print("8. Crear Función")
            print("9. Salir")
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                nombreZona = input("Ingresa el nombre de la Zona de Juegos: ")
                horario = input("Ingresa el horario de la Zona de Juegos: ")
                zona = ZonaDeJuegos(nombreZona, horario)
                print(f"Zona de Juegos creada: {zona}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 2:
                nombreBodega = input("Ingresa el nombre de la Bodega: ")
                materiales = int(input("Ingrese la cantidad inicial de materiales: "))
                bodega = Bodega(nombreBodega, materiales)
                print(f"Bodega creada: {bodega}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 3:
                nombreMaquina = input("Ingresa el nombre de la Máquina: ")
                print("Ingresa el tipo de la Máquina")
                print("1. Arcade")
                print("2. Dance Dance")
                print("3. Mesa de discos")
                print("4. Boxing")
                print("5. Basket")
                tipoMaquina = int(input("Selecciona una opción: "))
                if tipoMaquina==1:
                    tipo="Arcade"
                elif tipoMaquina==2:
                    tipo="Dance Dance"
                elif tipoMaquina==3:
                    tipo="Mesa de discos"
                elif tipoMaquina==4:
                    tipo="Boxing"
                elif tipoMaquina==5:
                    tipo="Basket"
                else:
                    Interfaz.error()

                materialesNecesarios = int(input("Ingresa la cantidad de materiales necesarios para la Máquina: "))
                precioMaquina = float(input("Ingresa el precio de la Máquina: "))
                maquina = Maquina(nombreMaquina, tipo, materialesNecesarios, precioMaquina)
                print(f"Máquina creada: {maquina}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 4:
                nombreCliente = input("Ingresa el nombre del Cliente: ")
                saldo = float(input("Ingresa el saldo inicial del Cliente: "))
                idCliente = int(input("Ingresa el número de identificación del Cliente: "))
                cliente = Cliente(nombreCliente, saldo, idCliente)
                print(f"Cliente creado: {cliente}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 5:
                nombreCine = input("Ingresa el nombre del Cine: ")
                cine = Cine(nombreCine)
                print(f"Cine creado: {cine}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 6:
                tituloPelicula = input("Ingresa el título de la Película: ")
                print("Ingresa el género de la Película")
                print("1. Acción")
                print("2. Infantil")
                print("3. Terror")
                print("4. +18")
                print("5. Drama")
                generoPelicula = int(input("Selecciona una opción: "))
                if generoPelicula==1:
                    genero="Accion"
                elif generoPelicula==2:
                    genero="Infantil"
                elif generoPelicula==3:
                    genero="Terror"
                elif generoPelicula==4:
                    genero="+18"
                elif generoPelicula==5:
                    genero="Drama"
                else:
                    Interfaz.error()

                duracionInput = input("Ingresa la duración de la Película (en horas y minutos, formato HH:MM): ")
                try:
                    duracion = datetime.strptime(duracionInput, "%H:%M").time()
                except ValueError:
                    print("Formato de tiempo inválido. Usa el formato HH:MM.")
                    continue  # Volver al menú si la duración es inválida

                pelicula = Pelicula(tituloPelicula, genero, duracion)
                print(f"Película creada exitosamente: {pelicula.titulo}, Género: {pelicula.genero}, Duración: {pelicula.duracion}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 7:
                numeroSala = int(input("Ingresa el número de la Sala: "))
                filas = int(input("Ingresa el número de filas de la Sala: "))
                columnas = int(input("Ingresa el número de columnas de la Sala: "))
                sala = Sala(numeroSala, filas, columnas)
                print(f"Sala creada: {sala}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 8:
                print("Ingresa el tipo de Función:")
                print("1. Normal")
                print("2. VIP")
                eleccionTipo = int(input("Selecciona una opción: "))
                if eleccionTipo==1:
                    tipoFuncion="Normal"
                elif eleccionTipo==2:
                    tipoFuncion="VIP"
                else:
                    Interfaz.error()
                funcion = Funcion(tipoFuncion)
                print(f"Función creada: {funcion}")
                continuar = Interfaz.verificarContinuar()

            elif opcion == 9:
                continuar = False
                print("Saliendo del menú de creación.")

            else:
                print("Opción inválida. Inténtalo de nuevo.")
    
    @staticmethod
    def verificarContinuar():
        respuesta = int(input("¿Desea hacer otra creación? 1. Sí | 2. No: "))
        if respuesta == 2:
            return False
        elif respuesta == 1:
            return True
        else:
            print("Selección inválida.")
            return False
    
    
    @staticmethod
    def asignacion():
        continuar = True

        while continuar:
        # Mostrar el menú de opciones
            print("Menú de Asignaciones:")
            print("1. Asignar una zona de juegos a un cine")
            print("2. Agregar una función a un cine")
            print("3. Agregar una máquina a una zona de juegos")
            print("4. Asignar una película a una función")
            print("5. Asignar una sala a una función")
            print("6. Salir")

            opcion = int(input("Elige una opción: "))
        
            # Evaluar la opción seleccionada por el usuario
            if opcion == 1:
                # Asignar una zona de juegos a un cine
                if not ZonaDeJuegos.zonasDeJuegos:
                    print("No hay zonas de juegos disponibles.")
                    continue
                if not Cine.cines:
                    print("No hay cines disponibles.")
                    continue

                # Mostrar lista de zonas de juegos disponibles
                print("Selecciona la zona de juegos a asignar:")
                for i, zona in enumerate(ZonaDeJuegos.zonasDeJuegos):
                    print(f"{i}. {zona.getNombre()}")

                zonaSeleccionada = int(input())

                # Mostrar lista de cines disponibles
                print("Selecciona el cine al que deseas asignar la zona de juegos:")
                for i, cine in enumerate(Cine.cines):
                    print(f"{i}. {cine.getNombre()}")

                cineSeleccionado = int(input())

                # Asignar la zona de juegos seleccionada al cine
                Cine.cines[cineSeleccionado].setZonaDeJuegos(ZonaDeJuegos.zonasDeJuegos[zonaSeleccionada])
                ZonaDeJuegos.zonasDeJuegos[zonaSeleccionada].setCine(Cine.cines[cineSeleccionado])
                print(f"Zona de juegos asignada correctamente al cine {Cine.cines[cineSeleccionado].getNombre()}")

            elif opcion == 2:
                # Agregar una función a un cine
                if not Funcion.allFunciones:
                    print("No hay funciones disponibles.")
                    continue
                if not Cine.cines:
                    print("No hay cines disponibles.")
                    continue

                # Seleccionar la función que se desea agregar
                print("Selecciona la función para reemplazar en un cine:")
                for i, funcion in enumerate(Funcion.allFunciones):
                    if funcion.getPelicula():
                        print(f"{i}. {funcion.getPelicula().getTitulo()}  {funcion.getHoraInicio()}  {funcion.getTipo()}")
                    else:
                        print(f"{i}. Función sin película asignada  {funcion.getHoraInicio()}  {funcion.getTipo()}")

                funcionSeleccionada = int(input())

                # Seleccionar el cine
                print("Selecciona el cine donde deseas reemplazar la función:")
                for i, cine in enumerate(Cine.cines):
                    print(f"{i}. {cine.getNombre()}")

                cineSeleccionado1 = int(input())

                # Seleccionar el día de la semana
                print("Selecciona el día de la semana para reemplazar la función:")
                print("1. Lunes")
                print("2. Martes")
                print("3. Jueves")
                print("4. Viernes")
                print("5. Sábado")
                diaSeleccionado = int(input())

                diaSeleccionadoLista = None
                if diaSeleccionado == 1:
                    diaSeleccionadoLista = Cine.cines[cineSeleccionado1].getLunes()
                elif diaSeleccionado == 2:
                    diaSeleccionadoLista = Cine.cines[cineSeleccionado1].getMartes()
                elif diaSeleccionado == 3:
                    diaSeleccionadoLista = Cine.cines[cineSeleccionado1].getJueves()
                elif diaSeleccionado == 4:
                    diaSeleccionadoLista = Cine.cines[cineSeleccionado1].getViernes()
                elif diaSeleccionado == 5:
                    diaSeleccionadoLista = Cine.cines[cineSeleccionado1].getSabado()
                else:
                    print("Día inválido.")
                    continue

                if diaSeleccionadoLista:
                    # Mostrar funciones actuales del día seleccionado
                    print("Selecciona la posición de la función que deseas reemplazar:")
                    for i, funcion in enumerate(diaSeleccionadoLista):
                        if funcion and funcion.getPelicula():
                            print(f"{i}. {funcion.getPelicula().getTitulo()}  {funcion.getHoraInicio()}")
                        else:
                            print(f"{i}. Función vacía")

                    posicionSeleccionada = int(input())

                    # Reemplazar la función en la posición seleccionada
                    if 0 <= posicionSeleccionada < len(diaSeleccionadoLista):
                        diaSeleccionadoLista[posicionSeleccionada] = Funcion.allFunciones[funcionSeleccionada]
                        print(f"Función reemplazada correctamente en el cine {Cine.cines[cineSeleccionado1].getNombre()} en el día seleccionado.")
                    else:
                        print("Posición inválida.")

            elif opcion == 3:
                # Agregar una máquina a una zona de juegos
                if not Maquina.allMaquinas:
                    print("No hay máquinas disponibles.")
                    continue
                if not ZonaDeJuegos.zonasDeJuegos:
                    print("No hay zonas de juegos disponibles.")
                    continue

                # Mostrar lista de máquinas disponibles
                print("Selecciona la máquina a agregar:")
                for i, maquina in enumerate(Maquina.allMaquinas):
                    print(f"{i}. {maquina.getNombre()}")

                maquinaSeleccionada = int(input())

                # Mostrar lista de zonas de juegos disponibles
                print("Selecciona la zona de juegos a la que deseas agregar la máquina:")
                for i, zona in enumerate(ZonaDeJuegos.zonasDeJuegos):
                    print(f"{i}. {zona.getNombre()}")

                zonaSeleccionada = int(input())

                # Agregar la máquina seleccionada a la zona de juegos
                ZonaDeJuegos.zonasDeJuegos[zonaSeleccionada].getMaquinas().append(Maquina.allMaquinas[maquinaSeleccionada])
                print(f"Máquina agregada correctamente a la zona de juegos {ZonaDeJuegos.zonasDeJuegos[zonaSeleccionada].getNombre()}")

            elif opcion == 4:
                # Asignar una película a una función
                if not Pelicula.totalPeliculas:
                    print("No hay películas disponibles.")
                    continue
                if not Funcion.allFunciones:
                    print("No hay funciones disponibles.")
                    continue

                # Mostrar lista de películas disponibles
                print("Selecciona la película a asignar:")
                for i, pelicula in enumerate(Pelicula.totalPeliculas):
                    print(f"{i}. {pelicula.getTitulo()}")

                peliculaSeleccionada = int(input())

                # Mostrar lista de funciones disponibles
                print("Selecciona la función a la que deseas asignar la película:")
                for i, funcion in enumerate(Funcion.allFunciones):
                    if funcion.getPelicula():
                        print(f"{i}. {funcion.getPelicula().getTitulo()}  {funcion.getHoraInicio()}  {funcion.getTipo()}")
                    else:
                        print(f"{i}. Función sin película asignada  {funcion.getHoraInicio()}  {funcion.getTipo()}")

                funcionSeleccionada1 = int(input())

                # Asignar la película seleccionada a la función
                Funcion.allFunciones[funcionSeleccionada1].setPelicula(Pelicula.totalPeliculas[peliculaSeleccionada])
                print("Película asignada correctamente a la función.")

            elif opcion == 5:
                # Asignar una sala a una función
                if not Sala.allSalas:
                    print("No hay salas disponibles.")
                    continue
                if not Funcion.allFunciones:
                    print("No hay funciones disponibles.")
                    continue

                # Mostrar lista de salas disponibles
                print("Selecciona la sala a asignar:")
                for i, sala in enumerate(Sala.allSalas):
                    print(f"{i}. {sala.getNumero()}")

                salaSeleccionada = int(input())

                # Mostrar lista de funciones disponibles
                print("Selecciona la función a la que deseas asignar la sala:")
                for i, funcion in enumerate(Funcion.allFunciones):
                    if funcion.getSala():
                        print(f"{i}. {funcion.getSala().getNumero()}  {funcion.getHoraInicio()}  {funcion.getTipo()}")
                    else:
                        print(f"{i}. Función sin sala asignada  {funcion.getHoraInicio()}  {funcion.getTipo()}")

                funcionSeleccionada2 = int(input())

                # Asignar la sala seleccionada a la función
                Funcion.allFunciones[funcionSeleccionada2].setSala(Sala.allSalas[salaSeleccionada])
                print("Sala asignada correctamente a la función.")

            elif opcion == 6:
                # Salir del menú
                continuar = False
                print("Saliendo del menú de asignaciones.")

            else:
                print("Opción inválida. Inténtalo de nuevo.")
    
    
    @staticmethod
    def calificarPelicula():
        peliculas=[]
        for cine in Cine.cines:
            peliculas.extend(cine.peliculasActivas())
        if not peliculas:
            print("No hay películas activas en este momento.")
            return
        
        def objetosRepetidos(objetos):
            objetosUnicos = []
            for obj in objetos:
                if not any(obj.getTitulo() == unico.getTitulo() for unico in objetosUnicos):
                    objetosUnicos.append(obj)
            return objetosUnicos
        
        peliculas=objetosRepetidos(peliculas)
        
        # Mostrar lista de películas con índice
        for i, pelicula in enumerate(peliculas):
            print(f"{i + 1}. {pelicula.getTitulo()} - Calificación actual: {pelicula.getCalificacionPromedio():.2f}")
    
        # Solicitar selección de película
        seleccion = int(input("Seleccione el número de la película que desea calificar: "))
        if seleccion < 1 or seleccion > len(peliculas):
            print("Selección inválida.")
            return
    
        peliculaSeleccionada = peliculas[seleccion - 1]
    
        # Solicitar calificación
        calificacion = int(input(f"Ingrese una calificación para {peliculaSeleccionada.getTitulo()} (1-5): "))
        if calificacion < 1 or calificacion > 5:
            print("Calificación inválida.")
            return
    
        # Actualizar calificación
        peliculaSeleccionada.actualizarCalificacion(calificacion)
    
        # Confirmar y mostrar resultado
        print("Calificación guardada correctamente.")
        print(f"Nueva calificación promedio de {peliculaSeleccionada.getTitulo()}: {peliculaSeleccionada.getCalificacionPromedio():.2f}")

    def primeraOperacion():
        print("uwux2")

        

