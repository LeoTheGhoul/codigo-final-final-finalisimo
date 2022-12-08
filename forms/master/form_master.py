import tkinter as tk
from tkinter import ttk
import util.generic as utl


class MasterPanel():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Menu Principal')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 500)

        logo = utl.leer_imagen("./imagenes/principal.png", (150, 150))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg='#fed42b')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#fed42b')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Bienvenido a SIT", font=(
            'Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        inicio = tk.Button(frame_form_fill, text="¿Que son los Imupuestos?", font=(
            'Times', 15), bg='#cc3474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))

        inicio = tk.Button(frame_form_fill, text="¿Por que pagar Imupuestos?", font=(
            'Times', 15), bg='#cc3474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))

        inicio = tk.Button(frame_form_fill, text="¿Para que sirven los Imupuestos?", font=(
            'Times', 15), bg='#cc3474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))

        inicio = tk.Button(frame_form_fill, text="¿Que me puede pasar si no pago Imupuestos?", font=(
            'Times', 15), bg='#cc3474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))

        inicio = tk.Button(frame_form_fill, text="¿Como calculo los Imupuestos?", font=(
            'Times', 15), bg='#cc3474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))

        self.ventana.mainloop()

    def register():
        pass