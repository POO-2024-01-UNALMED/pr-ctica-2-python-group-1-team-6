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
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




from datetime import time,datetime

class Interfaz:

    @staticmethod
    def error():
     print("Error")
    
    @staticmethod
    def comprarBoleta():
        cines = Cine.cines #Todos los cines creados.
        cliente = None
        print("Has elegido la opción de comprar boleta, por favor ingresa tu número de identificación:")

        #Le pedimos al usuario que ingrese su número de identificación para localizarlo en el sistema..
        #Si no aparece, le pedimos que ingrese sus datos y le ofrecemos una tarjeta de membresía.
        while (True):
            numeroIdentificacion = int(input())
            cliente = Cliente.buscarClientePorId(numeroIdentificacion)
            if cliente is None:
                print("Cliente no encontrado. ¿Desea crear uno nuevo?(ingrese número)\n1. Sí\n2. No")
                respuesta = int(input())
                if respuesta == 1:
                    print("Ingresa tu nombre: ")
                    nombre = input()
                    print("Ingresa tu saldo inicial: ")
                    saldoInicial = float(input())
                    cliente = Cliente(nombre, saldoInicial, numeroIdentificacion)
                    print("Cliente creado exitosamente.")
                    break
                elif respuesta == 2:
                    print("Saliendo... Necesitas un usuario para continuar.")
                    return
                else:
                    print("Selección invalida, elige 1 ó 2.")
                    return
                print("¿Deseas adquirir una tarjeta de membresía para usar en nuestros cines?(ingrese número)\n1. Sí\n2. No")
                while (True):
                    respuesta = int(input())
                    if respuesta == 2:
                        break
                    elif respuesta == 1:
                        printn("Tenemos los siguientes planes de tarjeta: \n1. Plan Platino. Obtienes 200 puntos por cada compra realizada. El costo de tramitarla es de 25.000$\n2. Plan Oro. Obtienes 150 puntos por cada compra realizada. El costo de tramitarla es de 17.000$\n3. Plan Bronce. Obtienes 100 puntos por cada compra realizada. El costo de tramitarla es de 10.000$")
                        print("Elige la opción de tarjeta de tu preferencia, o ingresa 4 para salir")
                        print("Este es tu saldo: " + cliente.getSaldo())
                        while (True):
                            eleccionTarjeta = int(input())
                            if tarjeta == 1:
                                operacion = cliente.adquirirTarjeta(25000)
                                if (operacion):
                                    print("Ahora cuentas con una tarjeta Platino.")
                                    break
                                else:
                                    print("No tienes suficiente dinero para el plan Platino.")
                                    if (cliente.getSaldo() < 17000 and cliente.getSaldo() < 10000):
                                        print("Tampoco tienes suficiente dinero para el Oro y Bronce.")
                                        break
                                    else:
                                        print("¿Te interesa otro plan distinto a Platino?(ingrese número)\n1. Sí\n2. No")
                                        otroPlan = int(input())
                                        if otroPlan == 2:
                                            break;
                                        elif otroPlan == 1:
                                            mayorOro = cliente.getSaldo() >= 17000
                                            if (mayorOro):
                                                print("Elige:\n1.Plan Oro\n2.Plan Bronce")
                                                planSegundo = int(input())
                                                if (planSegundo == 1):
                                                    cliente.adquirirTarjeta(17000)
                                                    print("Ahora cuentas con una tarjeta Oro.")
                                                    break
                                                elif (planSegundo == 2):
                                                    cliente.adquirirTarjeta(10000)
                                                    print("Ahora cuentas con una tarjeta Bronce")
                                                    break
                                            else:
                                                cliente.adquirirTarjeta(10000)
                                                print("Ahora cuentas con una tarjeta Bronce")
                                                break
                            elif tarjeta == 2:
                                operacion = cliente.adquirirTarjeta(17000)
                                if (operacion):
                                    print("Ahora cuentas con una tarjeta Oro.")
                                    break
                                else:
                                    print("No tienes suficiente dinero para plan Oro.")
                                    if (cliente.getSaldo() >= 10000):
                                        print("¿Te interesa el plan Bronce?(ingrese número)\n1. Sí\n2. No")
                                        otroPlan = int(input())
                                        if (otroPlan) == 1:
                                            cliente.adquiriTarjeta(10000)
                                            print("Ahora cuentas con una tarjeta Bronce.")
                                            break
                                        else:
                                            break
                                    else:
                                        print("Como no tienes suficiente dinero para el plan Bronce, se da por finalizada la adquisición de la tarjeta")
                                        break
                            elif tarjeta == 3:
                                operacion = cliente.adquirirTarjeta(10000)
                                if (operacion):
                                    print("Ahora cuentas con una tarjeta Bronce.")
                                    break 
                                else:
                                    print("No tienes suficiente dinero para el plan Bronce")
                                    break
                            elif tarjeta == 4:
                                break
                            else:
                                continue
                    else:
                        print("Elección no válida, intentalo nuevamente.")
                if (cliente.getTarjeta()):
                    print("¿Desea recargar la tarjeta?(Ingrese número)\n1. Sí\n2. No")
                    recarga = int(input())
                    if (recarga == 1 and cliente.getSaldo()>0):
                        print("Indique la cantidad a recargar:")
                        while (True):
                            cantidad = int(input())
                            if (cliente.recargarTarjeta(cantidad)):
                                print(cantidad + "$ añadidos a tu cuenta")
                                break
                            else:
                                print("No tienes tal cantidad. Intenta con otra. Este es tu saldo actual " + str(cliente.getSaldo()))
                                continue
                    elif (recarga == 2):
                        break
                    else:
                        print("No tienes dinero para añadir a tu tarjeta")
                break
            else:
                print("Cliente encontrado.")
                break
        
        print("A continuación se listan todos los cines posibles, elige el que prefieres: ")
        
        #Para mostrar en pantalla cada uno de los cines
        for i in range(len(cines)):
            cines[i],ajustarFunciones()
            print(f"{i+1}, {cines[i].getNombre()}")
        
        cineEscogido = None
        condicion = True
        while(condicion):
            eleccion = int(input())
            if eleccion > len(cines) or eleccion <= 0:
                print("Entrada no válida.")
                continue
            cineEscogido = cines[eleccion-1]
            condicion = False
        condicion = True
    
        print("Elegiste " + cineEscogido.getNombre())
        print("Estas son las películas que actualmente maneja nuestro cine:")

        for i in range(len(Cine.peliculas)):
            print(f"{i+1}. {Cine.peliculas[i].getTitulo()}")
        
        peliculaElegida = None
        print("Ingresa el número de la película que deseas ver, para confirmar si hay funciones activas:")

        while(condicion):
            pelicula = int(input())
            if (pelicula > len(Cine.peliculas)) or pelicula <= 0:
                print("Entrada no válida.")
                continue
            peliculaElegida = Cine.peliculas[pelicula-1]
            condicion = False
        condicion = True

        primeraIteracion = True

        while condicion:  # El método verifica que la película tenga por lo menos una función en el cine que el usuario eligió.
            existenciaFuncion = cliente.comprarBoleta(cineEscogido, peliculaElegida)
            
            if not existenciaFuncion:
                if primeraIteracion:
                    print(f"En este momento no hay funciones disponibles para {peliculaElegida.getTitulo()} en {cineEscogido.getNombre()}")
                    primeraIteracion = False
                
                print("¿Qué quieres cambiar para hacer de nuevo la búsqueda?: \n 1. El cine\n 2. La película")
                cambio = int(input())  # Simulamos la entrada del usuario

                # Se le permite al usuario cambiar su elección de cine o de película para buscar nuevamente.
                if cambio == 1:
                    cineEscogido = cambioCine(cineEscogido, peliculaElegida)
                    continue  # Con el nuevo cine, volvemos a ejecutar el bucle.
                elif cambio == 2:
                    peliculaElegida = cambioPelicula(peliculaElegida, cineEscogido)
                    continue  # Con la nueva película, volvemos a ejecutar el bucle.
                else:
                    print("Entrada no válida")
                    continue
            
            condicion = False

        condicion = True

        print("A continuación se muestran la/las funciones que puede elegir para ver " + peliculaElegida.getTitulo())
        funcionesPosibles = cineEscogido.obtenerFunciones(peliculaElegida)

        for i in range(1, len(funcionesPosibles) + 1):
            horaFuncion = funcionesPosibles[i - 1].definirMomentoDelDia()
            print(f"{i}. {funcionesPosibles[i - 1].getDia()}, sala {funcionesPosibles[i - 1].getSala().getNumero()}, a las {horaFuncion}{funcionesPosibles[i - 1].getMomentoDelDia()}.")

        # Muy importante preguntarle al usuario si quiere continuar con el proceso o darlo por terminado.
        print("¿Desea hacer una reserva? \n1. Sí\n2. No. Salir.")
        reserva = None

        # Nos aseguramos de que escoja correctamente. Si quiere terminar, damos por finalizada la operación.
        while condicion:
            reserva = int(input())  # Simulamos la entrada del usuario
            if reserva != 1 and reserva != 2:
                print("Entrada no válida")
                continue
            elif reserva == 2:
                return  # Salir del programa
            condicion = False

        condicion = True    
        funcionElegida = None

        # Dando una respuesta positiva le preguntamos qué función quiere tomar, si solo hay una función la tomamos simplemente:
        if len(funcionesPosibles) == 1:
            funcionElegida = funcionesPosibles[0]
        else:
            print("Elija el número de la función a la que desea asistir: ")
            while condicion:
                funcion = int(input())  # Simulamos la entrada del usuario
                if funcion <= 0 or funcion > len(funcionesPosibles):
                    print("Entrada no válida")
                    continue
                funcionElegida = funcionesPosibles[funcion - 1]
                condicion = False
        condicion = True
        horaFuncion = funcionElegida.definirMomentoDelDia()

        # Ahora mostramos en pantalla todas las sillas de sala, y le decimos que elija por fila y columna el asiento:
        print("Esta es la distribución de las sillas de la sala en la función escogida:")
        print(funcionElegida.getSala().estadoSilleteria())
        print("Ingrese por fila y por columna el asiento que desea ocupar:")
        
        # En este bucle se verifica que el asiento elegido no se encuentre ocupado, de ser así, se pregunta nuevamente:
        while condicion:
            print("Fila: ")
            fila = int(input())  
            print("Columna: ")
            columna = int(input())
            
            if funcionElegida.getSala().estaDisponible(fila - 1, columna - 1):
                print("El asiento está disponible")
                condicion = False
            else:
                print("El asiento no está disponible, intente con otro")
                continue

        condicion = True
        precioBoleto = funcionElegida.getPrecio()  # Precio de la entrada.

        # Ahora se continúa con el pago de la entrada. Si el usuario no tiene tarjeta, directamente vamos al pago con su saldo personal.
        print("Se procede con el pago de su boleto")
        tieneTarjeta = cliente.getTarjeta()  # Si tiene tarjeta o no.

        if not tieneTarjeta:
            print("Como no tiene ninguna tarjeta a su nombre, se procede al pago con su saldo")
            print(f"Precio de la entrada: {precioBoleto}     Su saldo: {cliente.getSaldo()}")
            
            resultado = cliente.pagarConSaldo(precioBoleto)
            
            if resultado:
                funcionElegida.getSala().reservarSilla(fila - 1, columna - 1)  # Marcar como ocupado el asiento.
                print(f"Se ha realizado exitosamente el pago.\nDetalles de la operación:\nNombre del Cliente: {cliente.getNombre()}\nIdentificación: {cliente.getIdentificacion()}\nPelícula: {peliculaElegida.getTitulo()}\nSala de la proyección: {funcionElegida.getSala().getNumero()}\nDía: {funcionElegida.getDia()}\nHora de la función: {horaFuncion}{funcionElegida.getMomentoDelDia()}\nCine: {cineEscogido.getNombre()}\nAsiento: fila {fila} y columna {columna}\nPrecio de la boleta: {precioBoleto}")  # Detalles de la compra
                return
            else:
                print("No tienes suficiente dinero para comprar la boleta")
                return  # Finalizar el proceso si no hay dinero suficiente.
        
        # Hasta este punto llegamos si el usuario tiene tarjeta de membresía.
        # Le preguntamos si quiere pagar con tarjeta o con su saldo personal.
        while condicion:
            print("¿Desea llevar a cabo el pago con su tarjeta?\n1. Sí\n2. No")
            pago = int(input())  # Simulamos la entrada del usuario
            
            if pago == 1:
                condicion = False  # Si elige con tarjeta, salimos del bucle.
            elif pago == 2:
                print("Se procede entonces con el pago desde su saldo")
                print(f"Precio de la entrada: {precioBoleto}     Su saldo: {usuario.getSaldo()}")
                
                resultado = usuario.pagarConSaldo(precioBoleto)
                
                if resultado:
                    funcionElegida.getSala().reservarSilla(fila - 1, columna - 1)
                    print(f"Se ha realizado exitosamente el pago.\nDetalles de la operación:\nNombre del Cliente: {usuario.getNombre()}\nIdentificación: {usuario.getIdentificacion()}\nPelícula: {peliculaElegida.getTitulo()}\nSala de la proyección: {funcionElegida.getSala().getNumero()}\nDía: {funcionElegida.getDia()}\nHora de la función: {horaFuncion}{funcionElegida.getMomentoDelDia()}\nCine: {cineEscogido.getNombre()}\nAsiento: fila {fila} y columna {columna}\nPrecio de la boleta: {precioBoleto}")  # Detalles de la compra.
                    condicion = False
                    return
                else:
                    print("No tienes suficiente dinero para comprar la boleta")
                    return  # Si no tiene suficiente dinero, damos por finalizada la operación.
            else:
                print("Entrada no válida.")
                continue

        condicion = True
        # En este bucle se va a tratar del pago con el saldo o los puntos de la tarjeta del cliente
        while condicion:
            print("Desea pagar con:\n1. El saldo de su tarjeta\n2. Los puntos de su tarjeta")
            pago = int(input())  # Simulamos la entrada del usuario
            
            if pago == 1:
                print(f"Precio de la entrada: {precioBoleto}   Saldo de su tarjeta: {cliente.getSaldoTarjeta()}")
                if cliente.pagarSaldoTarjeta(precioBoleto):
                    funcionElegida.getSala().reservarSilla(fila - 1, columna - 1)
                    puntosGanados = cliente.agregarPuntos()  # Si se completa el pago con el saldo de la tarjeta, se agregan los puntos correspondientes de acuerdo al plan de la tarjeta.
                    print(f"Has ganado {puntosGanados} puntos por tu compra, gracias a que tienes plan {cliente.getTipoTarjeta()}.")  # Se le informa al cliente sobre los puntos.
                    condicion = False
                else:
                    print("No tiene saldo suficiente en su tarjeta. ¿Quiere pagar con los puntos de la tarjeta?:\n1. Sí\n2. Finalizar Proceso")
                    otroPago = int(input())
                    if otroPago == 1:
                        precioBoleto = funcionElegida.getPrecio() / 100  # Si paga con los puntos de la tarjeta se hace la conversión de los puntos gastados.
                        print(f"Precio de la entrada a puntos: {precioBoleto}   Puntos de su tarjeta: {cliente.getPuntosTarjeta()}")
                        if cliente.pagarPuntosTarjeta(precioBoleto):
                            funcionElegida.getSala().reservarSilla(fila - 1, columna - 1)
                            condicion = False
                        else:
                            print("No tienes tampoco puntos suficientes en la tarjeta. Finalizando el proceso.")
                            return
                    elif otroPago == 2:
                        condicion = False
                        return
                    else:
                        print("Entrada no válida")
                        continue
            elif pago == 2:
                print(f"Precio de la entrada a puntos: {precioBoleto}   Puntos de su tarjeta: {cliente.getPuntosTarjeta()}")
                if cliente.pagarPuntosTarjeta(precioBoleto):
                    funcionElegida.getSala().reservarSilla(fila - 1, columna - 1)
                    precioBoleto = funcionElegida.getPrecio() / 100
                    condicion = False
                else:
                    print("No tiene suficientes puntos en su tarjeta. ¿Quiere pagar con el saldo de la tarjeta:\n1. Sí\n2. Finalizar Proceso")
                    otroPago = int(input())
                    if otroPago == 1:
                        print(f"Precio de la entrada: {precioBoleto}   Saldo de su tarjeta: {cliente.getSaldoTarjeta()}")
                        if cliente.pagarSaldoTarjeta(precioBoleto):
                            funcionElegida.getSala().reservarSilla(fila - 1, columna - 1)
                            puntosGanados = cliente.agregarPuntos()
                            print(f"Has ganado {puntosGanados} puntos por tu compra, gracias a que tienes plan {cliente.getTipoTarjeta()}")
                            condicion = False
                        else:
                            print("No tienes tampoco saldo suficiente. Finalizando el proceso")
                            return
                    elif otroPago == 2:
                        condicion = False
                        return
                    else:
                        print("Entrada no válida")
                        continue
        print(f"Se ha realizado exitosamente el pago.\nDetalles de la operación:\nNombre del Cliente: {cliente.getNombre()}\nIdentificación: {cliente.getIdentificacion()}\nPelícula: {peliculaElegida.getTitulo()}\nSala de la proyección: {funcionElegida.getSala().getNumero()}\nDía: {funcionElegida.getDia()}\nHora de la función: {horaFuncion}{funcionElegida.getMomentoDelDia()}\nCine: {cineEscogido.getNombre()}\nAsiento: fila {fila} y columna {columna}\nPrecio de la boleta: {precioBoleto}")  # Detalles de la compra.

        
    @staticmethod
    def cambioCine(cine, pelicula):
        cines = Cine.cines
        cinesConPelicula = []
        cineEscogido = None

        # En caso de que el usuario quiera cambiar de cine, se buscan todos los que tengan funciones para la película.
        for j in range(len(cines)):
            if cines[j] != cine:
                if cines[j].hayPelicula(pelicula):
                    cinesConPelicula.append(cines[j])

        # Es posible que no haya ningún cine con función para la película, se lo decimos al usuario
        if len(cinesConPelicula) == 0:
            print(f"En este momento, {pelicula.getTitulo()} no tiene ninguna función activa en ninguno de nuestros cines, lo único que puedes hacer es cambiar de película")
            return cine

        # Se muestran todas las opciones que tiene para cambiar el cine
        print(f"Puedes encontrar funciones para {pelicula.getTitulo()} en:")
        for i in range(1, len(cinesConPelicula) + 1):
            print(f"{i}. {cinesConPelicula[i - 1].getNombre()}")

        print("\nElige el cine: ")

        # En este bucle nos aseguramos que su elección sea válida.
        condicion = True
        while condicion:
            decision = int(input())  # Simulamos la entrada del usuario
            if decision <= 0 or decision > len(cinesConPelicula):
                print("Entrada no válida")
                continue
            cineEscogido = cinesConPelicula[decision - 1]
            condicion = False

        return cineEscogido  # Retornamos el nuevo cine.

    @staticmethod
    def cambioPelicula(pelicula, cine):
        peliculaEscogida = None

        # Como el usuario quiere cambiar la película, le mostramos cuáles tienen función en la semana.
        print(f"Estas son las películas que están incluidas en la programación semanal \n{cine.enseñarFunciones()}")

        peliculasElegibles = cine.peliculasActivas()  # Obtenemos todas estas películas para mostrarlas.
        print("Elige el número de la película por la que quieres cambiar: ")

        for j in range(1, len(peliculasElegibles) + 1):
            print(f"{j}. {peliculasElegibles[j - 1].getTitulo()}")

        # Nos aseguramos de que haga una elección correcta.
        condicion = True
        while condicion:
            eleccion = int(input())  # Simulamos la entrada del usuario
            if eleccion <= 0 or eleccion > len(peliculasElegibles):
                print("Entrada no válida")
                continue
            peliculaEscogida = peliculasElegibles[eleccion - 1]
            condicion = False

        return peliculaEscogida  # Retornamos la nueva película.



    @staticmethod
    def gestionarZonaDeJuegos(app):
        """Gestiona las zonas de juegos utilizando la interfaz gráfica."""

        Interfaz.limpiarFormulario(app)        
        # Paso 1: Actualización de dinero recaudado en todas las zonas de juegos
        for cine in Cine.cines:
            if cine.zonaDeJuegos:
                cine.zonaDeJuegos.actualizarDineroRecaudado()

        # Mostrar informe de máquinas dañadas
        informe = "Informe de máquinas dañadas:\n"
        for cine in Cine.cines:
            if cine.zonaDeJuegos:
                informe += cine.zonaDeJuegos.informeMaquinas() + "\n"
    
        # Acumular texto en resultLabel
        app.resultLabel.config(text=app.resultLabel.cget("text") + informe)

        # Paso 2: Selección de la zona de juegos
        zonasDisponibles = [cine for cine in Cine.cines if cine.zonaDeJuegos]
        if not zonasDisponibles:
            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo hay zonas de juegos disponibles.")
            return

        criterios = ["Ingrese la zona de juegos para reparación"]
        opciones_zonas = [cine.zonaDeJuegos.getNombre() for cine in zonasDisponibles]

        app.procesoLabel.config(text="Seleccionar Zona de Juegos")
        app.indicacionLabel.config(text="Seleccione la zona donde desea reparar una máquina")
        app.actualizarFormulario("Zonas Disponibles", criterios, "Valores", opciones_zonas)

        # Botón 'Aceptar' pasa a seleccionar la máquina dañada
        def seleccionarZona():
            zona_nombre = app.frame.getValue("Ingrese la zona de juegos para reparación")
        
            # Buscar la zona seleccionada por su nombre
            zonaActual = None
            for cine in zonasDisponibles:
                if cine.zonaDeJuegos.getNombre() == zona_nombre:
                    zonaActual = cine.zonaDeJuegos
                    break
        
            if zonaActual is None:
                app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una zona válida.")
                return

            maquinasDañadas = zonaActual.getMaquinasDañadas()
        
            if not maquinasDañadas:
                app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo hay máquinas dañadas en la zona seleccionada.")
                return

            # Paso 3: Selección de la máquina dañada
            criterios_maquinas = ["Ingrese la máquina dañada"]
            opciones_maquinas = [maquina.getNombre() for maquina in maquinasDañadas]
            app.procesoLabel.config(text="Seleccionar Máquina a Reparar")
            app.indicacionLabel.config(text="Seleccione la máquina que desea reparar")
            app.actualizarFormulario("Máquinas Dañadas", criterios_maquinas, "Valores", opciones_maquinas)

            # Botón 'Aceptar' para realizar la reparación
            def seleccionarMaquina():
                maquina_nombre = app.frame.getValue("Ingrese la máquina dañada")
            
                # Buscar la máquina seleccionada por su nombre
                maquinaSeleccionada = None
                for maquina in maquinasDañadas:
                    if maquina.getNombre() == maquina_nombre:
                        maquinaSeleccionada = maquina
                        break
            
                if maquinaSeleccionada is None:
                    app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una máquina válida.")
                    return

                # Reparación
                resultado_reparacion = Bodega.allBodegas[0].realizarMantenimiento(zonaActual, maquinasDañadas.index(maquinaSeleccionada))
                app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nReparación realizada: {resultado_reparacion}")

                # Recomendación de movimiento
                recomendacion = zonaActual.recomendarMovimiento(maquinaSeleccionada)
                app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nRecomendación: {recomendacion}")

                criterios=["Ingrese la zona de destino"]
                app.procesoLabel.config(text="Seleccionar Zona de Destino")
                app.indicacionLabel.config(text="Seleccione la zona donde desea mover la máquina")
                app.actualizarFormulario("Zonas Disponibles", criterios, "Valores", opciones_zonas)

                # Botón 'Aceptar' para mover la máquina
                def seleccionarZonaDestino():
                    zona_destino_nombre = app.frame.getValue("Ingrese la zona de destino")
                    print(zona_destino_nombre)
                    # Buscar la zona de destino por su nombre
                    zonaDestino = None
                    for cine in zonasDisponibles:
                        if cine.zonaDeJuegos.getNombre() == zona_destino_nombre:
                            zonaDestino = cine.zonaDeJuegos
                            break
                
                    if zonaDestino is None:
                        app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una zona válida.")
                        return

                    if zonaActual != zonaDestino:
                        resultado_movimiento = zonaActual.moverMaquina(zonaDestino, maquinasDañadas.index(maquinaSeleccionada))
                        app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nMovimiento realizado: {resultado_movimiento}")
                    else:
                        app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nLa máquina permanecerá en {zonaActual.getNombre()}")
                    # Paso 4: Aplicar incentivos
                    aplicarIncentivo()

                def aplicarIncentivo():
        # Preguntar al usuario si desea aplicar incentivos
                    criterios_incentivo = ["¿Desea aplicar algún incentivo en una zona de juegos?"]
                    opciones_incentivo = ["Si", "No"]

                    app.procesoLabel.config(text="Aplicar Incentivos")
                    app.indicacionLabel.config(text="Seleccione si desea aplicar un incentivo")
                    app.actualizarFormulario("Aplicar Incentivo", criterios_incentivo, "Opciones", opciones_incentivo)

                    def seleccionarIncentivo():
                        opcionIncentivo = app.frame.getValue("¿Desea aplicar algún incentivo en una zona de juegos?")

                        if opcionIncentivo == "Si":
                            criterios_tipo_incentivo = ["Seleccione el tipo de incentivo"]
                            opciones_tipo_incentivo = ["Rebajar el precio de una maquina", "Regalar un bono por el uso de una maquina"]
                            app.procesoLabel.config(text="Tipo de Incentivo")
                            app.indicacionLabel.config(text="Seleccione el tipo de incentivo")
                            app.actualizarFormulario("Tipo de Incentivo", criterios_tipo_incentivo, "Opciones", opciones_tipo_incentivo)

                            def seleccionarTipoIncentivo():
                                tipoIncentivo = app.frame.getValue("Seleccione el tipo de incentivo")

                                if tipoIncentivo == "Rebajar el precio de una maquina":
                                    # Obtener las dos máquinas que menos venden
                                    dosMenosVenden = Maquina.obtenerDosMaquinasMenosVenden()

                                    if not dosMenosVenden:
                                        app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo hay máquinas disponibles para recomendar.")
                                    else:
                                        app.resultLabel.config(text=app.resultLabel.cget("text") + "\nRecomendación de cambio de precio:\n" +
                                                        "\n".join([maquina.getNombre() for maquina in dosMenosVenden]))

                                    # Seleccionar la zona donde aplicar la rebaja
                                    app.procesoLabel.config(text="Seleccionar Zona para Rebaja")
                                    app.indicacionLabel.config(text="Seleccione la zona donde desea aplicar la rebaja")
                                    app.actualizarFormulario("Zonas para Rebaja", ["Seleccione una zona"], "Opciones", opciones_zonas)

                                    def seleccionarZonaRebaja():
                                        zona_rebaja_nombre = app.frame.getValue("Seleccione una zona")
                                        zonaRebaja = None
                                        for cine in zonasDisponibles:
                                            if cine.zonaDeJuegos.getNombre() == zona_rebaja_nombre:
                                                zonaRebaja = cine.zonaDeJuegos
                                                break

                                        if zonaRebaja is None:
                                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una zona válida.")
                                            return

                                        # Seleccionar la máquina para rebajar el precio
                                        maquinasEnZona = zonaRebaja.getMaquinas()
                                        opciones_maquinas_rebaja = [maquina.getNombre() for maquina in maquinasEnZona]
                                        app.actualizarFormulario("Máquinas para Rebaja", ["Seleccione una máquina"], "Opciones", opciones_maquinas_rebaja)

                                        def seleccionarMaquinaRebaja():
                                            maquina_rebaja_nombre = app.frame.getValue("Seleccione una máquina")
                                            maquinaRebajada = None
                                            for maquina in maquinasEnZona:
                                                if maquina.getNombre() == maquina_rebaja_nombre:
                                                    maquinaRebajada = maquina
                                                    break

                                            if maquinaRebajada is None:
                                                app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una máquina válida.")
                                                return

                                            # Ingresar el nuevo precio
                                            app.procesoLabel.config(text="Nuevo Precio")
                                            app.indicacionLabel.config(text=f"Ingrese el nuevo precio para {maquinaRebajada.getNombre()}")
                                            app.actualizarFormulario("Nuevo Precio", ["Nuevo Precio"], "Valores", [])

                                            def confirmarNuevoPrecio():
                                                nuevoPrecio = float(app.frame.getValue("Nuevo Precio"))
                                                maquinaRebajada.setPrecioUso(nuevoPrecio)
                                                app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nEl precio de {maquinaRebajada.getNombre()} ha sido rebajado a {nuevoPrecio}")

                                            app.frame.setComando(confirmarNuevoPrecio)

                                        app.frame.setComando(seleccionarMaquinaRebaja)
                                    app.frame.setComando(seleccionarZonaRebaja)

                                elif tipoIncentivo == "Regalar un bono por el uso de una maquina":
                                    # Seleccionar la zona donde aplicar el bono
                                    app.procesoLabel.config(text="Seleccionar Zona para Bono")
                                    app.indicacionLabel.config(text="Seleccione la zona donde desea aplicar el bono")
                                    app.actualizarFormulario("Zonas para Bono", ["Seleccione una zona"], "Opciones", opciones_zonas)

                                    def seleccionarZonaBono():
                                        zona_bono_nombre = app.frame.getValue("Seleccione una zona")
                                        zona = None
                                        for cine in zonasDisponibles:
                                            if cine.zonaDeJuegos.getNombre() == zona_bono_nombre:
                                                zona = cine.zonaDeJuegos
                                                break

                                        if zona is None:
                                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una zona válida.")
                                            return

                                        # Seleccionar la máquina para aplicar el bono
                                        maquinasEnZona = zona.getMaquinas()
                                        opciones_maquinas_bono = [maquina.getNombre() for maquina in maquinasEnZona]
                                        app.actualizarFormulario("Máquinas para Bono", ["Seleccione una máquina"], "Opciones", opciones_maquinas_bono)

                                        def seleccionarMaquinaBono():
                                            maquina_bono_nombre = app.frame.getValue("Seleccione una máquina")
                                            maquina = None
                                            for maquina in maquinasEnZona:
                                                if maquina.getNombre() == maquina_bono_nombre:
                                                    maquina = maquina
                                                    break

                                            if maquina is None:
                                                app.resultLabel.config(text=app.resultLabel.cget("text") + "\nSeleccione una máquina válida.")
                                                return

                                            # Activar el bono en la máquina seleccionada
                                            maquina.activarBono()
                                            app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nEl bono ha sido activado para {maquina.getNombre()}")

                                        app.frame.setComando(seleccionarMaquinaBono)

                                    app.frame.setComando(seleccionarZonaBono)

                            app.frame.setComando(seleccionarTipoIncentivo)

                        else:
                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo se aplicarán incentivos.")
        
                    app.frame.setComando(seleccionarIncentivo)
                app.frame.setComando(seleccionarZonaDestino)
            app.frame.setComando(seleccionarMaquina)
        app.frame.setComando(seleccionarZona)

    @staticmethod
    def gestionarPeliculas(app):
        Interfaz.limpiarFormulario(app)
        # Paso 1: Mostrar calificaciones de las películas
        calificaciones = []
        for cine in Cine.cines:
            calificaciones.append(f"Cine: {cine.getNombre()}")
            calificaciones.extend(cine.obtenerCalificacionesPeliculas())
        
        # Mostrar las calificaciones en la etiqueta de resultado
        app.resultLabel.config(text="\n".join(calificaciones))

        # Paso 2: Selección del cine
        criterios = ["Nombre del cine"]
        app.actualizarFormulario("Ingrese el cine", criterios, "Cine seleccionado")

        def seleccionarCine():
            cineSeleccionado = app.frame.getValue("Nombre del cine")
            cineOrigen = next(cine for cine in Cine.cines if cine.getNombre() == cineSeleccionado)

            # Paso 3: Selección de película
            peliculas=["Ingrese el titulo de la pelicula"]
            app.actualizarFormulario("Seleccione la película", peliculas, "Película seleccionada")

            def seleccionarPelicula():
                peliculaSeleccionada = app.frame.getValue("Ingrese el titulo de la pelicula")
                peliculaAIntercambiar = next(pelicula for pelicula in cineOrigen.peliculasActivas() if pelicula.getTitulo() == peliculaSeleccionada)
                
                # Paso 4: Recomendar una película para intercambio
                recomendacion = Pelicula.recomendarIntercambio(peliculaAIntercambiar)
                app.resultLabel.config(text=f"Recomendación: {recomendacion}")
                
                # Selección de nuevo cine para el intercambio
                criterios = ["Ingrese el nombre del cine de la pelicula a intercambiar"]
                app.actualizarFormulario("Seleccione el nuevo cine", criterios, "Cine destino")
                
                def seleccionarNuevoCine():
                    nuevoCineSeleccionado = app.frame.getValue("Ingrese el nombre del cine de la pelicula a intercambiar")
                    nuevoCine = next(cine for cine in Cine.cines if cine.getNombre() == nuevoCineSeleccionado)
                    
                    # Paso 5: Selección de película en el nuevo cine
                    peliculasNuevoCine = ["Ingrese el titulo de la pelicula intercambio"]
                    app.actualizarFormulario("Seleccione la película en el nuevo cine", peliculasNuevoCine, "Película destino")
                    
                    def seleccionarPeliculaDestino():
                        peliculaIntercambioSeleccionada = app.frame.getValue("Ingrese el titulo de la pelicula intercambio")
                        peliculaIntercambio = next(pelicula for pelicula in nuevoCine.peliculasActivas() if pelicula.getTitulo() == peliculaIntercambioSeleccionada)

                        # Confirmar intercambio
                        confirmacion = messagebox.askyesno("Confirmar Intercambio", f"¿Desea intercambiar {peliculaAIntercambiar.getTitulo()} por {peliculaIntercambio.getTitulo()}?")
                        if confirmacion:
                            resultadoIntercambio = Funcion.realizarIntercambio(cineOrigen,nuevoCine,peliculaAIntercambiar, peliculaIntercambio)
                            app.resultLabel.config(text=resultadoIntercambio)
                        
                            # Aplicar incentivos (bono o descuento)
                            incentivos = ["Ingrese un incentivo"]
                            app.actualizarFormulario("Seleccione un incentivo", incentivos, "Incentivo")
                            def aplicarIncentivo():
                                incentivoSeleccionado = app.frame.getValue("Ingrese un incentivo")
                                if incentivoSeleccionado == "Rebajar precio":
                                    # Rebajar el precio de la entrada
                                    calificaciones = []
                                    for cine in Cine.cines:
                                        calificaciones.append(f"Cine: {cine.getNombre()}")
                                        calificaciones.extend(cine.obtenerCalificacionesPeliculas())
                                    app.resultLabel.config(text="\n".join(calificaciones))
                                    funciones = ["Ingrese el titulo de la pelicula perteneciente a la funcion","Ingrese su numero de sala"]
                                    app.actualizarFormulario("Seleccione la función", funciones, "Función seleccionada")
                                
                                    def aplicarPrecio():
                                        titulo = app.frame.getValue("Ingrese el titulo de la pelicula perteneciente a la funcion")
                                        numSala=app.frame.getValue("Ingrese su numero de sala")
                                        print(numSala,titulo)
                                        for cine in Cine.cines:
                                            for f in cine.totalFunciones():
                                                if f.getPelicula().getTitulo()==titulo and f.getSala().getNumero()==numSala:
                                                    funcion=f
                                                    if funcion:
                                                        break
                                        precio = ["Ingrese el nuevo precio"]
                                        app.actualizarFormulario("Nuevo precio", precio, "Valor")
                                        nuevoPrecio=int(app.frame.getValue("Ingrese el nuevo precio"))
                                        funcion.setPrecio(nuevoPrecio)
                                        app.resultLabel.config(text=f"Nuevo precio: {nuevoPrecio}")
                                
                                    app.frame.setComando(aplicarPrecio)

                                elif incentivoSeleccionado == "Aplicar bono":
                                    peliculaIntercambio.activarBono()
                                    app.resultLabel.config(text=f"Bono activado para {peliculaIntercambio.getTitulo()}")
                        
                        app.frame.setComando(aplicarIncentivo)

                    app.frame.setComando(seleccionarPeliculaDestino)
                app.frame.setComando(seleccionarNuevoCine)
            app.frame.setComando(seleccionarPelicula)
        app.frame.setComando(seleccionarCine)
    
    @staticmethod
    def gestionarCartelera():
        print("Elige el cine al que deseas modificar su cartelera semanal:\n")
        listaVacios = None
        cine = None
        #Le pedimos al usuario que elija el cine al que le quiere añadir funciones.
        for i in range(len(Cine.cines)):
            print(f"{i+1}. {Cine.cines[i].getNombre()}.")
        while True:
            eleccion = int(input("->:"))
            cine = Cine.cines[eleccion-1]
            listaVacios = cine.hallarEspaciosSinFuncion() #Tomamos todas los posibles horarios para añadir funciones.
            if(listaVacios == -1): #Consideremos el caso donde no haya cupo.
                print("Este cine no tiene huecos para agregar funciones, selecciona otro")
                continue
            else:
                break
        print("Esta es la programación semanal que actualmente se tiene en el cine escogido:")
        #Mostramos con una tabla la programación semanal.
        
        peliculasListas = []
        print("Estos son los espacios libres en el cine escogido:")
        for j in range(len(listaVacios)):
            print(f"{j+1}. Día {listaVacios[j][0]}, a las {listaVacios[j][1]}")
        condicion = True
        while condicion:
            horaPeli = None
            espacio = None
            diaPeli = None                
            if len(listaVacios) == 1:
                espacio = listaVacios[0]
                print("Como solo hay una alternativa, la tomamos de inmediato.")
            else:
                print("Elige el espacio que deseas modificar:")
                eleccion = int(input("->:"))
                espacio = listaVacios[eleccion-1]
                if len(espacio) == 4:
                    print("Ya asignaste película para este espacio:")
                    continue
            peliculasParaElegir = Pelicula.ObtenerPeliculasElegibles(espacio[1], espacio[0], cine)
            if len(peliculasParaElegir)==1:
                horaPeli = espacio[1]
                diaPeli = espacio[0]
                print(f"Solo hallamos una alternatva, lo tomamos de inmediato: {peliculasParaElegir[0].getTitulo()}, calificación: {str(peliculasParaElegir[0].getCalificacionPromedio())}")
                peliculasListas += [[peliculasParaElegir[0],diaPeli, horaPeli, espacio[2]]]
                espacio.append("A")
            else:
                print("Elige la película para rellenar el espacio:\n")
                for i in range(len(peliculasParaElegir)):
                    print(f"{str(i+1)}. {peliculasParaElegir[i].getTitulo()}, calificación: {str(peliculasParaElegir[i].getCalificacionPromedio())}")
                eleccion = int(input("->:"))
                diaPeli = espacio[0]
                horaPeli = espacio[1]
                peliculasListas += [[peliculasParaElegir[eleccion-1], diaPeli, horaPeli, espacio[2]]]
                espacio.append("A")
            numeroVacios = 0
            for espacio in listaVacios:
                if len(espacio) == 3:
                    break
                else:
                    numeroVacios += 1
            if numeroVacios == len(listaVacios):
                print("No hay más espacios.")
                break
            print("¿Quiéres continuar llenando espacios? (S/N)")
            decision = input("->:")
            if (decision == "S"):
                continue
            elif (decision == "N"):
                print("Saliendo")
                break

        #Por cada película para agregar debemos preguntar la sala y definir el precio de entrada
        
        for adicion in peliculasListas:
            print(f"Elige la sala de proyección para {adicion[0].getTitulo()}, del día {adicion[1]} y a las {adicion[2]}")
            for x in range(len(adicion[3])):
                print(f"{x+1}. Sala {adicion[3][x].getNumero()}. Capacidad: {adicion[3][x].getCapacidad()} butacas")
            eleccion = int(input("Elige la sala que prefieras: "))
            salaEscogida = adicion[3][eleccion-1]
            precioEntrada = int(input("Digita el precio de la entrada: "))
            funcionAnadida = Funcion.agregarFuncion(cine, adicion[1], adicion[2], adicion[0], precioEntrada, salaEscogida)
            for elemento in peliculasListas:
                if adicion != elemento:
                    if int(elemento[2][:2]) + 2 == int(adicion[2][:2]) or int(elemento[2][:2]) + 2 == int(adicion[2][:2]):
                        for salaElemento in elemento[3]:
                            if salaElemento == salaEscogida:
                                elemento[3].remove(salaElemento)
    
    def menuCreacion(app):
        Interfaz.limpiarFormulario(app)
        opciones = [
            "Crear Zona de Juegos",
            "Crear Máquina",
            "Crear Cliente",
            "Crear Cine",
            "Crear Película",
            "Crear Sala",
            "Crear Función",
            "Salir"
     ]
    
        # Función que se ejecuta cuando cambias la opción del combobox
        def changed(event):
            app.entrada.delete(0, "end")  # Limpia el contenido de la entrada
            app.entrada.insert(0, combo.get())  # Inserta el valor seleccionado del combobox
    
        # Configura las etiquetas del proceso
        app.resultLabel.config(text="")
        app.procesoLabel.config(text="Menú de Creación")
        app.indicacionLabel.config(text="Seleccione una opción del menú")
    
        # Define la variable de valor por defecto para el combobox
        valorDefecto = tk.StringVar(value="Opciones de creación")
    
        # Crea el combobox y vincula el evento de cambio de selección
        combo = ttk.Combobox(app, values=opciones, textvariable=valorDefecto)
        combo.bind("<<ComboboxSelected>>", changed)
        combo.pack(side="top", anchor="center", pady=5)
        app.widgetsSueltos.append(combo)
    
        # Crea el campo de entrada para mostrar la opción seleccionada (si es necesario)
        app.entrada = tk.Entry(app)  # Define app.entrada para que esté accesible en el ámbito de la clase
        app.entrada.pack(side="top", anchor="center", pady=5)
        app.widgetsSueltos.append(app.entrada)

        app.actualizarFormulario("",[],"")
    
        # Si no se va a utilizar actualizarFormulario aquí, puedes eliminarlo o ajustarlo
        # app.actualizarFormulario("", [], "")
    
        # Función para aceptar la opción seleccionada
        def aceptarOpcion():
            opcion = app.entrada.get()  # Obtiene el valor de la entrada
            if opcion == "Crear Zona de Juegos":
                crearZonaDeJuegos(app)
            elif opcion == "Crear Máquina":
                 crearMaquina(app)
            elif opcion == "Crear Película":
                 crearPelicula(app)
            elif opcion == "Crear Función":
                 crearFuncion(app)
            elif opcion == "Crear Cliente":
                 crearCliente(app)
            elif opcion == "Crear Cine":
                 crearCine(app)
            elif opcion == "Crear Sala":
                 crearSala(app)    
        app.frame.setComando(aceptarOpcion)  # Vincula la función aceptarOpcion con el botón 'Aceptar'
    
        # Función para crear Zona de Juegos
        def crearZonaDeJuegos(app):
            criterios = ["Nombre de la Zona", "Horario"]
            app.procesoLabel.config(text="Crear Zona de Juegos")
            app.indicacionLabel.config(text="Ingrese el nombre y horario de la nueva zona de juegos")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos Zona de Juegos", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación de la zona
            def aceptarZona():
                nombreZona = app.frame.getValue("Nombre de la Zona")
                horario = app.frame.getValue("Horario")
                zona = ZonaDeJuegos(nombreZona, horario)
                app.resultLabel.config(text=f"Zona de Juegos creada: {zona}")

            app.frame.setComando(aceptarZona)  # Vincula aceptarZona con el botón 'Aceptar' para la creación de la zona
        def crearMaquina(app):
            criterios = ["Nombre de la maquina", "Tipo de maquina","Materiales necesarios para la maquina","Precio de la maquina"]
            app.procesoLabel.config(text="Crear Maquina")
            app.indicacionLabel.config(text="Ingrese las especificaciones de la maquina")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos Maquina", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación de la maquina
            def aceptarMaquina():
                nombreMaquina = app.frame.getValue("Nombre de la maquina")
                tipo = app.frame.getValue("Tipo de maquina")
                materiales = int(app.frame.getValue("Materiales necesarios para la maquina"))
                precio = float(app.frame.getValue("Precio de la maquina"))
                maquina=Maquina(nombreMaquina,tipo,materiales,precio)
                app.resultLabel.config(text=f"Maquina creada: {maquina}")

            app.frame.setComando(aceptarMaquina)  # Vincula aceptarMaquina con el botón 'Aceptar' para la creación de la maquina
        def crearPelicula(app):
            criterios = ["Titulo de la pelicula", "Genero","Durcion (en horas y minutos, formato HH:MM)"]
            app.procesoLabel.config(text="Crear Pelicula")
            app.indicacionLabel.config(text="Ingrese las especificaciones de la pelicula")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos Pelicula", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación de la pelicula
            def aceptarPelicula():
                titulo = app.frame.getValue("Titulo de la pelicula")
                genero = app.frame.getValue("Genero")
                duracion = datetime.strptime((app.frame.getValue("Durcion (en horas y minutos, formato HH:MM)")),"%H:%M").time()
                
                pelicula=Pelicula(titulo,genero,duracion)
                app.resultLabel.config(text=f"Pelicula creada: {pelicula}")

            app.frame.setComando(aceptarPelicula)  # Vincula aceptarPelicula con el botón 'Aceptar' para la creación de la pelicual
        def crearFuncion(app):
            criterios = ["Tipo de funcion"]
            app.procesoLabel.config(text="Crear Funcion")
            app.indicacionLabel.config(text="Ingrese las especificaciones de la funcion")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos Funcion", criterios, "Valores", [])
            
            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación de la funcion
            def aceptarFuncion():
                tipoFuncion = app.frame.getValue("Tipo de funcion")
                funcion=Funcion(tipoFuncion)
                app.resultLabel.config(text=f"Funcion creada: {funcion}")

            app.frame.setComando(aceptarFuncion)  # Vincula aceptarFuncion con el botón 'Aceptar' para la creación de la funcion
        def crearCliente(app):
            criterios = ["Nombre del cliente", "Saldo","ID"]
            app.procesoLabel.config(text="Crear Cliente")
            app.indicacionLabel.config(text="Ingrese los datos del cliente")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos del cliente", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación del cliente
            def aceptarCliente():
                nombre = app.frame.getValue("Nombre del cliente")
                saldo = float(app.frame.getValue("Saldo"))
                id = int(app.frame.getValue("ID"))
                cliente=Cliente(nombre,saldo,id)
                app.resultLabel.config(text=f"Cliente creado: {cliente}")

            app.frame.setComando(aceptarCliente)  # Vincula aceptarCliente con el botón 'Aceptar' para la creación del cliente
        def crearCine(app):
            criterios = ["Nombre del cine"]
            app.procesoLabel.config(text="Crear Cine")
            app.indicacionLabel.config(text="Ingrese los datos del cine")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos del cine", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación del cine
            def aceptarCine():
                nombre = app.frame.getValue("Nombre del cine")
                cine=Cine(nombre)
                app.resultLabel.config(text=f"Cine creado: {cine}")

            app.frame.setComando(aceptarCine)  # Vincula aceptarCine con el botón 'Aceptar' para la creación del cine
        def crearSala(app):
            criterios = ["Numero de la sala","numero de filas","numero de columnas"]
            app.procesoLabel.config(text="Crear Sala")
            app.indicacionLabel.config(text="Ingrese las especificaciones de la sala")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos de la sala", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación de la sala
            def aceptarSala():
                numero = int(app.frame.getValue("Numero de la sala"))
                filas = int(app.frame.getValue("numero de filas"))
                columnas = int(app.frame.getValue("numero de columnas"))
                sala=Sala(numero,filas,columnas)
                app.resultLabel.config(text=f"Sala creada: {sala}")

            app.frame.setComando(aceptarSala)  # Vincula aceptarSala con el botón 'Aceptar' para la creación de la sala
    
    def menuAsignacion(app):
        Interfaz.limpiarFormulario(app)
        opciones = [
            "Asignar una zona de juegos a un cine",
            "Agregar una función a un cine",
            "Agregar una máquina a una zona de juegos",
            "Asignar una película a una función",
            "Asignar una sala a una función",
            "Salir"
        ]
    
        def changed(event):
            app.entrada.delete(0, "end")
            app.entrada.insert(0, combo.get())

        app.resultLabel.config(text="")
        app.procesoLabel.config(text="Menú de Asignaciones")
        app.indicacionLabel.config(text="Seleccione una opción del menú")

        valorDefecto = tk.StringVar(value="Opciones de asignación")
        combo = ttk.Combobox(app, values=opciones, textvariable=valorDefecto,width=40)
        combo.bind("<<ComboboxSelected>>", changed)
        combo.pack(side="top", anchor="center", pady=5)
        app.widgetsSueltos.append(combo)

        app.entrada = tk.Entry(app,width=40)
        app.entrada.pack(side="top", anchor="center", pady=5)
        app.widgetsSueltos.append(app.entrada)

        app.actualizarFormulario("", [], "")

        def aceptarOpcion():
            opcion = app.entrada.get()
            if opcion == "Asignar una zona de juegos a un cine":
                asignarZonaCine(app)
            elif opcion == "Agregar una función a un cine":
                agregarFuncionCine(app)
            elif opcion == "Agregar una máquina a una zona de juegos":
                agregarMaquinaZona(app)
            elif opcion == "Asignar una película a una función":
                asignarPeliculaFuncion(app)
            elif opcion == "Asignar una sala a una función":
                asignarSalaFuncion(app)
            elif opcion == "Salir":
                # Acción para salir
                pass

        app.frame.setComando(aceptarOpcion)

        def asignarZonaCine(app):
            if not ZonaDeJuegos.zonasDeJuegos or not Cine.cines:
                app.resultLabel.config(text="No hay zonas de juegos o cines disponibles.")
                return

            app.procesoLabel.config(text="Asignar Zona de Juegos a Cine")
            app.indicacionLabel.config(text="Seleccione una zona de juegos y un cine")
            combo.destroy()
            app.entrada.destroy()
            # Filtrar zonas de juegos que no tengan un cine asignado
            zonas = [zona.getNombre() for zona in ZonaDeJuegos.zonasDeJuegos if zona.getCine() is None]
            # Filtrar cines que no tengan una zona de juegos asignada
            cines = [cine.getNombre() for cine in Cine.cines if cine.getZonaDeJuegos() is None]

            valorDefecto1 = tk.StringVar(value="Opciones de zonas")
            valorDefecto2 = tk.StringVar(value="Opciones de cines")

            def changed1(event):
                app.entrada1.delete(0, "end")
                app.entrada1.insert(0, combo1.get())
            def changed2(event):
                app.entrada2.delete(0, "end")
                app.entrada2.insert(0, combo2.get())

            combo1 = ttk.Combobox(app, values=zonas, textvariable=valorDefecto1,width=40)
            combo1.bind("<<ComboboxSelected>>", changed1)
            combo1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo1)

            combo2 = ttk.Combobox(app, values=cines, textvariable=valorDefecto2,width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo2)

            app.entrada1 = tk.Entry(app,width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada1)

            app.entrada2 = tk.Entry(app,width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada2)

            app.actualizarFormulario("", [], "")

            def aceptarAsignacion():
                zonaSeleccionada = app.entrada1.get()
                cineSeleccionado = app.entrada2.get()
                zona = next(z for z in ZonaDeJuegos.zonasDeJuegos if z.getNombre() == zonaSeleccionada)
                cine = next(c for c in Cine.cines if c.getNombre() == cineSeleccionado)
                cine.setZonaDeJuegos(zona)
                zona.setCine(cine)
                app.resultLabel.config(text=f"Zona de juegos {zona.getNombre()} asignada al cine {cine.getNombre()}")

                combo1.destroy()
                combo2.destroy()
                app.entrada1.destroy()
                app.entrada2.destroy()
            app.frame.setComando(aceptarAsignacion)

        def agregarFuncionCine(app):
            if not Funcion.allFunciones or not Cine.cines:
                app.resultLabel.config(text="No hay funciones o cines disponibles.")
                return

            app.procesoLabel.config(text="Agregar Función a Cine")
            app.indicacionLabel.config(text="Seleccione una función, un cine y un dia")
            combo.destroy()
            app.entrada.destroy()
    
            funciones = [f"{funcion.getPelicula().getTitulo()},{funcion.getTipo()},{funcion.getSala()}" for funcion in Funcion.allFunciones]
            cines = [cine.getNombre() for cine in Cine.cines]
            dias=["Lunes","Martes","Jueves","Viernes","Sabado"]
    
            valorDefecto1 = tk.StringVar(value="Opciones de funciones")
            valorDefecto2 = tk.StringVar(value="Opciones de cines")
            valorDefecto3 = tk.StringVar(value="Opciones de Dias")
    
            def changed1(event):
                app.entrada1.delete(0, "end")
                app.entrada1.insert(0, combo1.get())
    
            def changed2(event):
                app.entrada2.delete(0, "end")
                app.entrada2.insert(0, combo2.get())
            
            def changed3(event):
                app.entrada3.delete(0, "end")
                app.entrada3.insert(0, combo3.get())
    
            combo1 = ttk.Combobox(app, values=funciones, textvariable=valorDefecto1, width=40)
            combo1.bind("<<ComboboxSelected>>", changed1)
            combo1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo1)
    
            combo2 = ttk.Combobox(app, values=cines, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo2)

            combo3 = ttk.Combobox(app, values=dias, textvariable=valorDefecto3, width=40)
            combo3.bind("<<ComboboxSelected>>", changed3)
            combo3.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo3)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada1)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada2)

            app.entrada3 = tk.Entry(app, width=40)
            app.entrada3.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada3)
    
            app.actualizarFormulario("", [], "")

            def aceptarAsignacion():
                funcionSeleccionada = app.entrada1.get()
                cineSeleccionado = app.entrada2.get()
        
                funcion = next(f for f in Funcion.allFunciones if f"{f.getPelicula().getTitulo()},{f.getTipo()},{f.getSala()}" == funcionSeleccionada)
                cine = next(c for c in Cine.cines if c.getNombre() == cineSeleccionado)

                if app.entrada3.get()=="Lunes":
                    funciones=cine.getLunes()
                elif app.entrada3.get()=="Martes":
                    funciones=cine.getMartes()
                elif app.entrada3.get()=="Jueves":
                    funciones=cine.getJueves()
                elif app.entrada3.get()=="Viernes":
                    funciones=cine.getViernes()
                elif app.entrada3.get()=="Sabado":
                    funciones=cine.getSabado()
        
                resultado = cine.agregarFuncion(funcion, funciones)

    # Validar el resultado y actualizar la etiqueta con el mensaje adecuado
                if resultado == "No se encontro una posicion apropiada":
                    app.resultLabel.config(text="No se encontró una posición apropiada")
                elif resultado == "No se pudo reorganizar las funciones para hacer espacio.":
                    app.resultLabel.config(text="No se pudo reorganizar las funciones para hacer espacio.")
                else:
                    app.resultLabel.config(text=f"Función {funcion.getPelicula().getTitulo()} {funcion.getTipo()} agregada al cine {cine.getNombre()}, el día {app.entrada3.get()}")
                
                combo1.destroy()
                combo2.destroy()
                combo3.destroy()
                app.entrada1.destroy()
                app.entrada2.destroy()
                app.entrada3.destroy()

            app.frame.setComando(aceptarAsignacion)


        def agregarMaquinaZona(app):
            if not Maquina.allMaquinas or not ZonaDeJuegos.zonasDeJuegos:
                app.resultLabel.config(text="No hay máquinas o zonas de juegos disponibles.")
                return

            app.procesoLabel.config(text="Agregar Máquina a Zona de Juegos")
            app.indicacionLabel.config(text="Seleccione una máquina y una zona de juegos")
            combo.destroy()
            app.entrada.destroy()
    
            maquinas = [maquina.getNombre() for maquina in Maquina.allMaquinas]
            zonas = [zona.getNombre() for zona in ZonaDeJuegos.zonasDeJuegos]
    
            valorDefecto1 = tk.StringVar(value="Opciones de máquinas")
            valorDefecto2 = tk.StringVar(value="Opciones de zonas")
    
            def changed1(event):
                app.entrada1.delete(0, "end")
                app.entrada1.insert(0, combo1.get())
    
            def changed2(event):
                app.entrada2.delete(0, "end")
                app.entrada2.insert(0, combo2.get())
    
            combo1 = ttk.Combobox(app, values=maquinas, textvariable=valorDefecto1, width=40)
            combo1.bind("<<ComboboxSelected>>", changed1)
            combo1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo1)
    
            combo2 = ttk.Combobox(app, values=zonas, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo2)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada1)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada2)
    
            app.actualizarFormulario("", [], "")

            def aceptarAsignacion():
                maquinaSeleccionada = app.entrada1.get()
                zonaSeleccionada = app.entrada2.get()
        
                maquina = next(m for m in Maquina.allMaquinas if m.getNombre() == maquinaSeleccionada)
                zona = next(z for z in ZonaDeJuegos.zonasDeJuegos if z.getNombre() == zonaSeleccionada)
                
                zonaAsignada = False

                for cine in Cine.cines:
                    if cine.getZonaDeJuegos() and cine.getZonaDeJuegos().getNombre() == zona.getNombre() and cine.getZonaDeJuegos().getHorario() == zona.getHorario():
                        cine.getZonaDeJuegos().getMaquinas().append(maquina)
                        maquinaAsignada = True
                        break

                # Si no se encontró la zona en ningún cine, asignar la máquina a la zona proporcionada
                if not maquinaAsignada:
                    zona.getMaquinas().append(maquina)
                app.resultLabel.config(text=f"Máquina {maquina.getNombre()} agregada a la zona de juegos {zona.getNombre()}")

                combo1.destroy()
                combo2.destroy()
                app.entrada1.destroy()
                app.entrada2.destroy()
    
            app.frame.setComando(aceptarAsignacion)

        

        def asignarPeliculaFuncion(app):
            if not Pelicula.totalPeliculas or not Funcion.allFunciones:
                app.resultLabel.config(text="No hay películas o funciones disponibles.")
                return

            app.procesoLabel.config(text="Asignar Película a Función")
            app.indicacionLabel.config(text="Seleccione una película y una función")
            combo.destroy()
            app.entrada.destroy()
    
            peliculas = [pelicula.getTitulo() for pelicula in Pelicula.totalPeliculas]
            funciones = [f"{funcion.getTipo()},{funcion.getSala()}" for funcion in Funcion.allFunciones if funcion.getPelicula() is None]
    
            valorDefecto1 = tk.StringVar(value="Opciones de películas")
            valorDefecto2 = tk.StringVar(value="Opciones de funciones")
    
            def changed1(event):
                app.entrada1.delete(0, "end")
                app.entrada1.insert(0, combo1.get())
    
            def changed2(event):
                app.entrada2.delete(0, "end")
                app.entrada2.insert(0, combo2.get())
    
            combo1 = ttk.Combobox(app, values=peliculas, textvariable=valorDefecto1, width=40)
            combo1.bind("<<ComboboxSelected>>", changed1)
            combo1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo1)
    
            combo2 = ttk.Combobox(app, values=funciones, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo2)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada1)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada2)
    
            app.actualizarFormulario("", [], "")

            def aceptarAsignacion():
                peliculaSeleccionada = app.entrada1.get()
                funcionSeleccionada = app.entrada2.get()
        
                pelicula = next(p for p in Pelicula.totalPeliculas if p.getTitulo() == peliculaSeleccionada)
                funcion = next(f for f in Funcion.allFunciones if f"{f.getTipo()},{f.getSala()}" == funcionSeleccionada)
        
                funcion.setPelicula(pelicula)
                app.resultLabel.config(text=f"Película {pelicula.getTitulo()} asignada a la función {funcion.getTipo()} en la sala {funcion.getSala()}")

                combo1.destroy()
                combo2.destroy()
                app.entrada1.destroy()
                app.entrada2.destroy()

            app.frame.setComando(aceptarAsignacion)

        def asignarSalaFuncion(app):
            if not Sala.allSalas or not Funcion.allFunciones:
                app.resultLabel.config(text="No hay salas o funciones disponibles.")
                return

            app.procesoLabel.config(text="Asignar Sala a Función")
            app.indicacionLabel.config(text="Seleccione una sala y una función")
            combo.destroy()
            app.entrada.destroy()
    
            salas = [f"Sala {sala.getNumero()}" for sala in Sala.allSalas]
            funciones = [f"Funcion {funcion.getTipo()}" for funcion in Funcion.allFunciones if funcion.getSala() is None]
    
            valorDefecto1 = tk.StringVar(value="Opciones de salas")
            valorDefecto2 = tk.StringVar(value="Opciones de funciones")
    
            def changed1(event):
                app.entrada1.delete(0, "end")
                app.entrada1.insert(0, combo1.get())
    
            def changed2(event):
                app.entrada2.delete(0, "end")
                app.entrada2.insert(0, combo2.get())
    
            combo1 = ttk.Combobox(app, values=salas, textvariable=valorDefecto1, width=40)
            combo1.bind("<<ComboboxSelected>>", changed1)
            combo1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo1)

            combo2 = ttk.Combobox(app, values=funciones, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(combo2)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada1)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
            app.widgetsSueltos.append(app.entrada2)
    
            app.actualizarFormulario("", [], "")

            def aceptarAsignacion():
                salaSeleccionada = app.entrada1.get()
                funcionSeleccionada = app.entrada2.get()
        
                sala = next(s for s in Sala.allSalas if f"Sala {s.getNumero()}" == salaSeleccionada)
                funcion = next(f for f in Funcion.allFunciones if f.getSala() is None if f"Funcion {f.getTipo()}" == funcionSeleccionada)
        
                funcion.setSala(sala)
                app.resultLabel.config(text=f"Sala {sala.getNumero()} asignada a la función de tipo {funcion.getTipo()} ")

                combo1.destroy()
                combo2.destroy()
                app.entrada1.destroy()
                app.entrada2.destroy()
                
            app.frame.setComando(aceptarAsignacion)

    @staticmethod
    def comprarBoletaJuegos(app):
        Interfaz.limpiarFormulario(app)
        # Paso 1: Identificación del cliente
        criterios = ["Número de identificación"]
        app.actualizarFormulario("Ingrese su número de identificación", criterios, "Cliente seleccionado")

        def identificarCliente():
            idCliente = int(app.frame.getValue("Número de identificación"))
            cliente = Cliente.buscarClientePorId(idCliente)

            if cliente is None:
                opciones = ["Sí", "No"]
                app.actualizarFormulario("Cliente no encontrado. ¿Desea crear uno nuevo?", ["Seleccione una opción"], "Respuesta", opciones)

                def crearCliente():
                    respuesta = app.frame.getValue("Seleccione una opción")
                    if respuesta == "Sí":
                        criteriosCliente = ["Nombre completo", "Saldo inicial"]
                        app.actualizarFormulario("Ingrese los datos del nuevo cliente", criteriosCliente, "Datos cliente")

                        def crearNuevoCliente():
                            nombre = app.frame.getValue("Nombre completo")
                            saldoInicial = float(app.frame.getValue("Saldo inicial"))
                            cliente = Cliente(nombre, saldoInicial, idCliente)
                            app.resultLabel.config(text="Cliente creado exitosamente.")
                            seleccionarCine(cliente)  # Pasamos el cliente a la siguiente función

                        app.frame.setComando(crearNuevoCliente)

                    elif respuesta == "No":
                        app.resultLabel.config(text="Operación cancelada.")
                        return

                app.frame.setComando(crearCliente)
            else:
                seleccionarCine(cliente)  # Pasamos el cliente a la siguiente función

        def seleccionarCine(cliente):
            cines = [f"{cine.getNombre()} {cine.getZonaDeJuegos().getNombre()}" for cine in Cine.cines if cine.getZonaDeJuegos()]
            app.actualizarFormulario("Seleccione el cine", ["Nombre del cine"], "Cine seleccionado", [])
            app.resultLabel.config(text="\n".join(cines))
            def seleccionarZonaDeJuegos():
                cineSeleccionado = app.frame.getValue("Nombre del cine")
                cine = next(c for c in Cine.cines if c.getNombre() == cineSeleccionado)

                # Paso 3: Selección de la máquina en la zona de juegos
                maquinas = cine.getZonaDeJuegos().getMaquinas()
                opcionesMaquinas = [f"{m.getNombre()} - Precio: {m.getPrecioUso()}" for m in maquinas]
                app.actualizarFormulario("Seleccione la máquina", ["Máquina"], "Máquina seleccionada", [])
                app.resultLabel.config(text="\n".join(opcionesMaquinas))
                def comprarBoleta():
                    maquina = app.frame.getValue("Máquina")
                    maquinaSeleccionada = next(
                        m for cine in Cine.cines for m in cine.getZonaDeJuegos().getMaquinas() if m.getNombre() == maquina
                    )

                    # Verificar si la máquina requiere mantenimiento
                    if maquinaSeleccionada.necesitaMantenimiento():
                        messagebox.showwarning(
                            "Mantenimiento",
                            f"La máquina {maquinaSeleccionada.getNombre()} no está disponible debido a mantenimiento."
                        )
                        return

                    # Paso 4: Realizar la compra
                    if cliente.getSaldo() >= maquinaSeleccionada.getPrecioUso():
                        cliente.setSaldo(cliente.getSaldo() - maquinaSeleccionada.getPrecioUso())
                        maquinaSeleccionada.usar()
                        app.resultLabel.config(text="Compra realizada exitosamente.")

                        # Paso 5: Asignar bono si está activo
                        bonoMensaje = maquinaSeleccionada.asignarBono(cliente)
                        app.resultLabel.config(text=f"Compra realizada. {bonoMensaje}")

                        # Paso 6: Imprimir recibo
                        recibo = (
                            f"Recibo:\nCliente: {cliente.getNombre()}\n"
                            f"Máquina: {maquinaSeleccionada.getNombre()}\n"
                            f"Precio: {maquinaSeleccionada.getPrecioUso()}\n"
                            f"Saldo restante: {cliente.getSaldo()}"
                        )
                        app.resultLabel.config(text=recibo)
                    else:
                        app.resultLabel.config(text="Saldo insuficiente.")

                app.frame.setComando(comprarBoleta)

            app.frame.setComando(seleccionarZonaDeJuegos)

        app.frame.setComando(identificarCliente)
   
    @staticmethod
    def calificarPelicula(app):
        Interfaz.limpiarFormulario(app)
        # Obtener todas las películas activas en los cines
        peliculas = []
        for cine in Cine.cines:
            peliculas.extend(cine.peliculasActivas())

        if not peliculas:
            messagebox.showwarning("No hay peliculas activas en este momento")
            return

        def objetosRepetidos(objetos):
            objetosUnicos = []
            for obj in objetos:
                if not any(obj.getTitulo() == unico.getTitulo() for unico in objetosUnicos):
                    objetosUnicos.append(obj)
            return objetosUnicos

        peliculas = objetosRepetidos(peliculas)
    
        # Mostrar lista de películas para seleccionar
        peliculasOpciones = [f"{pelicula.getTitulo()} - Calificación actual: {pelicula.getCalificacionPromedio():.2f}" for pelicula in peliculas]
        app.actualizarFormulario("Seleccione la película que desea calificar", ["Película"], "Película seleccionada", [])
        app.resultLabel.config(text="\n".join(peliculasOpciones))

        def seleccionarPelicula():
            seleccion = app.frame.getValue("Película")
            peliculaSeleccionada = next(pelicula for pelicula in peliculas if f"{pelicula.getTitulo()}" in seleccion)

            # Solicitar calificación
            app.actualizarFormulario(f"Ingrese una calificación para {peliculaSeleccionada.getTitulo()} (1-5)", ["Calificación"], "Calificación seleccionada")
        
            def ingresarCalificacion():
                try:
                    calificacion = float(app.frame.getValue("Calificación"))
                    if calificacion < 1 or calificacion > 5:
                        app.resultLabel.config(text="Calificación inválida. Ingrese un valor entre 1 y 5.")
                        return
                except ValueError:
                    app.resultLabel.config(text="Calificación inválida. Ingrese un número válido.")
                    return
            
                # Actualizar calificación de la película
                peliculaSeleccionada.actualizarCalificacion(calificacion)
            
                # Mostrar confirmación y nueva calificación
                mensaje = (
                    f"Calificación guardada correctamente.\n"
                    f"Nueva calificación promedio de {peliculaSeleccionada.getTitulo()}: {peliculaSeleccionada.getCalificacionPromedio():.2f}"
                )
                app.resultLabel.config(text=mensaje)

            app.frame.setComando(ingresarCalificacion)

        app.frame.setComando(seleccionarPelicula)
    
    @staticmethod
    def comprarBoleta(app):
        Interfaz.limpiarFormulario(app)

        # Paso 1: Solicitar ID del cliente
        app.procesoLabel.config(text="Comprar Boleta - Paso 1")
        app.indicacionLabel.config(text="Ingrese su ID de cliente")
    
        criterios = ["ID de cliente"]
        app.actualizarFormulario("Datos del Cliente", criterios, "Valores", [])
    
        def obtenerCliente():
            cliente_id = int(app.frame.getValue("ID de cliente"))
            cliente = Cliente.buscarClientePorId(cliente_id)
        
            # Si el cliente no existe, ofrecer opción de crearlo
            if cliente is None:
                app.indicacionLabel.config(text="Cliente no encontrado. ¿Desea crear uno?")
                opciones = ["Sí", "No"]
                app.actualizarFormulario("Opciones", ["Crear Cliente"], "Opciones", opciones)
            
                def crearCliente():
                    crear_cliente = app.frame.getValue("Crear Cliente")
                    if crear_cliente == "Sí":
                        # Solicitar nombre y saldo del nuevo cliente
                        criterios_cliente = ["Nombre", "Saldo"]
                        app.indicacionLabel.config(text="Ingrese los datos del nuevo cliente")
                        app.actualizarFormulario("Crear Cliente", criterios_cliente, "Valores", [])
                    
                        def confirmarCliente():
                            nombre = app.frame.getValue("Nombre")
                            saldo = float(app.frame.getValue("Saldo"))
                            nuevo_cliente = Cliente(nombre, saldo, cliente_id)
                            app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nCliente {nombre} creado con éxito.")
                            continuarCompra(nuevo_cliente)
                    
                        app.frame.setComando(confirmarCliente)
                    else:
                        app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo se realizó la compra.")
                        return
            
                app.frame.setComando(crearCliente)
            else:
                continuarCompra(cliente)

        app.frame.setComando(obtenerCliente)
    
        def continuarCompra(cliente):
            # Paso 2: Seleccionar cine
            cinesDisponibles = [cine.getNombre() for cine in Cine.cines]
            app.procesoLabel.config(text="Comprar Boleta - Paso 2")
            app.indicacionLabel.config(text="Seleccione el cine")
            app.actualizarFormulario("Cine", ["Seleccione Cine"], "Opciones", [])
            app.resultLabel.config(text="\n".join(cinesDisponibles))

            def seleccionarCine():
                cine_seleccionado_nombre = app.frame.getValue("Seleccione Cine")
                cine_seleccionado = next(cine for cine in Cine.cines if cine.getNombre() == cine_seleccionado_nombre)
            
                # Paso 3: Seleccionar función
                dias_semana = ['Lunes', 'Martes', 'Jueves', 'Viernes', 'Sábado']
                funciones_por_dia = {
                    'Lunes': cine_seleccionado.getLunes(),
                    'Martes': cine_seleccionado.getMartes(),
                    'Jueves': cine_seleccionado.getJueves(),
                    'Viernes': cine_seleccionado.getViernes(),
                    'Sábado': cine_seleccionado.getSabado(),
                }

                funcionesDisponibles = []
                funcion_map = {}
                contador = 1
                for dia in dias_semana:
                    funciones_dia = funciones_por_dia[dia]
                    for funcion in funciones_dia:
                        if funcion:
                            pelicula = funcion.getPelicula().getTitulo()
                            funcionesDisponibles.append(f"{contador}. {dia}: {pelicula}")
                            funcion_map[contador] = funcion
                            contador += 1

                app.procesoLabel.config(text="Comprar Boleta - Paso 3")
                app.indicacionLabel.config(text="Seleccione la función")
                app.actualizarFormulario("Funcion", ["Seleccione Función"], "Opciones", [])
                app.resultLabel.config(text="\n".join(funcionesDisponibles))

                def seleccionarFuncion():
                    funcionSeleccionadaIndex = app.frame.getValue("Seleccione Función")
                    funcionSeleccionada = funcion_map[int(funcionSeleccionadaIndex.split()[0])]

                    app.resultLabel.config(text=funcionSeleccionada.getSala().estadoSilleteria())
                
                    # Paso 4: Seleccionar asiento
                    app.procesoLabel.config(text="Comprar Boleta - Paso 4")
                    app.indicacionLabel.config(text="Seleccione la fila y columna")
                    app.actualizarFormulario("Asiento", ["Fila", "Columna"], "Valores", [])
                
                    def seleccionarAsiento():
                        fila = int(app.frame.getValue("Fila")) - 1
                        columna = int(app.frame.getValue("Columna")) - 1
                    
                        if funcionSeleccionada.getSala().estaDisponible(fila, columna):
                            funcionSeleccionada.getSala().reservarSilla(fila, columna)
                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nAsiento reservado con éxito.")
                            mostrarRecibo(cliente, cine_seleccionado, funcionSeleccionada, fila, columna)
                        else:
                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nEl asiento seleccionado no está disponible.")
                            return
                
                    app.frame.setComando(seleccionarAsiento)
            
                app.frame.setComando(seleccionarFuncion)
        
            app.frame.setComando(seleccionarCine)
    
        def mostrarRecibo(cliente, cine, funcion, fila, columna):
            # Mostrar el recibo final
            precio = funcion.getPrecio()
            if cliente.getTipo() == "Preferencial":
                precio *= 0.9
            elif cliente.getTipo() == "VIP":
                precio *= 0.8
        
            recibo = f"\n--- Recibo de compra ---\nCliente: {cliente.getNombre()} ({cliente.getIdentificacion()})\n" \
                    f"Cine: {cine.getNombre()}\nPelícula: {funcion.getPelicula().getTitulo()}\nSala: {funcion.getSala().getNumero()}\n" \
                    f"Asiento: Fila {fila + 1}, Columna {columna + 1}\nHora de la función: {funcion.getHoraInicio()}\n" \
                    f"Precio total: ${precio:.2f}\n------------------------"
            app.resultLabel.config(text=app.resultLabel.cget("text") + recibo)

        
    @staticmethod
    def limpiarFormulario(app):
        # Destruir los widgets del app.frame si los hay
        if app.frame is not None and app.frame.winfo_children():
            for widget in app.frame.winfo_children():
                widget.destroy()
    
        # Destruir los widgets sueltos (Combobox y Entry fuera del frame)
        if app.widgetsSueltos:
            for widget in app.widgetsSueltos:
                widget.destroy()
            app.widgetsSueltos.clear()  # Limpiar la lista después de destruir los widgets
        
        if hasattr(app, 'imagenLabel') and app.imagenLabel is not None:
            app.imagenLabel.destroy()
            app.imagenLabel = None

        # Limpiar etiquetas de resultado y proceso
        if app.resultLabel is not None:
            app.resultLabel.config(text="")
        if app.procesoLabel is not None:
            app.procesoLabel.config(text="")
        if app.indicacionLabel is not None:
            app.indicacionLabel.config(text="")
        

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


        

