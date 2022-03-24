from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = {}
        self._hinta = 0
        self._maara = 0
        self._ostoslista = []

    def tavaroita_korissa(self):
        return self._maara

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() not in self._ostoskori:
            self._ostoskori[lisattava.nimi()] = Ostos(lisattava)
        else:
            self._ostoskori[lisattava.nimi()].muuta_lukumaaraa(1)

        self._hinta += lisattava.hinta()
        self._maara += 1

    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi():
            self._ostoskori[poistettava.nimi()].muuta_lukumaaraa(-1)
            if self._ostoskori[poistettava.nimi()].lukumaara() == 0:
                del self._ostoskori[poistettava.nimi()]

        self._hinta -= poistettava.hinta()
        self._maara -= 1

    def tyhjenna(self):
        self._ostoskori.clear()
        self._ostoslista.clear()
        self._maara = 0
        self._hinta = 0

    def ostokset(self):
        for ostos in self._ostoskori.values():
            self._ostoslista.append(ostos)
        return self._ostoslista