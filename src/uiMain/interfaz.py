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
        cls.funcion1 = Funcion(cls.pelicula1, "Normal", cls.sala1, 45000)
        cls.funcion2 = Funcion(cls.pelicula2, "Normal", cls.sala2, 25000)
        cls.funcion3 = Funcion(cls.pelicula3, "Normal", cls.sala3, 30000)
        cls.funcion4 = Funcion(cls.pelicula4, "Normal", cls.sala4, 40000)
        cls.funcion5 = Funcion(cls.pelicula5, "Normal", cls.sala5, 50000)
        cls.funcion6 = Funcion(cls.pelicula6, "Normal", cls.sala6, 12000)
        cls.funcion7 = Funcion(cls.pelicula7, "Normal", cls.sala7, 22000)
        cls.funcion8 = Funcion(cls.pelicula8, "Normal", cls.sala8, 280)
        cls.funcion9 = Funcion(cls.pelicula9, "Normal", cls.sala9, 350)
        cls.funcion10 = Funcion(cls.pelicula1, "Normal", cls.sala10, 190)
        cls.funcion11 = Funcion(cls.pelicula3, "Normal", cls.sala11, 270)
        cls.funcion12 = Funcion(cls.pelicula7, "Normal", cls.sala12, 230)
        cls.funcion13 = Funcion(cls.pelicula4, "Normal", cls.sala13, 410)
        cls.funcion14 = Funcion(cls.pelicula2, "Normal", cls.sala14, 260)
        cls.funcion15 = Funcion(cls.pelicula5, "Normal", cls.sala15, 500)
        cls.funcion16 = Funcion(cls.pelicula8, "Normal", cls.sala16, 300)
        cls.funcion17 = Funcion(cls.pelicula9, "Normal", cls.sala17, 340)
        cls.funcion18 = Funcion(cls.pelicula6, "Normal", cls.sala18, 130)
        cls.funcion19 = Funcion(cls.pelicula7, "Normal", cls.sala19, 200)
        cls.funcion20 = Funcion(cls.pelicula9, "Normal", cls.sala20, 330)
        cls.funcion21 = Funcion(cls.pelicula6, "Normal", cls.sala21, 140)
        cls.funcion22 = Funcion(cls.pelicula7, "Normal", cls.sala22, 210)
        cls.funcion23 = Funcion(cls.pelicula3, "Normal", cls.sala23, 300)
        cls.funcion24 = Funcion(cls.pelicula4, "Normal", cls.sala24, 420)
        cls.funcion25 = Funcion(cls.pelicula5, "Normal", cls.sala25, 480)

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
        cls.cine1.agregarFuncion(cls.funcion2, cls.cine1.getLunes())  # Acción: "Spiderman" (8 am)

        cls.cine1.agregarFuncion(cls.funcion4, cls.cine1.getMartes())  # +18: "Deadpool" (8 am)
        cls.cine1.agregarFuncion(cls.funcion5, cls.cine1.getMartes())  # Drama: "Oppenheimer" (10 am)

        cls.cine1.agregarFuncion(cls.funcion3, cls.cine1.getJueves())  # Terror: "Jason Vorhees" (8 am)
        cls.cine1.agregarFuncion(cls.funcion8, cls.cine1.getJueves())  # Terror: "El Conjuro" (10 am)

        cls.cine1.agregarFuncion(cls.funcion9, cls.cine1.getViernes())  # Acción: "Inception" (8 am)
        cls.cine1.agregarFuncion(cls.funcion5, cls.cine1.getViernes())  # Drama: "Oppenheimer" (12 pm)
        cls.cine1.agregarFuncion(cls.funcion4, cls.cine1.getViernes())  # +18: "Deadpool" (4 pm)

        cls.cine1.agregarFuncion(cls.funcion9, cls.cine1.getSabado())  # Acción: "Inception" (8 am)
        cls.cine1.agregarFuncion(cls.funcion3, cls.cine1.getSabado())  # Terror: "Jason Vorhees" (11 am)

        # Asignación de máquinas a zonas de juegos
        cls.zona1.agregarMaquina(cls.arcade1)
        cls.zona1.agregarMaquina(cls.danceDance1)
        cls.zona1.agregarMaquina(cls.mesaDeDiscos1)
        cls.zona2.agregarMaquina(cls.arcade2)
        cls.zona2.agregarMaquina(cls.boxing1)
        cls.zona2.agregarMaquina(cls.mesaDeDiscos2)
        cls.zona3.agregarMaquina(cls.basket1)


    @staticmethod
    def error():
     print("Error")

