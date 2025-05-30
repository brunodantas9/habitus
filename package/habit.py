from datetime import date, timedelta

class Habito:
    def __init__(self, nome, descricao, categoria, periodicidade):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.periodicidade = periodicidade
        self.registros = []

    def registrar(self, data):
        if data not in self.registros:
            self.registros.append(data)

    def progresso(self):
        return len(self.registros)


class HabitoDiario(Habito):
    def progresso(self):
        hoje = date.today()
        dias_mes = [d for d in self.registros if d.month == hoje.month and d.year == hoje.year]
        return len(set(dias_mes))


class HabitoSemanal(Habito):
    def progresso(self):
        hoje = date.today()
        inicio_semana = hoje - timedelta(days=hoje.weekday())
        dias_semana = [d for d in self.registros if d >= inicio_semana]
        return len(set(dias_semana))


class HabitoMensal(Habito):
    def progresso(self):
        hoje = date.today()
        meses = [d.month for d in self.registros if d.year == hoje.year]
        return len(set(meses))

