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

    @staticmethod
    def error():
     print("Error")

# Gestiona la zona de juegos
    @staticmethod
    def gestionarZonaDeJuegos():
        # Simula la entrada del usuario
        entrada = input

        # Actualización de dinero recaudado en todas las zonas de juegos a través de los cines
        for cine in Cine.cines:
            if cine.zonaDeJuegos:  # Verificar si la zonaDeJuegos no es None
                cine.zonaDeJuegos.actualizarDineroRecaudado()

        # Mostrar informe de máquinas dañadas en cada zona de juegos a través de los cines
        print("Informe de máquinas dañadas:")
        for cine in Cine.cines:
            if cine.zonaDeJuegos:  # Verificar si la zonaDeJuegos no es None
                print(cine.zonaDeJuegos.informeMaquinas())

        # Selección de zona de juegos y máquina para reparar
        print("Seleccione el número de la zona de la máquina que desea reparar: ")
        zonasDisponibles = [cine for cine in Cine.cines if cine.zonaDeJuegos]
        for i, cine in enumerate(zonasDisponibles):
            print(f"{i + 1}. {cine.zonaDeJuegos.getNombre()}")
        zonaSeleccionada = int(entrada()) - 1

        # Obtener la zona de juegos seleccionada a través del cine correspondiente
        zonaActual = zonasDisponibles[zonaSeleccionada].zonaDeJuegos
        maquinasDañadas = zonaActual.getMaquinasDañadas()
        if not maquinasDañadas:
            print("No hay máquinas dañadas en la zona seleccionada.")
            return

        # Seleccionar la máquina a reparar dentro de la zona seleccionada
        print("Seleccione el número de la máquina que desea reparar:")
        for i, maquina in enumerate(maquinasDañadas):
            print(f"{i + 1}. {maquina.getNombre()}")
        seleccionMaquina = int(entrada()) - 1

        # Realizar la reparación usando el método de la bodega
        print(Bodega.allBodegas[0].realizarMantenimiento(zonaActual, seleccionMaquina))

        # Recomendación de movimiento para la máquina reparada
        maquinaReparada = maquinasDañadas[seleccionMaquina]
        print(zonaActual.recomendarMovimiento(maquinaReparada))

        # Selección de la zona de destino para mover la máquina reparada
        print("Seleccione la zona a la que desea mover la máquina:")
        for i, cine in enumerate(zonasDisponibles):
            print(f"{i + 1}. {cine.zonaDeJuegos.getNombre()}")
        seleccionZona = int(entrada()) - 1

        # Obtener la zona de juegos de destino a través del cine correspondiente
        zonaDestino = zonasDisponibles[seleccionZona].zonaDeJuegos
        if zonaActual != zonaDestino:
            print(zonaActual.moverMaquina(zonaDestino, seleccionMaquina))
        else:
            print(f"La máquina permanecerá en {zonaActual.getNombre()}")

        # Aplicar incentivos a las zonas de juegos si el usuario lo desea
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
                # Obtener las dos máquinas que menos venden para recomendar un cambio de precio
                dosMenosVenden = Maquina.obtenerDosMaquinasMenosVenden()

                if not dosMenosVenden:
                    print("No hay máquinas disponibles para recomendar.")
                else:
                    print("Recomendación de cambio de precio:")
                    for maquina in dosMenosVenden:
                        print(maquina)

                # Seleccionar la zona donde aplicar la rebaja
                print("Seleccione la zona donde aplicar la rebaja:")
                for i, cine in enumerate(zonasDisponibles):
                    print(f"{i + 1}. {cine.zonaDeJuegos.getNombre()}")
                seleccionZonaRebaja = int(entrada()) - 1

                zonaRebaja = zonasDisponibles[seleccionZonaRebaja].zonaDeJuegos

                # Seleccionar la máquina específica en la zona para rebajar su precio
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
                # Seleccionar la zona de juegos para aplicar el bono
                print("Seleccione la zona de juegos:")
                for i, cine in enumerate(zonasDisponibles):
                    print(f"{i + 1}. {cine.zonaDeJuegos.getNombre()}")
                zonaSeleccionada1 = int(entrada()) - 1

                zona = zonasDisponibles[zonaSeleccionada1].zonaDeJuegos

                # Seleccionar la máquina específica en la zona para aplicar el bono
                print("Seleccione la máquina a la que desea aplicar el bono:")
                for i, maquina in enumerate(zona.getMaquinas()):
                    print(f"{i + 1}. {maquina.getNombre()}")
                maquinaSeleccionada = int(entrada()) - 1

                maquina = zona.getMaquinas()[maquinaSeleccionada]
                maquina.activarBono()

                print(f"El bono ha sido activado para la máquina {maquina.getNombre()}")

        else:
            print("No se aplicarán incentivos.")

        # Actualización final de dinero recaudado en todas las zonas de juegos a través de los cines
        for cine in Cine.cines:
            if cine.zonaDeJuegos:  # Verificar si la zonaDeJuegos no es None
                cine.zonaDeJuegos.actualizarDineroRecaudado()
                print(f"Dinero recaudado por {cine.zonaDeJuegos.getNombre()}: {cine.zonaDeJuegos.getDineroRecaudado()}")


    
    

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
        print("0.Salir")
        nuevoCineSeleccionado = int(input()) - 1
        if nuevoCineSeleccionado==-1:
            return
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
    def gestionarCartelera():
        print("Elige el cine al que deseas modificar su cartelera semanal:\n")
        listaVacios = None
        cine = None
        while True:
            for i in range(len(Cine.cines)):
                print(f"{i+1} {Cine.cines[i].getNombre()}.")
            eleccion = int(input("->:"))
            cine = Cine.cines[eleccion-1]
            listaVacios = cine.hallarEspaciosSinFuncion()
            if(listaVacios == -1):
                print("Este cine no tiene huecos para agregar funciones, selecciona otro")
                continue
            else:
                break
        print("Esta es la programación semanal que actualmente se tiene en el cine escogido:")
        #Falta

        peliculasListas = []
        while True:
            print("Estos son los espacios libres en el cine escogido::")
            horaPeli = None
            espacio = None
            diaPeli = None                
            for j in range(len(listaVacios)):
                horaDelDia = "am"
                if listaVacios[j][2] >= time(12,0):
                    horaDelDia = "pm"

                print(f"{j+1}. Día {listaVacios[j][1]}, a las {listaVacios[j][2].strftime('%H:%M') + horaDelDia}")
            if len(listaVacios) == 1:
                espacio = listaVacios[0]
                print("Como solo hay una alternativa, la tomamos de inmediato")
            else:
                print("Elige el espacio que deseas modificar:")
                eleccion = int(input("->:"))
                espacio = listaVacios[eleccion]
            peliculasParaElegir = Pelicula.ObtenerPeliculasElegibles(espacio[2], espacio[1], cine)
            if len(peliculasParaElegir)==1:
                horaPeli = listaVacios[0][2]
                diaPeli = listaVacios[0][1]
                print(f"Como solo hay una alternativa, lo tomamos de inmediato: {peliculasParaElegir[0].getTitulo()}")
                peliculasListas += [[peliculasParaElegir[0],diaPeli, horaPeli] ]
                break
            else:
                print("Elige la película para rellenar el espacio:\n")
                for i in range(len(peliculasParaElegir)):
                    print(f"{str(i+1)}. {peliculasParaElegir[i].getTitulo()}, calificación: {str(peliculasParaElegir[i].getCalificacionPromedio())}")
                eleccion = int(input("->:"))
                diaPeli = espacio[1]
                horaPeli = espacio[2]
                peliculasListas += [[peliculasParaElegir[eleccion-1], diaPeli, horaPeli]]
                listaVacios.remove(espacio)
            if len(listaVacios) == 0:
                break
            else:
                print("¿Quiéres continuar llenando espacios? (S/N)")
                decision = input("->:")
                if (decision == "S"):
                    continue
                elif (decision == "N"):
                    print("Saliendo")
                    break
    
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
        calificacion = float(input(f"Ingrese una calificación para {peliculaSeleccionada.getTitulo()} (1-5): "))
        if calificacion < 1 or calificacion > 5:
            print("Calificación inválida.")
            return
    
        # Actualizar calificación
        peliculaSeleccionada.actualizarCalificacion(calificacion)
    
        # Confirmar y mostrar resultado
        print("Calificación guardada correctamente.")
        print(f"Nueva calificación promedio de {peliculaSeleccionada.getTitulo()}: {peliculaSeleccionada.getCalificacionPromedio():.2f}")

    @staticmethod
    def serializarTodo():
        Cine.serializarCines('src/baseDatos/temp/cine.pkl')
        Cliente.serializarClientes('src/baseDatos/temp/cliente.pkl')
        Funcion.serializarFunciones('src/baseDatos/temp/funcion.pkl')
        Pelicula.serializarPeliculas('src/baseDatos/temp/pelicula.pkl')
        Sala.serializarSalas('src/baseDatos/temp/sala.pkl')
        ZonaDeJuegos.serializarZonasDeJuegos('src/baseDatos/temp/zonaDeJuegos.pkl')
        Bodega.serializarBodegas('src/baseDatos/temp/bodega.pkl')
        Maquina.serializarMaquinas('src/baseDatos/temp/maquina.pkl')
    
    @staticmethod
    def deserializarTodo():
        Cine.deserializarCines('src/baseDatos/temp/cine.pkl')
        Cliente.deserializarClientes('src/baseDatos/temp/cliente.pkl')
        Funcion.deserializarFunciones('src/baseDatos/temp/funcion.pkl')
        Pelicula.deserializarPeliculas('src/baseDatos/temp/pelicula.pkl')
        Sala.deserializarSalas('src/baseDatos/temp/sala.pkl')
        ZonaDeJuegos.deserializarZonasDeJuegos('src/baseDatos/temp/zonaDeJuegos.pkl')
        Bodega.deserializarBodegas('src/baseDatos/temp/bodega.pkl')
        Maquina.deserializarMaquinas('src/baseDatos/temp/maquina.pkl')
        

    def primeraOperacion():
        print('ufu')


        

