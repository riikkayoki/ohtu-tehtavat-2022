from summa import Summa
from miinus import Miinus
from nollaus import Nollaus
from kumoaminen import Kumoaminen

class Komentotehdas:
    def __init__(self, io):
        self.io = io
        self.komennot = {
            1: Summa(io),
            2: Miinus(io),
            3: Nollaus(io),
            4: Kumoaminen(io),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]
        return None