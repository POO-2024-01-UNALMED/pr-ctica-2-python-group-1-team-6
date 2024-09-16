import tkinter as tk
from tkinter import messagebox
#Esta es la clase que crea los formularios que se usan en la interfaz
class FieldFrame(tk.Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(parent)
        
        # Titulo de las columnas
        tk.Label(self, text=tituloCriterios).grid(row=0, column=0)
        tk.Label(self, text=tituloValores).grid(row=0, column=1)

        # Listas para almacenar entradas y etiquetas
        self.criterios = criterios
        self.entries = {}
        
        #Crear etiquetas y campos de entrada
        for i, criterio in enumerate(criterios):
            tk.Label(self, text=criterio).grid(row=i + 1, column=0)

            entry = tk.Entry(self)
            entry.grid(row=i + 1, column=1)

            if valores:
                entry.insert(0, valores[i])

            self.entries[criterio] = entry
            # Deshabilita el campo si es necesario
            if habilitado and not habilitado[i]:
                entry.config(state='disabled')
    
        #Crea y ubica el boton borrar y aceptar
        tk.Button(self, text="Borrar", font = ("Arial", 12), fg = "white", bg = "blue",command=self.clear,
        width=12,height=2).grid(pady = (10,10), padx=(10,10), column = 1, row = len(self.criterios)+1, columnspan=3)
        tk.Button(self, text="Aceptar", font = ("Arial", 12), fg = "white", bg = "blue", width=7,height=2, command=lambda: self.funAceptar(self.comando)).grid(pady = (10,10),
            padx=(10,10), column = 0, row = len(self.criterios)+1)

        self.comando = None
    #Limpia las entradas
    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def getValue(self, criterio):
       #retorna el valor del criterio
        entry = self.entries.get(criterio)
        if entry:
            return entry.get()
        else:
            return None

    def validar(self):
        #Valida que todos los campos estén llenos
        for criterio in self.criterios:
            value = self.getValue(criterio)
            if not value:
                messagebox.showwarning("Error", f"El campo {criterio} no puede estar vacío.")
                return False
        return True

    def funAceptar(self, comando=None):
        #Valida los campos y, si son válidos, ejecuta el comando que le pasan
        if self.validar():
            # Si la validacion se da ejecuta el comando
            if comando is not None:
                comando()  # Ejecuta el comando pasado
        else:
            pass

    def setComando(self, comando):
        #Permite configurar el comando a ejecutar cuando se presiona Aceptar.
        self.comando = comando
        
        