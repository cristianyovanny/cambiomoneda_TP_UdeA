from tkinter import *
from tkinter.ttk import Notebook
import Util
import pandas as pd
from datetime import *
from matplotlib import pyplot as plt

iconos = ["./iconos/Grafica.png", \
          "./iconos/Datos.png"]

textos = ["Gráfica", "Datos estadísticos"]

datos = None


def obtenerMonedas():
    global datos
    datos = pd.read_csv("Cambios Monedas.csv")
    monedas = datos["Moneda"].tolist()
    return list(dict.fromkeys(monedas))

def graficar():
    global datos, monedas
    if cmb_moneda.current () >= 0:
        datos.sort_values(by = "Fecha", ascending = False).head()
        cambios = datos[ datos["Moneda"] == monedas[cmb_moneda.current()]]

        y = cambios["Cambio"]
        fechas = cambios["Fecha"]
        x = [datetime.strptime(f, "%d/%m/%Y").date()  for f in fechas]

        plt.figure(figsize=(8, 4), dpi=50)
        plt.title("Cambios de " + monedas[cmb_moneda.current()])
        plt.ylabel("Cambio")
        plt.xlabel("Fecha")
        plt.plot(x, y)

        plt.savefig("graficaMonedas.png")
        img_grafica = PhotoImage(file = "graficaMonedas.png")

        lbl_grafica = Label(paneles[0])
        lbl_grafica.config(image = img_grafica)
        lbl_grafica.image = img_grafica
        lbl_grafica.place(x = 0, y = 0)

def estadisticas():
    pass

v = Tk()
v.title("Cambios de Moneda")
v.geometry("400x300")

botones = Util.agregarBarra(v, iconos, textos)
botones[0].configure(command = graficar)
botones[1].configure(command = estadisticas)

frm = Frame(v)
frm.pack(side = TOP, fill = X)
Util.agregarEtiqueta(frm, "Moneda", 0, 0)
monedas = obtenerMonedas()
cmb_moneda = Util.agregarLista(frm, monedas, 0, 1)

nb = Notebook(v)
nb.pack(fill = BOTH, expand = YES)
encabezados = ["Grafica", "Estadisticas"]
paneles = []
for e in encabezados:
    frm = Frame(v)
    paneles.append(frm)
    nb.add(frm, text = e)


