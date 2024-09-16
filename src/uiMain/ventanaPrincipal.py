import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import tkinter as tk
from tkinter import messagebox
from src.uiMain.fieldFrame import FieldFrame
from src.uiMain.interfaz import Interfaz

#Ventana principal
class ventanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Start Cinema")
        self.geometry("1900x750")
        # Crear etiquetas y campos
        self.procesoLabel = tk.Label(self, text="")
        self.procesoLabel.pack(side="top")

        self.indicacionLabel = tk.Label(self, text="")
        self.indicacionLabel.pack(side="top")

        self.resultLabel = tk.Label(self, text="", fg="blue",width=400)
        self.resultLabel.pack(side="bottom", fill="both", expand=True)
        self.widgetsSueltos = []

        self.frame =None
        
        self.imagen = tk.PhotoImage(file="src/uiMain/Imagenes/start.png")

        # Crear una etiqueta con la imagen que aparece de "interfaz"
        self.imagenLabel = tk.Label(self, image=self.imagen)
        self.imagenLabel.pack(expand=True, fill="both")
        # Crear menu 
        self.crearMenu()
    
    def crearMenu(self):
        #Crear el menu
        menubar = tk.Menu(self)
        
        # Archivo menu
        archivoMenu = tk.Menu(menubar, tearoff=0)
        archivoMenu.add_command(label="Aplicación", command=self.mostrarInfo)
        archivoMenu.add_command(label="Salir", command=self.volverAVentanaInicio)
        menubar.add_cascade(label="Archivo", menu=archivoMenu)

        # Procesos y Consultas menu
        procesosMenu = tk.Menu(menubar, tearoff=0)
        procesosMenu.add_command(label="Comprar boleto para ver una funcion",command=self.comprarBoleto)
        procesosMenu.add_command(label="Comprar boleto para jugar maquinitas",command=self.jugarMaquinitas)
        procesosMenu.add_command(label="Calificar Pelicula",command=self.calificarPelicula)
        procesosMenu.add_command(label="Gestionar zonas de juegos",command=self.gestionarZonaDeJuegos)
        procesosMenu.add_command(label="Gestionar Peliculas",command=self.gestionarPeliculas)
        procesosMenu.add_command(label="Menu de creacion",command=self.menuCreacion)
        procesosMenu.add_command(label="Menu de asignacion",command=self.menuAsignacion)
        menubar.add_cascade(label="Procesos y Consultas", menu=procesosMenu)

        # Ayuda menu
        ayudaMenu = tk.Menu(menubar, tearoff=0)
        ayudaMenu.add_command(label="Acerca de", command=self.mostrarAutores)
        menubar.add_cascade(label="Ayuda", menu=ayudaMenu)

        self.config(menu=menubar)

    def mostrarInfo(self):
        #Mostrar informacion sobre la aplicacion
        messagebox.showinfo("Información", """Aplicación de Simulación de Cine:

Compra boletos para películas y juegos, gestiona las zonas de juegos y administra la programación de películas en los cines. Ofrece una experiencia completa de operación y gestión de un cine.""")

    def mostrarAutores(self):
        #Mostrar los autores de la aplicacion
        messagebox.showinfo("Acerca de", """Autores: Juan Manuel Henao Rodriguez """)
    
    def gestionarZonaDeJuegos(self):
       Interfaz.gestionarZonaDeJuegos(self)
    
    def gestionarPeliculas(self):
       Interfaz.gestionarPeliculas(self)
    def menuCreacion(self):
       Interfaz.menuCreacion(self)
    def menuAsignacion(self):
        Interfaz.menuAsignacion(self)
    def jugarMaquinitas(self):
        Interfaz.comprarBoletaJuegos(self)
    def calificarPelicula(self):
        Interfaz.calificarPelicula(self)
    def comprarBoleto(self):
        Interfaz.comprarBoleta(self)
    
    def actualizarFormulario(self, titulo_criterios, criterios, titulo_valores, valores=None,habilitado=None):
        #Actualiza los formularios de la interfaz
        if self.frame:
            self.frame.pack_forget()
        
        # Crear un nuevo FieldFrame
        self.frame = FieldFrame(self, titulo_criterios, criterios, titulo_valores, valores,habilitado)
        self.frame.pack(side="top", anchor="center")
    
    def volverAVentanaInicio(self):
        from src.uiMain.ventanaInicio import ventanaInicio
        self.destroy()  # Cerrar la ventana principal completamente para evitar conflictos
        nuevaVentanaInicio = ventanaInicio()  # Crear una nueva instancia de la ventana de inicio
        nuevaVentanaInicio.mainloop()
        
        
        
        

        

