import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#Ventana de inicio
class ventanaInicio(tk.Tk):
    def __init__(self):
        # Crear ventana
        super().__init__()
        self.geometry("1900x750")
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
        textSaludo = """
        Bienvenido 
        al Sistema"""
        saludo = tk.Label(p3, text=textSaludo, font=("Arial", 30), bg="black", fg="white")
        saludo.pack(fill="both", expand=True)

        # Hojas de vida
        self.textHoja1 = """
        Nombre: Juan Manuel Henao Rodriguez
        
        Edad: 18 años
        
        Ocupacion: Estudiante de ingenieria de sistemas e informatica (2 semestre)
        
        Lugar de nacimiento: Corregimiento San Diego municipio de Liborina-Antioquia
        
        Cualidades: Responsable, proactivo y capacidad de aprendizaje rápido.
        """
        self.textHoja2 = """
        Nombre: Jhoan Alexis Rua Garcia
        
        Edad: 19 años
        
        Ocupacion: Estudiante de ingenieria de sistemas e informatica (2 semestre)
        
        Lugar de nacimiento: Municipio de Barbosa-Antioquia
        
        Cualidades: Creativo, comprometido y capacidad para resolver problemas.
        """
        self.hojaDeVida = tk.Button(p5, text=self.textHoja1,command=self.hojasDeVida, bg="black", fg="white", font=("Arial", 15))
        self.hojaDeVida.pack(fill="both", expand=True)

        # Cargar imágenes
        self.cargarImagenes()

        self.label1 = tk.Label(p6, image=self.imagen1)
        self.label1.grid(row=0, column=0, sticky="nw",padx=120,pady=5)
        self.label2 = tk.Label(p6, image=self.imagen2)
        self.label2.grid(row=0, column=1, sticky="ne",padx=30,pady=5)
        self.label3 = tk.Label(p6, image=self.imagen3)
        self.label3.grid(row=1, column=0, sticky="sw",padx=120,pady=5)
        self.label4 = tk.Label(p6, image=self.imagen4)
        self.label4.grid(row=1, column=1, sticky="se",padx=30,pady=5)

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
        #Cargar todas las imagenes
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # Construye las rutas absolutas para cada imagen
        ruta_imagen1 = os.path.join(dir_actual, 'Imagenes', 'itachi1.png')
        ruta_imagen2 = os.path.join(dir_actual, 'Imagenes', 'itachi2.png')
        ruta_imagen3 = os.path.join(dir_actual, 'Imagenes', 'itachi3.png')
        ruta_imagen4 = os.path.join(dir_actual, 'Imagenes', 'itachi4.png')
        ruta_imagen5 = os.path.join(dir_actual, 'Imagenes', 'shisui1.png')
        ruta_imagen6 = os.path.join(dir_actual, 'Imagenes', 'shisui2.png')
        ruta_imagen7 = os.path.join(dir_actual, 'Imagenes', 'shisui3.png')
        ruta_imagen8 = os.path.join(dir_actual, 'Imagenes', 'shisui4.png')
        ruta_imagen9 = os.path.join(dir_actual, 'Imagenes', 'images.png')
        ruta_imagen10 = os.path.join(dir_actual, 'Imagenes', 'descarga-_1_.png')
        ruta_imagen11 = os.path.join(dir_actual, 'Imagenes', 'descarga-_2_.png')
        ruta_imagen12 = os.path.join(dir_actual, 'Imagenes', 'descarga-_3_.png')
        ruta_imagen13 = os.path.join(dir_actual, 'Imagenes', 'descarga.png')

        # Cargar las imágenes usando las rutas absolutas
        self.imagen1 = tk.PhotoImage(file=ruta_imagen1)
        self.imagen2 = tk.PhotoImage(file=ruta_imagen2)
        self.imagen3 = tk.PhotoImage(file=ruta_imagen3)
        self.imagen4 = tk.PhotoImage(file=ruta_imagen4)
        self.imagen5 = tk.PhotoImage(file=ruta_imagen5)
        self.imagen6 = tk.PhotoImage(file=ruta_imagen6)
        self.imagen7 = tk.PhotoImage(file=ruta_imagen7)
        self.imagen8 = tk.PhotoImage(file=ruta_imagen8)
        self.imagen9 = tk.PhotoImage(file=ruta_imagen9)
        self.imagen10 = tk.PhotoImage(file=ruta_imagen10)
        self.imagen11 = tk.PhotoImage(file=ruta_imagen11)
        self.imagen12 = tk.PhotoImage(file=ruta_imagen12)
        self.imagen13 = tk.PhotoImage(file=ruta_imagen13)
        self.imagenesRotacion = [self.imagen9, self.imagen10, self.imagen11, self.imagen12, self.imagen13]

    def hojasDeVida(self):
        #Alternar entre los personajes en el botón de hojas de vida
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
        #Rota las imagenes cuando el mouse sale del area
        self.imagenActual = (self.imagenActual + 1) % len(self.imagenesRotacion)
        self.label5.config(image=self.imagenesRotacion[self.imagenActual])

    def salir(self):
        #Boton para cerrar el sistema y guardar todo
        from src.uiMain.interfaz import Interfaz
        Interfaz.serializarTodo()
        self.destroy()

    def alternarVisibilidad(self):
        #Alternar la visibilidad de la descripción del sistema
        if self.descripcionVisible:
            if self.frameCentral:
                self.frameCentral.destroy()
                self.frameCentral = None
            self.descripcionVisible = False
        else:
            if self.frameCentral is None:
                self.frameCentral = tk.Frame(self)
                self.frameCentral.place(x=600,y=150)
                descripcionText = """
El sistema, al presionar 
el botón 'Ventana Principal', 
te redireccionará a otra 
ventana con un menú llamado 
'Procesos y Consultas'. 
Este menú te mostrará 
opciones para crear y asignar 
los objetos que conforman un 
cine, gestionar tus zonas 
de juegos y películas, y, 
obviamente, podrás comprar 
boletos tanto para el cine 
como para las máquinas 
de juegos."""
                self.frameCentral.lift()
                descripcion = tk.Label(self.frameCentral, text=descripcionText, font=("Arial", 20),bg="black",fg="white")
                descripcion.pack(expand=True)
            self.descripcionVisible = True

    def abrirVentanaPrincipal(self):
        #Abrir la ventana principal y destruir la ventana de inicio, ademas carga toda la info del sistema
        from src.uiMain.ventanaPrincipal import ventanaPrincipal
        from src.uiMain.interfaz import Interfaz
        self.destroy()  # Ocultar la ventana de inicio
        Interfaz.deserializarTodo()
        app = ventanaPrincipal()
        app.mainloop()

if __name__ == "__main__":
    app=ventanaInicio()
    app.mainloop()
    