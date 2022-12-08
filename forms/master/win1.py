import tkinter as tk
from tkinter import ttk
import util.generic as utl


class MasterPanel():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('¿Que son los impuestos?')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 500)

        logo = utl.leer_imagen("./imagenes/inicio.png", (150, 150))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg='#ee6c94')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#ee6c94')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="¿Que son los impuestos?", font=(
            'Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="El impuesto es una clase de tributo (obligaciones generalmente pecuniarias\n en favor del acreedor tributario) regido por derecho público, que se\n caracteriza por no requerir una contraprestación directa o determinada por\n parte de la administración hacendaria (acreedor tributario).\n En la mayoría de legislaciones, los impuestos surgen exclusivamente por la\n “potestad tributaria del Estado” el que se constituye en el acreedor.\n Generalmente los impuestos son cargas obligatorias para las personas y\n empresas. Un principio rector, denominado “capacidad contributiva”, sugiere\n que quienes más tienen deben aportar en mayor medida al financiamiento\n estatal, para consagrar el principio constitucional de equidad y el\n principio social de la libertad.", font=(
            'Arial', 11), fg="#000000", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        self.ventana.mainloop()
