from janela_principal import Janela_princial
from banco_de_dados_simulado import Bd_Simulado


class Controle:
    def __init__(self):
        self.bd = Bd_Simulado()
        self.bd.carregar_carros()
        self.bd.car_compradores()
        self.bd.car_vendedores()
        self.jn = Janela_princial(self)
        self.jn.mainloop()
