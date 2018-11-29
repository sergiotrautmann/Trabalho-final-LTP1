from tkinter import *
from model import Comprador
from tkinter import messagebox


class Terceira_janela(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Comprador')
        self.geometry('400x250+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=6, column=0, padx=40, pady=30)

        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=8, column=1, columnspan=3, stick=S, pady=20)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var). \
            grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome'). \
            grid(row=1, column=1, padx=1, pady=1)

        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var). \
            grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF'). \
            grid(row=2, column=1, padx=1, pady=1)


    def add_comp(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        c = Comprador(nome, cpf)
        self.control.bd.add_comprador(c)
        messagebox.showinfo('Comprador', f'{nome} foi adicionado.')


    def destroy(self):
        self.control.bd.save_comprador()
        super().destroy()