# Gestiona la zona de juegos
    @staticmethod
    def gestionar_zona_de_juegos():
    # Simula la entrada del usuario
        entrada = input

    # Actualización de dinero recaudado en todas las zonas
        for zona in ZonaDeJuegos.zonas_de_juegos:
            zona.actualizar_dinero_recaudado()

    # Mostrar informe de máquinas dañadas en cada zona
        print("Informe de máquinas dañadas:")
        for zona in ZonaDeJuegos.zonas_de_juegos:
            print(zona.informe_maquinas())

    # Selección de zona y máquina para reparar
        print("Seleccione el número de la zona de la máquina que desea reparar: ")
        for i, zona in enumerate(ZonaDeJuegos.zonas_de_juegos):
            print(f"{i + 1}. {zona.get_nombre()}")
        zona_seleccionada = int(entrada()) - 1

        zona_actual = ZonaDeJuegos.zonas_de_juegos[zona_seleccionada]
        maquinas_dañadas = zona_actual.get_maquinas_dañadas()
        if not maquinas_dañadas:
            print("No hay máquinas dañadas en la zona seleccionada.")
            return

        print("Seleccione el número de la máquina que desea reparar:")
        for i, maquina in enumerate(maquinas_dañadas):
            print(f"{i + 1}. {maquina.get_nombre()}")
        seleccion_maquina = int(entrada()) - 1

    # Realizar reparación
        print(Interfaz.bodega.realizar_mantenimiento(zona_actual, seleccion_maquina))

    # Recomendación de movimiento
        maquina_reparada = maquinas_dañadas[seleccion_maquina]
        print(zona_actual.recomendar_movimiento(maquina_reparada))

    # Selección de zona de destino para mover la máquina reparada
        print("Seleccione la zona a la que desea mover la máquina:")
        for i, zona in enumerate(ZonaDeJuegos.zonas_de_juegos):
            print(f"{i + 1}. {zona.get_nombre()}")
        seleccion_zona = int(entrada()) - 1

        zona_destino = ZonaDeJuegos.zonas_de_juegos[seleccion_zona]
        if zona_actual != zona_destino:
            print(zona_actual.mover_maquina(zona_destino, seleccion_maquina))
        else:
            print(f"La máquina permanecerá en {zona_actual.get_nombre()}")

    # Aplicar incentivos
        print("¿Desea aplicar algún incentivo en una zona de juegos?")
        print("1. Sí")
        print("2. No")
        opcion_incentivo = int(entrada())

        if opcion_incentivo == 1:
            print("Seleccione el tipo de incentivo:")
            print("1. Rebajar el precio de una máquina")
            print("2. Regalar un bono por el uso de una máquina")
            tipo_incentivo = int(entrada())

        if tipo_incentivo == 1:
            dos_menos_venden = Maquina.obtener_dos_maquinas_menos_venden()

            if not dos_menos_venden:
                print("No hay máquinas disponibles para recomendar.")
            else:
                print("Recomendación de cambio de precio:")
                for maquina in dos_menos_venden:
                    print(maquina)

            print("Seleccione la zona donde aplicar la rebaja:")
            for i, zona in enumerate(ZonaDeJuegos.zonas_de_juegos):
                print(f"{i + 1}. {zona.get_nombre()}")
            seleccion_zona_rebaja = int(entrada()) - 1

            zona_rebaja = ZonaDeJuegos.zonas_de_juegos[seleccion_zona_rebaja]

            print("Seleccione la máquina para rebajar su precio:")
            maquinas_en_zona = zona_rebaja.get_maquinas()
            for i, maquina in enumerate(maquinas_en_zona):
                print(f"{i + 1}. {maquina.get_nombre()}")
            seleccion_maquina_rebaja = int(entrada()) - 1

            maquina_rebajada = maquinas_en_zona[seleccion_maquina_rebaja]
            nuevo_precio = float(input(f"Introduzca el nuevo precio para la máquina {maquina_rebajada.get_nombre()}: "))
            maquina_rebajada.set_precio_uso(nuevo_precio)

            print(f"El precio de la máquina {maquina_rebajada.get_nombre()} ha sido rebajado a {nuevo_precio}")

        elif tipo_incentivo == 2:
            print("Seleccione la zona de juegos:")
            for i, zona in enumerate(ZonaDeJuegos.zonas_de_juegos):
                print(f"{i + 1}. {zona.get_nombre()}")
            zona_seleccionada1 = int(entrada()) - 1

            zona = ZonaDeJuegos.zonas_de_juegos[zona_seleccionada1]

            print("Seleccione la máquina a la que desea aplicar el bono:")
            for i, maquina in enumerate(zona.get_maquinas()):
                print(f"{i + 1}. {maquina.get_nombre()}")
            maquina_seleccionada = int(entrada()) - 1

            maquina = zona.get_maquinas()[maquina_seleccionada]
            maquina.activar_bono()

            print(f"El bono ha sido activado para la máquina {maquina.get_nombre()}")

        else:
            print("No se aplicarán incentivos.")

    # Actualización final de dinero recaudado
        for zona in ZonaDeJuegos.zonas_de_juegos:
            zona.actualizar_dinero_recaudado()
            print(f"Dinero recaudado por {zona.get_nombre()}: {zona.get_dinero_recaudado()}")
    

    @staticmethod
    def gestionar_peliculas():
        # Paso 1: Ver las calificaciones
        print("Calificaciones de las películas en los cines:")
        for cine in Cine.cines:
            print("Cine:", cine.get_nombre())
            calificaciones = cine.obtener_calificaciones_peliculas()
            for calificacion in calificaciones:
                print(calificacion)

        # Paso 2: Selección de cine y película por parte del usuario
        print("Seleccione el cine de la película que desea intercambiar:")
        for i, cine in enumerate(Cine.cines):
            print(f"{i + 1}. {cine.get_nombre()}")
        cine_seleccionado = int(input()) - 1
        cine_origen = Cine.cines[cine_seleccionado]

        # Mostrar películas en el cine seleccionado
        print("Seleccione la película que desea intercambiar:")
        peliculas = cine_origen.peliculas_activas()
        for i, pelicula in enumerate(peliculas):
            print(f"{i + 1}. {pelicula.get_titulo()}")
        pelicula_seleccionada = int(input()) - 1
        pelicula_a_intercambiar = peliculas[pelicula_seleccionada]

        # Paso 3: Recomendar una película para intercambio basada en la selección
        print(Pelicula.recomendar_intercambio(pelicula_a_intercambiar))

        # Paso 4: Selección del nuevo cine para el intercambio
        print("Seleccione el nuevo cine (omitido el cine actual):")
        for i, cine in enumerate(Cine.cines):
            if i != cine_seleccionado:
                print(f"{i + 1}. {cine.get_nombre()}")
        nuevo_cine_seleccionado = int(input()) - 1
        if nuevo_cine_seleccionado >= cine_seleccionado:
            nuevo_cine_seleccionado += 1  # Ajustar el índice si el cine seleccionado es mayor
        nuevo_cine = Cine.cines[nuevo_cine_seleccionado]

        # Mostrar películas en el nuevo cine seleccionado
        print("Seleccione la película con la que desea intercambiar:")
        peliculas_nuevo_cine = nuevo_cine.peliculas_activas()
        for i, pelicula in enumerate(peliculas_nuevo_cine):
            print(f"{i + 1}. {pelicula.get_titulo()}")
        pelicula_intercambio_seleccionada = int(input()) - 1

        # Manejar la opción de no intercambiar
        if pelicula_intercambio_seleccionada == -1:
            print("No se realizará el intercambio.")
            return

        pelicula_intercambio = peliculas_nuevo_cine[pelicula_intercambio_seleccionada]

        # Confirmar el intercambio
        print(f"¿Desea realizar el intercambio entre {pelicula_a_intercambiar.get_titulo()} y {pelicula_intercambio.get_titulo()}? (1. Sí / 2. No)")
        realizar_intercambio = int(input())

        if realizar_intercambio == 1 and pelicula_a_intercambiar and pelicula_intercambio and pelicula_a_intercambiar != pelicula_intercambio:
            resultado_intercambio = Funcion.realizar_intercambio(pelicula_a_intercambiar, pelicula_intercambio)
            print(resultado_intercambio)
        else:
            print("No se realizó el intercambio.")

        # Paso 5: Aplicar bonos o descuentos
        print("¿Desea aplicar algún incentivo para la nueva película?")
        print("1. Rebajar el precio de la entrada")
        print("2. Regalar un bono")
        print("3. No aplicar incentivos")
        tipo_incentivo = int(input())

        if tipo_incentivo == 1:
            # Aplicar rebaja en el precio de la entrada
            print("Seleccione la función para la película a la que desea aplicar el nuevo precio:")
            funciones = pelicula_intercambio.get_funciones()
            for i, funcion in enumerate(funciones):
                print(f"{i + 1}. {funcion}")  # Asumiendo que la función tiene un método __str__ para mostrar información relevante
            funcion_seleccionada = int(input()) - 1

            if 0 <= funcion_seleccionada < len(funciones):
                funcion = funciones[funcion_seleccionada]
                nuevo_precio = float(input("Introduzca el nuevo precio para la entrada: "))
                funcion.set_precio(nuevo_precio)
                print(f"El precio de entrada ha sido rebajado a {nuevo_precio}")
            else:
                print("Selección de función inválida.")

        elif tipo_incentivo == 2:
            # Aplicar bono
            print("Seleccione el cine para aplicar el bono:")
            for i, cine in enumerate(Cine.cines):
                print(f"{i + 1}. {cine.get_nombre()}")
            cine_seleccionado = int(input()) - 1
            cine = Cine.cines[cine_seleccionado]

            # Seleccionar la película en la que se desea aplicar el bono
            print("Seleccione la película a la que desea aplicar el bono:")
            peliculas = cine.peliculas_activas()
            for i, pelicula in enumerate(peliculas):
                print(f"{i + 1}. {pelicula.get_titulo()}")
            pelicula_seleccionada = int(input()) - 1
            pelicula = peliculas[pelicula_seleccionada]

            # Activar el bono en la película seleccionada
            pelicula.activar_bono()
            print(f"El bono ha sido activado para la película {pelicula.get_titulo()}")

        elif tipo_incentivo == 3:
            print("No se aplicarán incentivos.")
        else:
            print("Opción no válida.")
    @staticmethod
    def comprar_boleta_juegos():
    # Paso 1: Identificación del cliente
        id_cliente = int(input("Ingrese su número de identificación: "))
        cliente = Cliente.buscar_cliente_por_id(id_cliente)

        if cliente is None:
            respuesta = int(input("Cliente no encontrado. ¿Desea crear uno nuevo? (1)Sí/(2)No: "))
        if respuesta == 1:
            nombre = input("Ingresa tu nombre: ")  # Captura el nombre completo
            saldo_inicial = float(input("Ingresa tu saldo inicial: "))  # Captura el saldo inicial
            cliente = Cliente(nombre, saldo_inicial, id_cliente)  # Crea el nuevo cliente
            print("Cliente creado exitosamente.")
        elif respuesta == 2:
            return
        else:
            print("Selección inválida. Por favor, seleccione un número válido.")
            return  # Sale del método si la selección es inválida

        # Paso 2: Selección del cine
        print("Seleccione el cine:")
        for i, cine in enumerate(Cine.cines):
         print(f"{i + 1}. {cine.get_nombre()}")  # Lista los cines disponibles
        cine_seleccionado_index = int(input()) - 1
        cine_seleccionado = Cine.cines[cine_seleccionado_index]

    # Paso 3: Selección de la máquina en la zona de juegos
        zona_de_juegos_seleccionada = cine_seleccionado.get_zona_de_juegos()  # Obtener la zona de juegos del cine
        maquinas_disponibles = zona_de_juegos_seleccionada.get_maquinas()

        print("Seleccione la máquina para comprar la boleta:")
        for i, maquina in enumerate(maquinas_disponibles):
            print(f"{i + 1}. {maquina.get_nombre()} - Precio: {maquina.get_precio_uso()}")  # Lista las máquinas disponibles
        maquina_seleccionada_index = int(input()) - 1
        maquina_seleccionada = maquinas_disponibles[maquina_seleccionada_index]

    # Verificar si la máquina requiere mantenimiento
        if maquina_seleccionada.necesita_mantenimiento():
            print(f"La máquina {maquina_seleccionada.get_nombre()} no está disponible debido a que requiere mantenimiento.")
            return

    # Paso 4: Realizar la compra
        if cliente.get_saldo() >= maquina_seleccionada.get_precio_uso():
            cliente.set_saldo(cliente.get_saldo() - maquina_seleccionada.get_precio_uso())  # Descuenta el precio de la máquina del saldo del cliente
            maquina_seleccionada.usar()  # Registra el uso de la máquina
            print("Compra realizada exitosamente.")

        # Paso 5: Asignar bono si está activo
            print(maquina_seleccionada.asignar_bono(cliente))  # Asigna un bono si es aplicable

        # Paso 6: Imprimir recibo
            print("Recibo:")
            print(f"Cliente: {cliente.get_identificacion()}")
            print(f"Tipo de cliente: {cliente.get_tipo()}")
            print(f"Máquina: {maquina_seleccionada.get_nombre()}")
            print(f"Precio pagado: {maquina_seleccionada.get_precio_uso()}")
            print(f"Saldo restante: {cliente.get_saldo()}")
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
                nombre_zona = input("Ingresa el nombre de la Zona de Juegos: ")
                horario = input("Ingresa el horario de la Zona de Juegos: ")
                zona = ZonaDeJuegos(nombre_zona, horario)
                print(f"Zona de Juegos creada: {zona}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 2:
                nombre_bodega = input("Ingresa el nombre de la Bodega: ")
                materiales = int(input("Ingrese la cantidad inicial de materiales: "))
                bodega = Bodega(nombre_bodega, materiales)
                print(f"Bodega creada: {bodega}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 3:
                nombre_maquina = input("Ingresa el nombre de la Máquina: ")
                print("Ingresa el tipo de la Máquina")
                print("1. Arcade")
                print("2. Dance Dance")
                print("3. Mesa de discos")
                print("4. Boxing")
                print("5. Basket")
                tipo_maquina = int(input("Selecciona una opción: "))
                tipo = Interfaz.obtener_tipo_maquina(tipo_maquina)

                materiales_necesarios = int(input("Ingresa la cantidad de materiales necesarios para la Máquina: "))
                precio_maquina = float(input("Ingresa el precio de la Máquina: "))
                maquina = Maquina(nombre_maquina, tipo, materiales_necesarios, precio_maquina)
                print(f"Máquina creada: {maquina}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 4:
                nombre_cliente = input("Ingresa el nombre del Cliente: ")
                saldo = float(input("Ingresa el saldo inicial del Cliente: "))
                id_cliente = int(input("Ingresa el número de identificación del Cliente: "))
                cliente = Cliente(nombre_cliente, saldo, id_cliente)
                print(f"Cliente creado: {cliente}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 5:
                nombre_cine = input("Ingresa el nombre del Cine: ")
                cine = Cine(nombre_cine)
                print(f"Cine creado: {cine}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 6:
                titulo_pelicula = input("Ingresa el título de la Película: ")
                print("Ingresa el género de la Película")
                print("1. Acción")
                print("2. Infantil")
                print("3. Terror")
                print("4. +18")
                print("5. Drama")
                genero_pelicula = int(input("Selecciona una opción: "))
                genero = Interfaz.obtener_genero_pelicula(genero_pelicula)

                duracion_input = input("Ingresa la duración de la Película (en horas y minutos, formato HH:MM): ")
                try:
                    duracion = datetime.datetime.strptime(duracion_input, "%H:%M").time()
                except ValueError:
                    print("Formato de tiempo inválido. Usa el formato HH:MM.")
                    continue  # Volver al menú si la duración es inválida

                pelicula = Pelicula(titulo_pelicula, genero, duracion)
                print(f"Película creada exitosamente: {pelicula.titulo}, Género: {pelicula.genero}, Duración: {pelicula.duracion}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 7:
                numero_sala = int(input("Ingresa el número de la Sala: "))
                filas = int(input("Ingresa el número de filas de la Sala: "))
                columnas = int(input("Ingresa el número de columnas de la Sala: "))
                sala = Sala(numero_sala, filas, columnas)
                print(f"Sala creada: {sala}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 8:
                print("Ingresa el tipo de Función:")
                print("1. Normal")
                print("2. VIP")
                eleccion_tipo = int(input("Selecciona una opción: "))
                tipo_funcion = Interfaz.obtener_tipo_funcion(eleccion_tipo)
                funcion = Funcion(tipo_funcion)
                print(f"Función creada: {funcion}")
                continuar = Interfaz.verificar_continuar()

            elif opcion == 9:
                continuar = False
                print("Saliendo del menú de creación.")

            else:
                print("Opción inválida. Inténtalo de nuevo.")
    
    @staticmethod
    def verificar_continuar():
        respuesta = int(input("¿Desea hacer otra creación? 1. Sí | 2. No: "))
        if respuesta == 2:
            return False
        elif respuesta == 1:
            return True
        else:
            print("Selección inválida.")
            return False
    def asignacion():
        print("uwu")
    def primeraOperacion():
        print("uwux2")

        

