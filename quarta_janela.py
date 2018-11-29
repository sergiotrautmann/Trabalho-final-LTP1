from tkinter import *
from model import Vendedor
from tkinter import messagebox


class Quarta_janela(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Vendedor')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=10, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=40, pady=10)
        Label(self, text='').grid(row=5, column=0, padx=10, pady=20)

        self.btn_add = Button(self, text='Adicionar Vendedor', command=self.add_vend).\
            grid(row=4, column=1, columnspan=3, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover Vendedor', command=self.rmv_vend).\
            grid(row=9, column=1, columnspan=3, pady=10, stick=S)
        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=10, column=1, columnspan=3, stick=S, pady=20)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).\
            grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome').\
            grid(row=1, column=1, padx=1, pady=1)

        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var).\
            grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF').\
            grid(row=2, column=1, padx=1, pady=1)

        self.entry_mat_var = StringVar()
        self.entry_mat = Entry(self, textvariable=self.entry_mat_var).\
            grid(row=3, column=3, padx=1, pady=1)
        self.lbl_mat = Label(self, text='Matrícula').\
            grid(row=3, column=1, padx=1, pady=1)

        self.entry_mat_var2 = StringVar()
        self.entry_mat2 = Entry(self, textvariable=self.entry_mat_var2). \
            grid(row=6, column=3, padx=1, pady=1)
        self.lbl_mat2 = Label(self, text='Matrícula'). \
            grid(row=6, column=1, padx=1, pady=1)

    def add_vend(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        matricula = self.entry_mat_var.get()
        v = Vendedor(nome, cpf, matricula)
        self.control.bd.add_vendedor(v)
        messagebox.showinfo('Vendedor', f'{nome} foi adicionado.')

    def rmv_vend(self):
        matricula = self.entry_mat_var2.get()
        remover = None
        for vend in self.control.bd.car_vendedores():
            if matricula == vend.get_matricula():
                if messagebox.askyesno\
                            ('Excluir', f'Tem ceteza que deseja excluir o vendedor {vend.get_nome()}?') is False:
                    return None
                remover = self.control.bd.remover_vendedor(vend)
                messagebox.showinfo('Vendedor', f'{vend.get_nome()} foi removido.')
        if remover is None:
            messagebox.showerror('Vendedor', 'Não há vendedor cadastrado com esta matrícula')

    def destroy(self):
        self.control.bd.save_vendedor()
        super().destroy()