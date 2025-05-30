class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.habitos = []

    def adicionar_habito(self, habito):
        self.habitos.append(habito)

    def remover_habito(self, nome):
        self.habitos = [h for h in self.habitos if h.nome != nome]

    def listar_habitos(self):
        return self.habitos
