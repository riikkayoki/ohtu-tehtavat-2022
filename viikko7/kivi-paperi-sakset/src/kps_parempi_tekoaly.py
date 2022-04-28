from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


from kps import KPS
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPS):
    def __init__(self, muisti):
        self._tekoaly = TekoalyParannettu(muisti)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tekoaly_siirto
