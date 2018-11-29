class Carro:
    def __init__(self, modelo, marca, ano, estado, preco, placa, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.estado = estado
        self.placa = placa
        self.cor = cor

    def get_modelo(self):
        return self.modelo
    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_estado(self):
        return self.estado

    def get_preco(self):
        return self.preco

    def get_placa(self):
        return self.placa

    def get_cor(self):
        return self.cor

    def get_dados(self):
        return self.modelo, self.ano, self.estado, self.preco, self.placa, self.cor

class Comprador:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_dados(self):
        return self.nome, self.cpf


class Vendedor:
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_matricula(self):
        return self.matricula

    def get_dados(self):
        return self.nome, self.cpf, self.matricula