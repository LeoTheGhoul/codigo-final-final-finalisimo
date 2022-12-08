import tkinter as tk
from tkinter import ttk
import util.generic as utl


class MasterPanel():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('¿Para que sirven los impuestos?')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 500)

        logo = utl.leer_imagen("./imagenes/inicio.png", (150, 150))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg='#ef6e96')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#ef6e96')
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
        title = tk.Label(frame_form_top, text="¿Para que sirven los impuestos?", font=(
            'Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Los impuestos sirven para pagar los gastos del estado, gracias a estos\n es posible financiar la construcción de obras públicas como carreteras,\n estaciones eléctricas, aeropuertos, etc.\n También permiten cubrir los gastos que se invierten en salud, educación,\n seguridad, ayudas sociales, entre otros.\n De los impuestos también se extraen los valores para pagar los sueldos\n a los gobernantes y a todo el poder público, como los ministerios, las\n fuerzas armadas, las entidades federativas y los municipios.\n Además, parte del dinero recaudado se destina a pagar la deuda pública.\n La recaudación de tributos es la principal fuente de ingresos del estado,\n sin ellos no sería posible mantener un país.", font=(
            'Arial', 11), fg="#000000", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        self.ventana.mainloop()