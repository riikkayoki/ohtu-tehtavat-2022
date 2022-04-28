from komentotehdas import Komentotehdas

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        if vastaus.endswith("a"):
            komento = Komentotehdas.kaksinpeli()
            komento().pelaa()
        elif vastaus.endswith("b"):
            komento = Komentotehdas.yksinpeli()
            komento().pelaa()
        elif vastaus.endswith("c"):
            komento = Komentotehdas.haastava_yksinpeli(10)
            komento.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
