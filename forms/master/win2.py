import tkinter as tk
from tkinter import ttk
import util.generic as utl


class MasterPanel():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('¿Por que pagar impuestos?')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 500)

        logo = utl.leer_imagen("./imagenes/inicio.png", (150, 150))

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
        title = tk.Label(frame_form_top, text="¿Por qué pagar Impuestos?", font=(
            'Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="La recaudación de los impuestos se destina a la satisfacción de ciertas\n necesidades de carácter colectivo como: la educación pública, la\n impartición de justicia, la seguridad, los hospitales públicos, la\n infraestructura y servicios de vías públicas, programas y proyectos de apoyo\n al desarrollo social y económico, necesidades que por separado cada\n persona no podría pagar por sí sola, pero que, en cambio, se pueden\n atender con las aportaciones de todos.\n Estos servicios ocasionan gastos y gracias a nuestras contribuciones la\n Federación cuenta con los recursos necesarios para: disponer de escuelas\n con profesores que contribuyan en tu enseñanza; disfrutar de bibliotecas,\n hospitales y centros deportivos; el mantenimiento de las calles de la ciudad\n en la que vivimos y su iluminación; para construir y arreglar las carreteras;\n para contar con un servicio de bomberos, policías y militares, que se\n ocupen de mantener nuestra seguridad.", font=(
            'Arial', 11), fg="#000000", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        self.ventana.mainloop()