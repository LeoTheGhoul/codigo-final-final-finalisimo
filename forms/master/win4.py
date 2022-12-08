import tkinter as tk
from tkinter import ttk
import util.generic as utl


class MasterPanel():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('¿Que me puede pasar si no pago impuestos?')
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
        title = tk.Label(frame_form_top, text="¿Que me puede pasar si no pago impuestos?", font=(
            'Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="El SAT solicita el pago de impuestos a las personas morales de la\n siguiente manera:\n\n Carta invitación: envía un mensaje de texto o correo electrónico al\n contribuyente para invitarlo a ponerse al corriente, ya que de no\n hacerlo se puede hacer acreedor a penalizaciones económicas como\n recargos (intereses moratorios), actualizaciones (incremento que sufre\n un adeudo por la inflación) y multas (penalización por cada\n obligación fiscal no presentada).\n\n Multa: si no se atienden las cartas invitación, el SAT procede a\n aplicar directamente una multa, por lo que el acumulado de pagos sería:\n impuesto corriente, recargos, actualizaciones y multa.\n\n Bloqueo de cuentas o embargos: si el negocio sigue teniendo actividad\n comercial, es decir, que entra dinero a sus cuentas, el SAT las interviene\n y las congela para evitar que se sigan realizando cobros y pagos. De igual\n forma, se pueden embargar algunos bienes para retener el pago del adeudo.", font=(
            'Arial', 11), fg="#000000", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        self.ventana.mainloop()