from tkinter import *


class Nota_fiscal(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Nota de Venda')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()

        file = open('Nota de Venda.txt', 'r')
        self.text = Text(self, width=50, height=20)
        self.text.insert('1.0', file.read())
        self.text.grid(row=0, column=0)

        Button(self, text='Fechar Janela', command=super().destroy).grid(row=2, column=0, pady=25)