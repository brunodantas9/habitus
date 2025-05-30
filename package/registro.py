from datetime import datetime

class Registro:
    def __init__(self, habito, data=None):
        self.habito = habito
        self.data = data if data else datetime.today().date()
