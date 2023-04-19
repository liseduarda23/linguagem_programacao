class Estudante:
    def __init__(self, nome, matricula,  prova01, prova02, trabalho01):
      self.nome = nome
      self.matricula = matricula
      self.prova01 = prova01
      self.prova02 = prova02
      self.trabalho01 = trabalho01

    def media(self):
      media = 2.5 * self.prova01 + 2.5 * self.prova02 + 2 * self.trabalho01 / 7
      print(media)