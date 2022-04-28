from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Komentotehdas:
    @staticmethod
    def kaksinpeli():
        return KPSPelaajaVsPelaaja
    @staticmethod
    def yksinpeli():
        return KPSTekoaly
    @staticmethod
    def haastava_yksinpeli(muisti):
        return KPSParempiTekoaly(muisti)
