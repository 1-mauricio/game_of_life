class Roda:
    def __init__(self, fabricante, modelo, diametro):
        self.fabricante = fabricante
        self.modelo = modelo
        self.diametro = diametro

class Veiculo:
    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.rodas = []
    
    def acelerar(self, tempo, rpm):
        pass

    def adiciona_rodas(self, quantidade, diametro):
        for i in range(quantidade): self.rodas.append(Roda(self.fabricante, self.modelo, diametro))

carro = Veiculo("Ford", "KA", 2020)