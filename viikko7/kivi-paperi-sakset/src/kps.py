from tuomari import Tuomari

class KPS:

    def pelaa(self):
        tuomari = Tuomari()
        ensimmaisen_siirto = self._ensimmaisen_siirto()
        toisen_siirto = self._toisen_siirto(ensimmaisen_siirto)
        print(f'Tietokone valitsi: {toisen_siirto}')

        while self._onko_ok_siirto(ensimmaisen_siirto) \
            and self._onko_ok_siirto(toisen_siirto):

            tuomari.kirjaa_siirto(ensimmaisen_siirto, toisen_siirto)
            print(tuomari)
            ensimmaisen_siirto = self._ensimmaisen_siirto()
            toisen_siirto = self._toisen_siirto(ensimmaisen_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"