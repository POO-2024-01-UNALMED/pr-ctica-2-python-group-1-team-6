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
from src.uiMain.excepciones import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




from datetime import time,datetime
#Aqui estan todos los metodos que le dan una funcionalidad al sistema
class Interfaz:

    
    #Gestionar Zona de juegos
    @staticmethod
    def gestionarZonaDeJuegos(app):
        
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
        opcionesZonas = [cine.zonaDeJuegos.getNombre() for cine in zonasDisponibles]

        app.procesoLabel.config(text="Seleccionar Zona de Juegos")
        app.indicacionLabel.config(text="Seleccione la zona donde desea reparar una máquina")
        app.actualizarFormulario("Zonas Disponibles", criterios, "Valores", [])

        # Botón 'Aceptar' pasa a seleccionar la máquina dañada
        def seleccionarZona():
            zonaNombre = app.frame.getValue("Ingrese la zona de juegos para reparación")
        
            # Buscar la zona seleccionada por su nombre
            try:
                zonaActual = None
                for cine in zonasDisponibles:
                    if cine.zonaDeJuegos.getNombre() == zonaNombre:
                        zonaActual = cine.zonaDeJuegos
                        break

                # Si no se encuentra una zona válida, lanzamos la excepción personalizada
                if zonaActual is None:
                    datosValidos = [cine.zonaDeJuegos.getNombre() for cine in zonasDisponibles]  # Lista de nombres válidos
                    raise DatoErroneoExcepcion(datosValidos, zonaNombre)

            except DatoErroneoExcepcion as e:
                # Manejo del error con un pop-up para informar al usuario
                messagebox.showerror("Error",f"{str(e)}.\nZonas válidas: {', '.join(e.datosValidos)}")
                return

            maquinasDañadas = zonaActual.getMaquinasDañadas()
        
            if not maquinasDañadas:
                app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo hay máquinas dañadas en la zona seleccionada.")
                return

            # Paso 3: Selección de la máquina dañada
            criteriosMaquinas = ["Ingrese la máquina dañada"]
            opcionesMaquinas = [maquina.getNombre() for maquina in maquinasDañadas]
            app.procesoLabel.config(text="Seleccionar Máquina a Reparar")
            app.indicacionLabel.config(text="Seleccione la máquina que desea reparar")
            app.actualizarFormulario("Máquinas Dañadas", criteriosMaquinas, "Valores", [])

            # Botón 'Aceptar' para realizar la reparación
            def seleccionarMaquina():
                maquina_nombre = app.frame.getValue("Ingrese la máquina dañada")
            
                try: # Buscar la máquina seleccionada por su nombre
                    maquinaSeleccionada = None
                    for maquina in maquinasDañadas:
                        if maquina.getNombre() == maquina_nombre:
                            maquinaSeleccionada = maquina
                            break
            
                    if maquinaSeleccionada is None:
                        datosValidos = opcionesMaquinas  # Opcional: Lista de nombres válidos
                        raise DatoErroneoExcepcion(datosValidos, maquina_nombre)

                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error",f"{str(e)}.\nMaquinas validas:{', '.join(e.datosValidos)}")
                    return
                        
                #Reparacion
                resultadoReparacion = Bodega.allBodegas[0].realizarMantenimiento(zonaActual, maquinasDañadas.index(maquinaSeleccionada))
                app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nReparación realizada: {resultadoReparacion}")

                # Recomendación de movimiento
                recomendacion = zonaActual.recomendarMovimiento(maquinaSeleccionada)
                app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nRecomendación: {recomendacion}")

                criterios=["Ingrese la zona de destino"]
                app.procesoLabel.config(text="Seleccionar Zona de Destino")
                app.indicacionLabel.config(text="Seleccione la zona donde desea mover la máquina")
                app.actualizarFormulario("Zonas Disponibles", criterios, "Valores", [])

                # Botón 'Aceptar' para mover la máquina
                def seleccionarZonaDestino():
                    zonaDestinoNombre = app.frame.getValue("Ingrese la zona de destino")
                    print(zonaDestinoNombre)
                    # Buscar la zona de destino por su nombre
                    try:
                        zonaDestino = None
                        for cine in zonasDisponibles:
                            if cine.zonaDeJuegos.getNombre() == zonaDestinoNombre:
                                zonaDestino = cine.zonaDeJuegos
                                break
                
                        if zonaDestino is None:
                            datosValidos=opcionesZonas
                            raise DatoErroneoExcepcion(datosValidos,zonaDestinoNombre)
                    except DatoErroneoExcepcion as e:
                        messagebox.showerror("Error",f"{str(e)}.\n Zonas validas: {', '.join(e.datosValidos)}")
                        return

                    if zonaActual != zonaDestino:
                        resultadoMovimiento = zonaActual.moverMaquina(zonaDestino, maquinasDañadas.index(maquinaSeleccionada))
                        app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nMovimiento realizado: {resultadoMovimiento}")
                    else:
                        app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nLa máquina permanecerá en {zonaActual.getNombre()}")
                    # Paso 4: Aplicar incentivos
                    aplicarIncentivo()

                def aplicarIncentivo():
                    # Preguntar al usuario si desea aplicar incentivos
                    criteriosIncentivo = ["¿Desea aplicar algún incentivo en una zona de juegos? Si/No"]
                    opcionesIncentivo = ["Si", "No"]

                    app.procesoLabel.config(text="Aplicar Incentivos")
                    app.indicacionLabel.config(text="Seleccione si desea aplicar un incentivo")
                    app.actualizarFormulario("Aplicar Incentivo", criteriosIncentivo, "Opciones", opcionesIncentivo)

                    def seleccionarIncentivo():
                        opcionIncentivo = app.frame.getValue("¿Desea aplicar algún incentivo en una zona de juegos? Si/No")
                    
                        if opcionIncentivo == "Si":
                            criteriosTipoIncentivo = ["Seleccione el tipo de incentivo"]
                            app.procesoLabel.config(text="Tipo de Incentivo")
                            app.indicacionLabel.config(text="Seleccione el tipo de incentivo")
                            app.actualizarFormulario("Tipo de Incentivo", criteriosTipoIncentivo, "Opciones", [])

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
                                    app.actualizarFormulario("Zonas para Rebaja", ["Seleccione una zona"], "Opciones", [])

                                    def seleccionarZonaRebaja():
                                        zonaRebajaNombre = app.frame.getValue("Seleccione una zona")

                                        try:
                                            zonaRebaja = None
                                            for cine in zonasDisponibles:
                                                if cine.zonaDeJuegos.getNombre() == zonaRebajaNombre:
                                                    zonaRebaja = cine.zonaDeJuegos
                                                    break

                                            if zonaRebaja is None:
                                                raise DatoErroneoExcepcion(opcionesZonas,zonaRebajaNombre)
                                        except DatoErroneoExcepcion as e:
                                            messagebox.showerror("Error",f"{str(e)}.\nZonas validas: {', '.join(e.datosValidos)}")
                                            return 


                                        # Seleccionar la máquina para rebajar el precio
                                        maquinasEnZona = zonaRebaja.getMaquinas()
                                        opcionesMaquinasRebaja = [maquina.getNombre() for maquina in maquinasEnZona]
                                        app.actualizarFormulario("Máquinas para Rebaja", ["Seleccione una máquina"], "Opciones", [])

                                        def seleccionarMaquinaRebaja():
                                            maquinaRebajaNombre = app.frame.getValue("Seleccione una máquina")
                                            try:
                                                maquinaRebajada = None
                                                for maquina in maquinasEnZona:
                                                    if maquina.getNombre() == maquinaRebajaNombre:
                                                        maquinaRebajada = maquina
                                                    break

                                                # Si la máquina no es válida, lanzamos la excepción DatoErroneoExcepcion
                                                if maquinaRebajada is None:
                                                    raise DatoErroneoExcepcion(opcionesMaquinasRebaja, maquinaRebajaNombre)

                                            except DatoErroneoExcepcion as e:
                                                messagebox.showerror("Error",f"{str(e)}.\nMáquinas válidas: {', '.join(e.datosValidos)}")
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
                                    app.actualizarFormulario("Zonas para Bono", ["Seleccione una zona"], "Opciones", opcionesZonas)

                                    def seleccionarZonaBono():
                                        zonaBonoNombre = app.frame.getValue("Seleccione una zona")
                                        try:
                                            zona = None
                                            for cine in zonasDisponibles:
                                                if cine.zonaDeJuegos.getNombre() == zonaBonoNombre:
                                                    zona = cine.zonaDeJuegos
                                                    break

                                    # Si la zona no es válida, lanzamos la excepción DatoErroneoExcepcion
                                            if zona is None:
                                                raise DatoErroneoExcepcion(opcionesZonas, zonaBonoNombre)

                                        except DatoErroneoExcepcion as e:
                                            messagebox.showerror("Error",f"{str(e)}.\nZonas válidas: {', '.join(e.datosValidos)}")
                                            return

                                        # Seleccionar la máquina para aplicar el bono
                                        maquinasEnZona = zona.getMaquinas()
                                        opcionesMaquinasBono = [maquina.getNombre() for maquina in maquinasEnZona]
                                        app.actualizarFormulario("Máquinas para Bono", ["Seleccione una máquina"], "Opciones", opcionesMaquinasBono)

                                        def seleccionarMaquinaBono():
                                            maquina_bono_nombre = app.frame.getValue("Seleccione una máquina")
                                            
                                            try:
                                                maquina = None
                                                for maquina in maquinasEnZona:
                                                    if maquina.getNombre() == maquina_bono_nombre:
                                                        maquina = maquina
                                                        break

                                                #Si la máquina no es válida, lanzamos la excepción DatoErroneoExcepcion
                                                if maquina is None:
                                                    raise DatoErroneoExcepcion(opcionesMaquinasBono, maquina_bono_nombre)

                                            except DatoErroneoExcepcion as e:
                                                messagebox.showerror("Error",f"{str(e)}.\nMáquinas válidas: {', '.join(e.datosValidos)}")
                                                return
                                            # Activar el bono en la máquina seleccionada
                                            maquina.activarBono()
                                            app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nEl bono ha sido activado para {maquina.getNombre()}")

                                        app.frame.setComando(seleccionarMaquinaBono)

                                    app.frame.setComando(seleccionarZonaBono)
                                else:
                                     messagebox.showerror("Error","Dato invalido")
                                     return
                            app.frame.setComando(seleccionarTipoIncentivo)

                        elif opcionIncentivo=="No":
                            app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo se aplicarán incentivos.")
                        else:
                            messagebox.showerror("Error","Dato invalido")
                            return
        
                    app.frame.setComando(seleccionarIncentivo)
                app.frame.setComando(seleccionarZonaDestino)
            app.frame.setComando(seleccionarMaquina)
        app.frame.setComando(seleccionarZona)
    #Gestionar Peliculas
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
            try:
                cineOrigen = None
                # Buscar si el cine existe en la lista de cines
                cineOrigen = next((cine for cine in Cine.cines if cine.getNombre() == cineSeleccionado), None)
    
                # Si no se encuentra el cine, lanza la excepción
                if cineOrigen is None:
                    nombresCines = [cine.getNombre() for cine in Cine.cines]
                    raise DatoErroneoExcepcion(nombresCines, cineSeleccionado)

            except DatoErroneoExcepcion as e:
                messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                return  # Asegurarse de que el código se detenga aquí

            # Paso 3: Selección de película
            peliculas=["Ingrese el titulo de la pelicula"]
            app.actualizarFormulario("Seleccione la película", peliculas, "Película seleccionada")

            def seleccionarPelicula():
                peliculaSeleccionada = app.frame.getValue("Ingrese el titulo de la pelicula")
                
                try:
                    peliculaAIntercambiar=None
                    peliculaAIntercambiar = next((pelicula for pelicula in cineOrigen.peliculasActivas() if pelicula.getTitulo() == peliculaSeleccionada),None)

                    if peliculaAIntercambiar is None:
                        nombresPeliculas= [pelicula.getTitulo() for pelicula in cineOrigen.peliculasActivas()]
                        raise DatoErroneoExcepcion(nombresPeliculas, peliculaSeleccionada)
                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                    return  # Asegurarse de que el código se detenga aquí
                # Paso 4: Recomendar una película para intercambio
                recomendacion = Pelicula.recomendarIntercambio(peliculaAIntercambiar)
                app.resultLabel.config(text=f"Recomendación: {recomendacion}")
                
                # Selección de nuevo cine para el intercambio
                criterios = ["Ingrese el nombre del cine de la pelicula a intercambiar"]
                app.actualizarFormulario("Seleccione el nuevo cine", criterios, "Cine destino")
                
                def seleccionarNuevoCine():
                    nuevoCineSeleccionado = app.frame.getValue("Ingrese el nombre del cine de la pelicula a intercambiar")
                    try:
                        nuevoCine = None
                        # Buscar si el cine existe en la lista de cines
                        nuevoCine = next((cine for cine in Cine.cines if cine.getNombre() == nuevoCineSeleccionado),None)
    
                        # Si no se encuentra el cine, lanza la excepción
                        if nuevoCine is None:
                            nombresCines = [cine.getNombre() for cine in Cine.cines]
                            raise DatoErroneoExcepcion(nombresCines, nuevoCineSeleccionado)

                    except DatoErroneoExcepcion as e:
                        messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                        return  # Asegurarse de que el código se detenga aquí
                    
                    
                    # Paso 5: Selección de película en el nuevo cine
                    peliculasNuevoCine = ["Ingrese el titulo de la pelicula intercambio"]
                    app.actualizarFormulario("Seleccione la película en el nuevo cine", peliculasNuevoCine, "Película destino")
                    
                    def seleccionarPeliculaDestino():
                        peliculaIntercambioSeleccionada = app.frame.getValue("Ingrese el titulo de la pelicula intercambio")
                        try:
                            peliculaIntercambio=None
                            peliculaIntercambio = next((pelicula for pelicula in nuevoCine.peliculasActivas() if pelicula.getTitulo() == peliculaIntercambioSeleccionada),None)

                            if peliculaIntercambio is None:
                                nombresPeliculas= [pelicula.getTitulo() for pelicula in nuevoCine.peliculasActivas()]
                                raise DatoErroneoExcepcion(nombresPeliculas, peliculaIntercambioSeleccionada)
                        except DatoErroneoExcepcion as e:
                            messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                            return  # Asegurarse de que el código se detenga aquí
                        
                        

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
                                    criterios = ["Ingrese el titulo de la pelicula perteneciente a la funcion","Ingrese su numero de sala","Ingrese el nuevo precio"]
                                    app.actualizarFormulario("Seleccione la función",criterios, "Función seleccionada")
                                
                                    def aplicarPrecio():
                                        titulo = app.frame.getValue("Ingrese el titulo de la pelicula perteneciente a la funcion")
                                        numSala = app.frame.getValue("Ingrese su numero de sala")
                                        try:
                                            # Obtener el título de la película y el número de sala ingresados por el usuaario
                                
                                            # Buscar la función correspondiente
                                            funcion = None
                                            for cine in Cine.cines:
                                                for f in cine.totalFunciones():
                                                    if f.getPelicula().getTitulo() == titulo and f.getSala().getNumero() == int(numSala):
                                                        funcion = f
                                                        break
        
                                            if funcion is None:
                                                raise DatoErroneoExcepcion("Datos inexistentes", "título o número de sala")
                                            
                                        except DatoErroneoExcepcion as e:
                                            messagebox.showerror("Error",f"{str(e)} {e.mensaje}")  # Mostrar el mensaje personalizado de error
                                            return
                                        try:
                                            nuevoPrecio = app.frame.getValue("Ingrese el nuevo precio")
                                            

                                            if not nuevoPrecio.isdigit():
                                                raise ExcepcionSugerida2(nuevoPrecio)
                                            nuevoPrecio=int(nuevoPrecio)
        
                                            # Aplicar el nuevo precio
                                            funcion.setPrecio(nuevoPrecio)
                                            app.resultLabel.config(text=f"Nuevo precio: {nuevoPrecio}")
                                        except ExcepcionSugerida2 as s:
                                            messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                                            return
                                
                                    app.frame.setComando(aplicarPrecio)
                                elif incentivoSeleccionado == "Aplicar bono":
                                    peliculaIntercambio.activarBono()
                                    app.resultLabel.config(text=f"Bono activado para {peliculaIntercambio.getTitulo()}")
                                else:
                                    messagebox.showerror("Error","Opcion no valida")
                                    return
                        
                            app.frame.setComando(aplicarIncentivo)

                    app.frame.setComando(seleccionarPeliculaDestino)
                app.frame.setComando(seleccionarNuevoCine)
            app.frame.setComando(seleccionarPelicula)
        app.frame.setComando(seleccionarCine)
    #Menu para crear instancias en ejecucion
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
                materiales = app.frame.getValue("Materiales necesarios para la maquina")
                precio = app.frame.getValue("Precio de la maquina")
                try:
                    # Validar el género
                    if tipo not in ["Arcade", "Dance Dance","Mesa de discos","Boxing","Basket"]:
                        raise DatoErroneoExcepcion(["Arcade", "Dance Dance","Mesa de discos","Boxing","Basket"],"tipo")
                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error de tipoo", f"{str(e)} {e.mensaje}")
                    return
                try:
                    if not materiales.isdigit():
                        raise ExcepcionSugerida2(materiales)
                    materiales=int(materiales)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
                try:
                    if not precio.isdigit():
                        raise ExcepcionSugerida2(precio)
                    precio=int(precio)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
                maquina=Maquina(nombreMaquina,tipo,materiales,precio)
                app.resultLabel.config(text=f"Maquina creada: {maquina}")

            app.frame.setComando(aceptarMaquina)  # Vincula aceptarMaquina con el botón 'Aceptar' para la creación de la maquina
        def crearPelicula(app):
            criterios = ["Titulo de la pelicula", "Genero","Duracion (en horas y minutos, formato HH:MM)"]
            app.procesoLabel.config(text="Crear Pelicula")
            app.indicacionLabel.config(text="Ingrese las especificaciones de la pelicula")
            combo.destroy()
            app.entrada.destroy()
            app.actualizarFormulario("Datos Pelicula", criterios, "Valores", [])

            # Función que se ejecuta al presionar el botón 'Aceptar' para la creación de la pelicula
            def aceptarPelicula():
                titulo = app.frame.getValue("Titulo de la pelicula")
                genero = app.frame.getValue("Genero")
                duracionStr = app.frame.getValue("Duracion (en horas y minutos, formato HH:MM)")
                
                try:
                    # Validar el género
                    if genero not in ["Acción", "Drama","+18","Infantil","Terror"]:
                        raise DatoErroneoExcepcion(["Acción", "Drama","+18","Infantil","Terror"],"genero")
                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error de género", f"{str(e)} {e.mensaje}")
                    return

                    # Validar el formato de duración
                try:
                    # Validar si la entrada de duración no es vacía o None
                    if not duracionStr:
                        raise DatoErroneoExcepcion("formato HH:MM", "Duracion (en horas y minutos, formato HH:MM)")

                    # Intentar convertir la cadena a tiempo
                    try:
                        duracion = datetime.strptime(duracionStr, "%H:%M").time()
                    except ValueError:
                        raise DatoErroneoExcepcion("formato HH:MM", duracionStr)

                except DatoErroneoExcepcion as a:
                    messagebox.showerror("Error de duración", f"Error: {str(a)} {a.mensaje}")
                    return
                
                pelicula = Pelicula(titulo, genero, duracion)
                app.resultLabel.config(text=f"Película creada: {pelicula}")

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
                try:
                    # Validar el género
                    if tipoFuncion not in ["Normal","VIP"]:
                        raise DatoErroneoExcepcion(["Normal","VIP"],"funcion")
                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error de funcion", f"{str(e)} {e.mensaje}")
                    return
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
                saldo = app.frame.getValue("Saldo")
                id = app.frame.getValue("ID")
                try:
                    if not saldo.isdigit():
                        raise ExcepcionSugerida2(saldo)
                    saldo=int(saldo)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
                try:
                    if not id.isdigit():
                        raise ExcepcionSugerida2(id)
                    id=int(id)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
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
                numero = app.frame.getValue("Numero de la sala")
                filas = app.frame.getValue("numero de filas")
                columnas = app.frame.getValue("numero de columnas")
                try:
                    if not numero.isdigit():
                        raise ExcepcionSugerida2(numero)
                    numero=int(numero)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
                try:
                    if not filas.isdigit():
                        raise ExcepcionSugerida2(filas)
                    filas=int(filas)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
                try:
                    if not columnas.isdigit():
                        raise ExcepcionSugerida2(columnas)
                    columnas=int(columnas)
                except ExcepcionSugerida2 as s:
                    messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                    return
                sala=Sala(numero,filas,columnas)
                app.resultLabel.config(text=f"Sala creada: {sala}")

            app.frame.setComando(aceptarSala)  # Vincula aceptarSala con el botón 'Aceptar' para la creación de la sala
    #Menu para asignar instancias creadas en ejecucuion
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
    
            try:
                funciones = []
                for funcion in Funcion.allFunciones:
                    if funcion.getPelicula() is None or funcion.getSala() is None:
                        raise AtributoNoneExcepcion()
                    funciones.append(f"{funcion.getPelicula().getTitulo()},{funcion.getTipo()},{funcion.getSala()}")
            except AtributoNoneExcepcion as e:
                messagebox.showerror("Error", e.mensaje())
                return
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
        
                try:
                    for f in Funcion.allFunciones:
                        if f.getPelicula() is None or f.getSala() is None:
                            raise AtributoNoneExcepcion()
                        if f"{f.getPelicula().getTitulo()},{f.getTipo()},{f.getSala()}" == funcionSeleccionada:
                            funcion = f
                            break
                except AtributoNoneExcepcion as e:
                    messagebox.showerror("Error", e.mensaje())
                    return

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
                
                maquinaAsignada = False

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
            try:
                funciones = []
                for funcion in Funcion.allFunciones:
                    if funcion.getPelicula() is None:
                        if funcion.getSala() is None:
                            raise AtributoNoneExcepcion()  # Lanza la excepción si la película es None
                        funciones.append(f"{funcion.getTipo()},{funcion.getSala()}")
            except AtributoNoneExcepcion as e:
                messagebox.showerror("Error", e.mensaje())
                return
    
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
                funcion=None
                try:
                    for f in Funcion.allFunciones:
                        if f.getSala() is None:
                            raise AtributoNoneExcepcion()
                        if f"{f.getTipo()},{f.getSala()}" == funcionSeleccionada:
                            funcion = f
                            break
                except AtributoNoneExcepcion as e:
                    messagebox.showerror("Error", e.mensaje())
                    return

        
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
    #Comprar boleta para jugar maquinitas
    @staticmethod
    def comprarBoletaJuegos(app):
        Interfaz.limpiarFormulario(app)
        # Paso 1: Identificación del cliente
        criterios = ["Número de identificación"]
        app.actualizarFormulario("Ingrese su número de identificación", criterios, "Cliente seleccionado")

        def identificarCliente():
            idCliente = app.frame.getValue("Número de identificación")
            try:
                if not idCliente.isdigit():
                    raise ExcepcionSugerida2(idCliente)
                idCliente=int(idCliente)
            except ExcepcionSugerida2 as s:
                messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                return
            cliente = Cliente.buscarClientePorId(idCliente)

            if cliente is None:
                app.actualizarFormulario("Cliente no encontrado. ¿Desea crear uno nuevo?", ["Si o No"], "Respuesta")

                def crearCliente():
                    respuesta = app.frame.getValue("Si o No")
                    if respuesta == "Si":
                        criteriosCliente = ["Nombre completo", "Saldo inicial","ID"]
                        valores = ["", "", str(idCliente)]
                        habilitado = [True, True, False]
                        app.actualizarFormulario("Ingrese los datos del nuevo cliente", criteriosCliente, "Datos cliente",valores,habilitado)

                        def crearNuevoCliente():
                            nombre = app.frame.getValue("Nombre completo")
                            saldoInicial = app.frame.getValue("Saldo inicial")
                            id=int(app.frame.getValue("ID"))
                            try:
                                if not saldoInicial.isdigit():
                                    raise ExcepcionSugerida2(saldoInicial)
                                saldoInicial=int(saldoInicial)
                            except ExcepcionSugerida2 as s:
                                messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                                return
                            cliente = Cliente(nombre, saldoInicial, id)
                            app.resultLabel.config(text="Cliente creado exitosamente.")
                            seleccionarCine(cliente)  # Pasamos el cliente a la siguiente función

                        app.frame.setComando(crearNuevoCliente)

                    elif respuesta == "No":
                        app.resultLabel.config(text="Operación cancelada.")
                        return
                    else:
                        messagebox.showerror("Error","Respuesta invalida")
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
                try:
                    cine = None
                    # Buscar si el cine existe en la lista de cines
                    cine = next((c for c in Cine.cines if c.getNombre() == cineSeleccionado),None)
    
                    # Si no se encuentra el cine, lanza la excepción
                    if cine is None:
                        nombresCines = [c.getNombre() for c in Cine.cines]
                        raise DatoErroneoExcepcion(nombresCines, cineSeleccionado)

                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                    return  # Asegurarse de que el código se detenga aquí

                # Paso 3: Selección de la máquina en la zona de juegos
                maquinas = cine.getZonaDeJuegos().getMaquinas()
                opcionesMaquinas = [f"{m.getNombre()} - Precio: {m.getPrecioUso()}" for m in maquinas]
                app.actualizarFormulario("Seleccione la máquina", ["Máquina"], "Máquina seleccionada", [])
                app.resultLabel.config(text="\n".join(opcionesMaquinas))
                def comprarBoleta():
                    maquina = app.frame.getValue("Máquina")
                    try:
                        maquinaSeleccionada = None
                        # Buscar si el cine existe en la lista de cines
                        maquinaSeleccionada = next((m for m in maquinas if m.getNombre() == maquina),None)
    
                        # Si no se encuentra el cine, lanza la excepción
                        if maquinaSeleccionada is None:
                            nombresMaquinas = [m.getNombre() for m in maquinas]
                            raise DatoErroneoExcepcion(nombresMaquinas, maquina)

                    except DatoErroneoExcepcion as e:
                        messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                        return  # Asegurarse de que el código se detenga aquí
                    # Verificar si la máquina requiere mantenimiento
                    if maquinaSeleccionada.necesitaMantenimiento():
                        messagebox.showwarning(
                            "Mantenimiento",
                            f"La máquina {maquinaSeleccionada.getNombre()} no está disponible debido a mantenimiento."
                        )
                        return
                    
                    try:
                        # Paso 4: Realizar la compra
                        if cliente.getSaldo() >= maquinaSeleccionada.getPrecioUso():
                            cliente.setSaldo(cliente.getSaldo() - maquinaSeleccionada.getPrecioUso())
                            maquinaSeleccionada.usar()
                            app.resultLabel.config(text="Compra realizada exitosamente.")

                            # Paso 5: Asignar bono si está activo
                            bonoMensaje = maquinaSeleccionada.asignarBono(cliente)
                            

                            # Paso 6: Imprimir recibo
                            recibo = (
                                f"Compra realizada. {bonoMensaje}"
                                f"Recibo:\nCliente: {cliente.getNombre()}\n"
                                f"Máquina: {maquinaSeleccionada.getNombre()}\n"
                                f"Precio: {maquinaSeleccionada.getPrecioUso()}\n"
                                f"Saldo restante: {cliente.getSaldo()}"
                                )
                            app.resultLabel.config(text=recibo)
                        else:
                            raise SaldoInsuficienteExcepcion(cliente.getNombre(), maquinaSeleccionada.getPrecioUso())
                    except SaldoInsuficienteExcepcion as e:
                        # Mostrar mensaje de error si el saldo es insuficiente
                        messagebox.showerror("Error", f"{str(e)} {e.mensaje()}")

                app.frame.setComando(comprarBoleta)

            app.frame.setComando(seleccionarZonaDeJuegos)

        app.frame.setComando(identificarCliente)
    #Metodo para calificar las peliculas
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
            try:
                peliculaSeleccionada=None
                
                peliculaSeleccionada = peliculaSeleccionada = next((pelicula for pelicula in peliculas if f"{pelicula.getTitulo()}" in seleccion),None)
    
                if peliculaSeleccionada is None:
                    raise DatoErroneoExcepcion(peliculasOpciones, seleccion)

            except DatoErroneoExcepcion as e:
                messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                return  # Asegurarse de que el código se detenga aquí
            # Solicitar calificación
            app.actualizarFormulario(f"Ingrese una calificación para {peliculaSeleccionada.getTitulo()} (1-5)", ["Calificación"], "Calificación seleccionada")
        
            def ingresarCalificacion():
                try:
                    calificacion = app.frame.getValue("Calificación")
                    if not calificacion or not calificacion.replace('.', '', 1).isdigit():
                        raise ExcepcionSugerida2(calificacion)
                    calificacion=float(calificacion)
                    try:
                        if calificacion < 1 or calificacion > 5:
                            messagebox.showerror("Error","Calificación inválida. Ingrese un valor entre 1 y 5.")
                            return
                    except ValueError:
                        messagebox.showerror("Error","Calificación inválida. Ingrese un número válido.")
                        return
                except ExcepcionSugerida2 as e:
                    messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
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
    #Metodo para comprar las boletas para ver una pelicula
    @staticmethod
    def comprarBoleta(app):
        Interfaz.limpiarFormulario(app)

        # Paso 1: Solicitar ID del cliente
        app.procesoLabel.config(text="Comprar Boleta - Paso 1")
        app.indicacionLabel.config(text="Ingrese su ID ")
    
        criterios = ["ID"]
        app.actualizarFormulario("Datos del Cliente", criterios, "Valores", [])
    
        def obtenerCliente():
            clienteId = app.frame.getValue("ID")
            try:
                if not clienteId.isdigit():
                    raise ExcepcionSugerida2(clienteId)
                clienteId=int(clienteId)
            except ExcepcionSugerida2 as s:
                messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                return
            cliente = Cliente.buscarClientePorId(clienteId)
        
            # Si el cliente no existe, ofrecer opción de crearlo
            if cliente is None:
                app.indicacionLabel.config(text="Cliente no encontrado. ¿Desea crear uno?")
                app.actualizarFormulario("Opciones", ["Crear Cliente(Si/No)"], "Opciones")
            
                def crearCliente():
                    crearCliente = app.frame.getValue("Crear Cliente(Si/No)")
                    if crearCliente == "Si":
                        # Solicitar nombre y saldo del nuevo cliente
                        criteriosCliente = ["Nombre", "Saldo","ID"]
                        valoresCliente=["","",str(clienteId)]
                        habilitado=[True,True,False]
                        app.indicacionLabel.config(text="Ingrese los datos del nuevo cliente")
                        app.actualizarFormulario("Crear Cliente", criteriosCliente, "Valores", valoresCliente,habilitado)
                    
                        def confirmarCliente():
                            nombre = app.frame.getValue("Nombre")
                            saldo = app.frame.getValue("Saldo")
                            try:
                                if not saldo.isdigit():
                                    raise ExcepcionSugerida2(saldo)
                                saldo=int(saldo)
                            except ExcepcionSugerida2 as s:
                                messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                                return
                            clienteId=int(app.frame.getValue("ID"))
                            nuevoCliente = Cliente(nombre, saldo, clienteId)
                            app.resultLabel.config(text=app.resultLabel.cget("text") + f"\nCliente {nombre} creado con éxito.")
                            continuarCompra(nuevoCliente)
                    
                        app.frame.setComando(confirmarCliente)
                    elif crearCliente=="No":
                        app.resultLabel.config(text=app.resultLabel.cget("text") + "\nNo se realizó la compra.")
                        return
                    else:
                        messagebox.showerror("Error","Opcion no valida")
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
                cineSeleccionadoNombre = app.frame.getValue("Seleccione Cine")
            
                try:
                    cineSeleccionado = None
                    # Buscar si el cine existe en la lista de cines
                    cineSeleccionado = next((cine for cine in Cine.cines if cine.getNombre() == cineSeleccionadoNombre),None)
    
                    # Si no se encuentra el cine, lanza la excepción
                    if cineSeleccionado is None:
                        raise DatoErroneoExcepcion(cinesDisponibles, cineSeleccionadoNombre)

                except DatoErroneoExcepcion as e:
                    messagebox.showerror("Error", f"{str(e)}\n{e.mensaje()}")
                    return  # Asegurarse de que el código se detenga aquí
            
                # Paso 3: Seleccionar función
                diasSemana = ['Lunes', 'Martes', 'Jueves', 'Viernes', 'Sábado']
                funcionesPorDia = {
                    'Lunes': cineSeleccionado.getLunes(),
                    'Martes': cineSeleccionado.getMartes(),
                    'Jueves': cineSeleccionado.getJueves(),
                    'Viernes': cineSeleccionado.getViernes(),
                    'Sábado': cineSeleccionado.getSabado(),
                }

                funcionesDisponibles = []
                funcionMap = {}
                contador = 1
                for dia in diasSemana:
                    funcionesDia = funcionesPorDia[dia]
                    for funcion in funcionesDia:
                        if funcion:
                            pelicula = funcion.getPelicula().getTitulo()
                            funcionesDisponibles.append(f"{contador}. {dia}: {pelicula}")
                            funcionMap[contador] = funcion
                            contador += 1

                app.procesoLabel.config(text="Comprar Boleta - Paso 3")
                app.indicacionLabel.config(text="Seleccione la función")
                app.actualizarFormulario("Funcion", ["Seleccione Función"], "Opciones", [])
                app.resultLabel.config(text="\n".join(funcionesDisponibles))

                def seleccionarFuncion():
                    try:
                        # Primer bloque try para seleccionar la función
                        funcionSeleccionadaIndex = app.frame.getValue("Seleccione Función")
                        try:
                            if not funcionSeleccionadaIndex.isdigit():
                                raise ExcepcionSugerida2(funcionSeleccionadaIndex)
                        except ExcepcionSugerida2 as s:
                            messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                            return
        
                         # Validar si la clave existe en funcionMap antes de intentar acceder a ella
                        indiceFuncion = int(funcionSeleccionadaIndex.split()[0])
                        if indiceFuncion not in funcionMap:
                            # Si el índice no está en el mapa, lanzamos la excepción personalizada
                            raise ExcepcionSugerida1()

                        # Accedemos a la función seleccionada solo si la clave es válida
                        funcionSeleccionada = funcionMap[indiceFuncion]

                        # Actualizamos la interfaz
                        app.resultLabel.config(text=funcionSeleccionada.getSala().estadoSilleteria())

                        # Paso 4: Seleccionar asiento
                        app.procesoLabel.config(text="Comprar Boleta - Paso 4")
                        app.indicacionLabel.config(text="Seleccione la fila y columna")
                        app.actualizarFormulario("Asiento", ["Fila", "Columna"], "Valores", [])

                        def seleccionarAsiento():
                            # Captura la fila y columna y las convierte a índice
                            fila = app.frame.getValue("Fila")
                            columna = app.frame.getValue("Columna")
                            try:
                                if not fila.isdigit():
                                    raise ExcepcionSugerida2(fila)
                                fila=int(fila)-1
                            except ExcepcionSugerida2 as s:
                                messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                                return
                            try:
                                if not columna.isdigit():
                                    raise ExcepcionSugerida2(columna)
                                columna=int(columna)-1
                            except ExcepcionSugerida2 as s:
                                messagebox.showerror("Error", f"{str(s)} {s.mensaje}")
                                return

                            # Validamos si el asiento está disponible
                            if funcionSeleccionada.getSala().estaDisponible(fila, columna):
                                funcionSeleccionada.getSala().reservarSilla(fila, columna)
                                app.resultLabel.config(text=app.resultLabel.cget("text") + "\nAsiento reservado con éxito.")
                                mostrarRecibo(cliente, cineSeleccionado, funcionSeleccionada, fila, columna)
                            else:
                                messagebox.showerror("Error","El asiento seleccionado no esta disponible")
                                return
                            

                        # Asignamos el comando para seleccionar asiento
                        app.frame.setComando(seleccionarAsiento)
    
                    except IndexError:
                        # Si ocurre un error de índice en la selección de función, lanzamos la excepción personalizada
                        raise ExcepcionSugerida1()

                    # Capturamos la excepción personalizada y mostramos un mensaje de error en un pop-up
                    except ExcepcionSugerida1 as s:
                        messagebox.showerror("Error", str(s))
            
                app.frame.setComando(seleccionarFuncion)
        
            app.frame.setComando(seleccionarCine)
    
        def mostrarRecibo(cliente, cine, funcion, fila, columna):
            # Mostrar el recibo final
            precio = funcion.getPrecio()
            try:
                # Paso 4: Realizar la compra
                if cliente.getSaldo() >= precio:
                    cliente.setSaldo(cliente.getSaldo() - precio)
                    app.resultLabel.config(text="Compra realizada exitosamente.")

                    # Paso 5: Asignar bono si está activo
                    bonoMensaje = funcion.getPelicula().asignarBono(cliente)
                    app.resultLabel.config(text=f"Compra realizada. {bonoMensaje}")

                    # Paso 6: Imprimir recibo
                    recibo = f"\n--- Recibo de compra ---\nCliente: {cliente.getNombre()} ({cliente.getIdentificacion()})\n" \
                    f"Cine: {cine.getNombre()}\nPelícula: {funcion.getPelicula().getTitulo()}\nSala: {funcion.getSala().getNumero()}\n" \
                    f"Asiento: Fila {fila + 1}, Columna {columna + 1}\nHora de la función: {funcion.getHoraInicio()}\n" \
                    f"Precio total: ${precio:.2f}\n------------------------"
                    app.resultLabel.config(text=app.resultLabel.cget("text") + recibo)
                    
                else:
                    raise SaldoInsuficienteExcepcion(cliente.getNombre(), precio)
            except SaldoInsuficienteExcepcion as e:
                # Mostrar mensaje de error si el saldo es insuficiente
                messagebox.showerror("Error", f"{str(e)} {e.mensaje()}")
            
        
            
            

    #Limpia la ventana cada vez que se ingresa a un metodo
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
        
    #Llama a todos los metodos que serializan y les manda el archivo donde lo deben hacer
    @staticmethod
    def serializarTodo():
        base_path = os.path.dirname(__file__)  # Obtener la ruta del archivo actual

        # Crear rutas absolutas y serializar
        Cine.serializarCines(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'cine.pkl')))
        Cliente.serializarClientes(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'cliente.pkl')))
        Funcion.serializarFunciones(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'funcion.pkl')))
        Pelicula.serializarPeliculas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'pelicula.pkl')))
        Sala.serializarSalas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'sala.pkl')))
        ZonaDeJuegos.serializarZonasDeJuegos(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'zonaDeJuegos.pkl')))
        Bodega.serializarBodegas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'bodega.pkl')))
        Maquina.serializarMaquinas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'maquina.pkl')))

    @staticmethod
    def deserializarTodo():
        base_path = os.path.dirname(__file__)  # Obtener la ruta del archivo actual

        # Crear rutas absolutas y deserializar
        Cine.deserializarCines(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'cine.pkl')))
        Cliente.deserializarClientes(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'cliente.pkl')))
        Funcion.deserializarFunciones(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'funcion.pkl')))
        Pelicula.deserializarPeliculas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'pelicula.pkl')))
        Sala.deserializarSalas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'sala.pkl')))
        ZonaDeJuegos.deserializarZonasDeJuegos(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'zonaDeJuegos.pkl')))
        Bodega.deserializarBodegas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'bodega.pkl')))
        Maquina.deserializarMaquinas(os.path.abspath(os.path.join(base_path, '..', 'baseDatos', 'temp', 'maquina.pkl')))

    


        



    


        

