import tkinter as tk

def add():
    entry = str(entryRequirement.get())
    #DEBO PONER LA LÓGICA PARA EL BACK END Y QUE LUEGO ME DEVUELVA EL VALOR
    result = tk.Label(text = "" + entry)
    result.pack()

def order():
    entry = str(entryRequirement.get())
    #DEBO PONER LA LÓGICA PARA EL BACK END Y QUE LUEGO ME DEVUELVA EL VALOR
    result = tk.Label(text = "" + entry)
    result.pack()

def simplify():
    entry = str(entryRequirement.get())
    #DEBO PONER LA LÓGICA PARA EL BACK END Y QUE LUEGO ME DEVUELVA EL VALOR
    result = tk.Label(text = "" + entry)
    result.pack()

window = tk.Tk()

labelRequirement = tk.Label(text = "Ingresa un polinomio, (ejemplo: 2x*2 + 3x*2 - 2x + 4)")
labelRequirement.pack()

entryRequirement = tk.Entry()
entryRequirement.pack()

buttonAdd = tk.Button(window, text = "Agregar", width = 10, command = add)
buttonAdd.pack()

buttonOrder = tk.Button(window, text = "Ordenar", width = 10, command = order)
buttonOrder.pack()

buttonSimplify = tk.Button(window, text = "Simplificar", width = 10, command = simplify)
buttonSimplify.pack()

window.mainloop()