class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    def miinus(self, arvo):
        self.tulos -= arvo

    def plus(self, arvo):
        self.tulos += arvo

    def nollaa(self):
        self.tulos = 0

    def kumoa(self):
        temp = self.tulos
        self.tulos = self.edellinen
        self.edellinen = temp

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo

