import tkinter as tk
from tkinter import ttk
import util.generic as utl


class MasterPanel():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('¿Como se cuanto pago de impuestos?')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 500)

        logo = utl.leer_imagen("./imagenes/tabla.png", (650, 400))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=700,
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
        title = tk.Label(frame_form_top, text="¿Que me puede pasar si no pago impuestos?", font=(
            'Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="c", font=(
            'Arial', 13), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        self.ventana.mainloop()