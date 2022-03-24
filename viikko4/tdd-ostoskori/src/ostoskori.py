from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = {}
        self._hinta = 0
        self._maara = 0
        self.ostoslista = []

    def tavaroita_korissa(self):
        return self._maara

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() not in self._ostoskori:
            self._ostoskori[lisattava.nimi()] = Ostos(lisattava)
        else:
            self._ostoskori[lisattava.nimi()].muuta_lukumaaraa(1)
        self._hinta += lisattava.hinta()
        self._maara += 1


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):

        for ostos in self._ostoskori.values():
            self.ostoslista.append(ostos)
        return self.ostoslista