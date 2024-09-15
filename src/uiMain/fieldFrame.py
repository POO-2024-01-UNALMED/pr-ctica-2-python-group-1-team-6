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


    def getValue(self, criterio):
       #retorna el valor del criterio
        entry = self.entries.get(criterio)
        if entry:
            return entry.get()
        else:
            return None

    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
    def validar(self):
        for criterio in self.criterios:
            value = self.getValue(criterio)
            if not value:
                messagebox.showwarning("Error", f"El campo {criterio} no puede estar vacío.")
                return
        messagebox.showinfo("Guardado", "Datos guardados exitosamente.")
    def funAceptar(self, comando = None):
        tk.Button(self, text="Aceptar", font = ("Arial", 12), fg = "white", bg = "blue", width=7,height=2, command=comando).grid(pady = (10,10),
        padx=(10,10), column = 0, row = len(self.criterios)+1)
        self.validar