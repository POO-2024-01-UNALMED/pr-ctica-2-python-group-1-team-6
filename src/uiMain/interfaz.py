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
    def gestionarZonaDeJuegos(app):
        """Gestiona las zonas de juegos utilizando la interfaz gráfica."""
    
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

                                            app.botonAceptar.config(command=confirmarNuevoPrecio)

                                        app.botonAceptar.config(command=seleccionarMaquinaRebaja)
                                    app.botonAceptar.config(command=seleccionarZonaRebaja)

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

                                        app.frame.funAceptar(seleccionarMaquinaBono)

                                    app.frame.funAceptar(seleccionarZonaBono)

                            app.frame.funAceptar(seleccionarTipoIncentivo)

                        else:
                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo se aplicarán incentivos.")
        
                    app.frame.funAceptar(seleccionarIncentivo)
                app.frame.funAceptar(seleccionarZonaDestino)
            app.frame.funAceptar(seleccionarMaquina)
        app.frame.funAceptar(seleccionarZona)

    @staticmethod
    def gestionarPeliculas(app):
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
                                
                                    app.frame.funAceptar(aplicarPrecio)

                                elif incentivoSeleccionado == "Aplicar bono":
                                    peliculaIntercambio.activarBono()
                                    app.resultLabel.config(text=f"Bono activado para {peliculaIntercambio.getTitulo()}")
                        
                        app.frame.funAceptar(aplicarIncentivo)

                    app.frame.funAceptar(seleccionarPeliculaDestino)
                app.frame.funAceptar(seleccionarNuevoCine)
            app.frame.funAceptar(seleccionarPelicula)
        app.frame.funAceptar(seleccionarCine)
    
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
    
    def menuCreacion(app):
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
    
        # Crea el campo de entrada para mostrar la opción seleccionada (si es necesario)
        app.entrada = tk.Entry(app)  # Define app.entrada para que esté accesible en el ámbito de la clase
        app.entrada.pack(side="top", anchor="center", pady=5)
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
        app.frame.funAceptar(aceptarOpcion)  # Vincula la función aceptarOpcion con el botón 'Aceptar'
    
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

            app.frame.funAceptar(aceptarZona)  # Vincula aceptarZona con el botón 'Aceptar' para la creación de la zona
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

            app.frame.funAceptar(aceptarMaquina)  # Vincula aceptarMaquina con el botón 'Aceptar' para la creación de la maquina
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

            app.frame.funAceptar(aceptarPelicula)  # Vincula aceptarPelicula con el botón 'Aceptar' para la creación de la pelicual
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

            app.frame.funAceptar(aceptarFuncion)  # Vincula aceptarFuncion con el botón 'Aceptar' para la creación de la funcion
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

            app.frame.funAceptar(aceptarCliente)  # Vincula aceptarCliente con el botón 'Aceptar' para la creación del cliente
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

            app.frame.funAceptar(aceptarCine)  # Vincula aceptarCine con el botón 'Aceptar' para la creación del cine
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

            app.frame.funAceptar(aceptarSala)  # Vincula aceptarSala con el botón 'Aceptar' para la creación de la sala
    
    def menuAsignacion(app):
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

        app.entrada = tk.Entry(app,width=40)
        app.entrada.pack(side="top", anchor="center", pady=5)
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

        app.frame.funAceptar(aceptarOpcion)

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
            combo2 = ttk.Combobox(app, values=cines, textvariable=valorDefecto2,width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
            app.entrada1 = tk.Entry(app,width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
            app.entrada2 = tk.Entry(app,width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
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
            app.frame.funAceptar(aceptarAsignacion)

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
    
            combo2 = ttk.Combobox(app, values=cines, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)

            combo3 = ttk.Combobox(app, values=dias, textvariable=valorDefecto3, width=40)
            combo3.bind("<<ComboboxSelected>>", changed3)
            combo3.pack(side="top", anchor="center", pady=5)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)

            app.entrada3 = tk.Entry(app, width=40)
            app.entrada3.pack(side="top", anchor="center", pady=5)
    
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

            app.frame.funAceptar(aceptarAsignacion)


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
    
            combo2 = ttk.Combobox(app, values=zonas, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
    
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
    
            app.frame.funAceptar(aceptarAsignacion)

        

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
    
            combo2 = ttk.Combobox(app, values=funciones, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
    
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

            app.frame.funAceptar(aceptarAsignacion)

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
    
            combo2 = ttk.Combobox(app, values=funciones, textvariable=valorDefecto2, width=40)
            combo2.bind("<<ComboboxSelected>>", changed2)
            combo2.pack(side="top", anchor="center", pady=5)
    
            app.entrada1 = tk.Entry(app, width=40)
            app.entrada1.pack(side="top", anchor="center", pady=5)
    
            app.entrada2 = tk.Entry(app, width=40)
            app.entrada2.pack(side="top", anchor="center", pady=5)
    
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
                
            app.frame.funAceptar(aceptarAsignacion)

    @staticmethod
    def comprarBoletaJuegos(app):
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

                        app.frame.funAceptar(crearNuevoCliente)

                    elif respuesta == "No":
                        app.resultLabel.config(text="Operación cancelada.")
                        return

                app.frame.funAceptar(crearCliente)
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

                app.frame.funAceptar(comprarBoleta)

            app.frame.funAceptar(seleccionarZonaDeJuegos)

        app.frame.funAceptar(identificarCliente)
   
    @staticmethod
    def calificarPelicula(app):
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

            app.frame.funAceptar(ingresarCalificacion)

        app.frame.funAceptar(seleccionarPelicula)

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


        

