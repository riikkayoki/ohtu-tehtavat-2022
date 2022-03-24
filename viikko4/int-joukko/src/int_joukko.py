OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=OLETUSKAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kasvatuskoko = kasvatuskoko
        self.kapasiteetti = kapasiteetti
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluuko_joukkoon(self, n):

        if self.lukujono.count(n) == 0:
            return False
        return True

    def lisaa_alkio(self, n):

        if not self.kuuluuko_joukkoon(n):
            if self.alkioiden_lkm == len(self.lukujono):
                self.lukujono = self.lukujono + [0] * self.kasvatuskoko
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        return False

    def poista_alkio(self, n):
        if self.kuuluuko_joukkoon(n):
            self.lukujono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_taulukko(self, a, b):
        for alkio in range(0, len(a)):
            b[alkio] = a[alkio]

    def palauta_alkioiden_lkm(self):
        return self.alkioiden_lkm

    def muuta_lukujonoksi(self):
        return [alkio for alkio in self.lukujono if alkio != 0]

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.muuta_lukujonoksi()
        b_taulu = b.muuta_lukujonoksi()

        for alkio in a_taulu:
            joukko.lisaa_alkio(alkio)

        for alkio in b_taulu:
            joukko.lisaa_alkio(alkio)

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.muuta_lukujonoksi()
        b_taulu = b.muuta_lukujonoksi()

        for i in a_taulu:
            for j in b_taulu:
                if i == j:
                    joukko.lisaa_alkio(j)
        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.muuta_lukujonoksi()
        b_taulu = b.muuta_lukujonoksi()

        for alkio in a_taulu:
            joukko.lisaa_alkio(alkio)

        for alkio in b_taulu:
            joukko.poista_alkio(alkio)

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            tuotos += str(self.lukujono[i]) + ", "
        tuotos += str(self.lukujono[self.alkioiden_lkm - 1])
        tuotos += "}"
        return tuotos
