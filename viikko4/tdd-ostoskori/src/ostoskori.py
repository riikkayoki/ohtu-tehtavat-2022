from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._hinta = 0


    def tavaroita_korissa(self):
        return len(self._ostoskori)

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        self._ostoskori.append(Ostos(lisattava))
        self._hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
