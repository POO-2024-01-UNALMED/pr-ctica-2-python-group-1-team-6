import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class ventanaInicio(tk.Tk):
    def __init__(self):
        # Crear ventana
        super().__init__()
        self.geometry("700x700")
        self.title("Ventana de Inicio")
        self.config(bg="black")

        # Paneles
        p1 = tk.Frame(self, bg="gray")
        p1.pack(side="left", fill="both", expand=True, padx=10, pady=15)
        p2 = tk.Frame(self, bg="gray")
        p2.pack(side="right", fill="both", expand=True, padx=10, pady=15)
        p3 = tk.Frame(p1, bg="gray", width=100, height=50)
        p3.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        p4 = tk.Frame(p1, bg="blue", width=100, height=200)
        p4.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)
        p5 = tk.Frame(p2, bg="gray", width=100, height=50)
        p5.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        p6 = tk.Frame(p2, bg="black", width=100, height=200)
        p6.pack(side="bottom", fill="both", padx=5, pady=5)

        # Texto de bienvenida
        textSaludo = """Bienvenido
        al
        Sistema"""
        saludo = tk.Label(p3, text=textSaludo, font=("Arial", 30), bg="black", fg="white")
        saludo.pack(fill="both", expand=True)

        # Hojas de vida
        self.textHoja1 = """Personaje 1: Luna Starwind..."""
        self.textHoja2 = """Personaje 2: Kai Vortex..."""
        self.hojaDeVida = tk.Button(p5, text=self.textHoja1, command=self.hojasDeVida, bg="black", fg="white", font=("Arial", 15))
        self.hojaDeVida.pack(fill="both", expand=True)

        # Cargar imágenes
        self.cargarImagenes()

        # Mostrar imágenes iniciales
        self.label1 = tk.Label(p6, image=self.imagen1)
        self.label1.grid(row=0, column=0, sticky="nw")
        self.label2 = tk.Label(p6, image=self.imagen2)
        self.label2.grid(row=0, column=1, sticky="ne")
        self.label3 = tk.Label(p6, image=self.imagen3)
        self.label3.grid(row=1, column=0, sticky="sw")
        self.label4 = tk.Label(p6, image=self.imagen4)
        self.label4.grid(row=1, column=1, sticky="se")

        # Botón de ventana principal
        ventanaPrincipal = tk.Button(p4, text="Ventana Principal", bg="black", fg="white", font=("Arial", 20), command=self.abrirVentanaPrincipal)
        ventanaPrincipal.pack(side="bottom", expand=True, fill="both")

        # Rotación de imágenes
        self.imagenActual = 0
        self.label5 = tk.Label(p4, image=self.imagenesRotacion[self.imagenActual])
        self.label5.pack(side="top", expand=True, fill="both")
        self.label5.bind("<Leave>", self.rotarImagen)

        # Menú
        self.descripcionVisible = False
        self.frameCentral = None
        menuBar = tk.Menu(self)
        self.config(menu=menuBar)
        menu1 = tk.Menu(menuBar)
        menuBar.add_cascade(label="Inicio", menu=menu1)
        menu1.add_command(label="Salir de la aplicación", command=self.salir)
        menu1.add_command(label="Descripción del sistema", command=self.alternarVisibilidad)

        

    def cargarImagenes(self):
        """Cargar todas las imágenes necesarias"""
        self.imagen1 = tk.PhotoImage(file="src/uiMain/Imagenes/iatchi1.png")
        self.imagen2 = tk.PhotoImage(file="src/uiMain/Imagenes/itachi2.png")
        self.imagen3 = tk.PhotoImage(file="src/uiMain/Imagenes/itachi3.png")
        self.imagen4 = tk.PhotoImage(file="src/uiMain/Imagenes/itachi4.png")
        self.imagen5 = tk.PhotoImage(file="src/uiMain/Imagenes/shisui1.png")
        self.imagen6 = tk.PhotoImage(file="src/uiMain/Imagenes/shisui2.png")
        self.imagen7 = tk.PhotoImage(file="src/uiMain/Imagenes/shisui3.png")
        self.imagen8 = tk.PhotoImage(file="src/uiMain/Imagenes/shisui4.png")
        self.imagen9 = tk.PhotoImage(file="src/uiMain/Imagenes/images.png")
        self.imagen10 = tk.PhotoImage(file="src/uiMain/Imagenes/descarga-_1_.png")
        self.imagen11 = tk.PhotoImage(file="src/uiMain/Imagenes/descarga-_2_.png")
        self.imagen12 = tk.PhotoImage(file="src/uiMain/Imagenes/descarga-_3_.png")
        self.imagen13 = tk.PhotoImage(file="src/uiMain/Imagenes/descarga.png")
        self.imagenesRotacion = [self.imagen9, self.imagen10, self.imagen11, self.imagen12, self.imagen13]

    def hojasDeVida(self):
        """Alternar entre los personajes en el botón de hojas de vida"""
        actualText = self.hojaDeVida['text']
        if actualText == self.textHoja1:
            self.hojaDeVida.config(text=self.textHoja2)
            self.label1.config(image=self.imagen5)
            self.label2.config(image=self.imagen6)
            self.label3.config(image=self.imagen7)
            self.label4.config(image=self.imagen8)
        else:
            self.hojaDeVida.config(text=self.textHoja1)
            self.label1.config(image=self.imagen1)
            self.label2.config(image=self.imagen2)
            self.label3.config(image=self.imagen3)
            self.label4.config(image=self.imagen4)

    def rotarImagen(self, event):
        """Rotar imágenes cuando el mouse sale del área"""
        self.imagenActual = (self.imagenActual + 1) % len(self.imagenesRotacion)
        self.label5.config(image=self.imagenesRotacion[self.imagenActual])

    def salir(self):
        """Cerrar la aplicación"""
        self.ventanaInicio.destroy()

    def alternarVisibilidad(self):
        """Alternar la visibilidad de la descripción del sistema"""
        if self.descripcionVisible:
            if self.frameCentral:
                self.frameCentral.destroy()
                self.frameCentral = None
            self.descripcionVisible = False
        else:
            if self.frameCentral is None:
                self.frameCentral = tk.Frame(self.ventanaInicio)
                self.frameCentral.pack(expand=True)
                descripcionText = "Es un sistema de cines muy chimba"
                descripcion = tk.Label(self.frameCentral, text=descripcionText, font=("Arial", 20))
                descripcion.pack(expand=True)
            self.descripcionVisible = True

    def abrirVentanaPrincipal(self):
        """Abrir la ventana principal y ocultar la ventana de inicio"""
        from src.uiMain.ventanaPrincipal import ventanaPrincipal
        from src.uiMain.interfaz import Interfaz
        self.destroy()  # Ocultar la ventana de inicio
        Interfaz.deserializarTodo()
        app = ventanaPrincipal()
        app.mainloop()


if __name__ == "__main__":
    app=ventanaInicio()
    app.mainloop()
    