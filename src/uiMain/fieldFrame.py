import tkinter as tk
from tkinter import messagebox
class FieldFrame(tk.Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(parent)
        
        # Column Titles
        tk.Label(self, text=tituloCriterios).grid(row=0, column=0)
        tk.Label(self, text=tituloValores).grid(row=0, column=1)

        # Lists for storing entries and labels
        self.criterios = criterios
        self.entries = {}
        
        # Create Labels and Entry fields
        for i, criterio in enumerate(criterios):
            # Create label for each criterion
            tk.Label(self, text=criterio).grid(row=i + 1, column=0)

            # Create corresponding Entry field
            entry = tk.Entry(self)
            entry.grid(row=i + 1, column=1)

            # Disable the field if required
            if habilitado and not habilitado[i]:
                entry.config(state='disabled')
            
            # Insert initial values if provided
            if valores:
                entry.insert(0, valores[i])

            self.entries[criterio] = entry
        
        tk.Button(self, text="Borrar", font = ("Arial", 12), fg = "white", bg = "blue",command=self.clear,
        width=12,height=2).grid(pady = (10,10), padx=(10,10), column = 1, row = len(self.criterios)+1, columnspan=3)
        tk.Button(self, text="Aceptar", font = ("Arial", 12), fg = "white", bg = "blue", width=7,height=2, command=lambda: self.funAceptar(self.comando)).grid(pady = (10,10),
            padx=(10,10), column = 0, row = len(self.criterios)+1)

        self.comando = None

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
        #Valida los campos y, si son válidos, ejecuta el comando pasado como argumento
        if self.validar():
            # Si la validación es exitosa, ejecuta el comando
            if comando is not None:
                comando()  # Ejecuta el comando pasado
        else:
            pass

    def setComando(self, comando):
        #Permite configurar el comando a ejecutar cuando se presiona Aceptar.
        self.comando = comando
        