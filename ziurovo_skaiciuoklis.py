

class Filmas():
    def __init__(self, pavadinimas, metai, trukme, salis):
        self.pavadinimas = pavadinimas
        self.metai = metai
        self.trukme = trukme
        self.salis = salis

    def get_trukme(self):
        return self.trukme

class Serialas(Filmas):
    def __init__(self, pavadinimas, metai, trukme, salis, sezonai, serijos):
        super().__init__(pavadinimas, metai, trukme, salis)
        self.sezonai = sezonai
        self.serijos = serijos


class Kolekcija():
    katalogas = []

    def prideti_filma(self, pavadinimas, metai, trukme, salis):
        filmas = Filmas(pavadinimas, metai, trukme, salis)
        self.katalogas.append(filmas)

    def prideti_seriala(self, pavadinimas, metai, trukme, salis, sezonai, serijos):
        serialas = Serialas(pavadinimas, metai, trukme, salis, sezonai, serijos)
        self.katalogas.append(serialas)

    def spausdinamas_katalogas(self):
        for irasas in self.katalogas:
            if isinstance(irasas, Serialas):
                print(irasas.pavadinimas, irasas.metai, irasas.trukme, irasas.salis, irasas.sezonai, irasas.serijos)
            elif isinstance(irasas, Filmas):
                print(irasas.pavadinimas, irasas.metai, irasas.trukme, irasas.salis)


class Ziurovas():

    ziurovo_sarasas = []

    def __init__(self, vardas):
        self.vardas = vardas

    def itraukti_filma(self, kolekcija, filmo_pavadinimas):
        for irasas in kolekcija:
            if filmo_pavadinimas == irasas.pavadinimas:
                self.ziurovo_sarasas.append(irasas)

    def spausdinti_ziurovo_sarasa(self):
        for irasas in self.ziurovo_sarasas:
            print(irasas.pavadinimas)

    def skaiciuoti_ziurovo_laika(self):
        pass

    def skaiciuoti_ziurovo_sarasa(self):
        pass

    def saugoti_ziurovo_sarasa(self):
        pass

kolekcija = Kolekcija()

kolekcija.prideti_filma("Lawrence of Arabia", 1962, 218, "UK")
kolekcija.prideti_filma("Everything Everywhere All at Once", 2022, 139, "USA")
kolekcija.prideti_seriala("The Office", 2005, 22, "USA", 9, 6)
kolekcija.prideti_seriala("Cowboy Bebop", 1998, 24, "Japan", 1, 26)

kolekcija.spausdinamas_katalogas()

ziurovas = Ziurovas("Jonas")
ziurovas.itraukti_filma(kolekcija.katalogas,"Cowboy Bebop")
ziurovas.itraukti_filma(kolekcija.katalogas,"Lawrence of Arabia")
ziurovas.spausdinti_ziurovo_sarasa()

