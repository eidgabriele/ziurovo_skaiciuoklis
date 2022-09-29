class Filmas():
    def __init__(self, pavadinimas, metai, trukme, salis):
        self.pavadinimas = pavadinimas
        self.metai = metai
        self.trukme = trukme
        self.salis = salis

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
            if isinstance(irasas, Filmas):
                print(irasas.pavadinimas, irasas.metai, irasas.trukme, irasas.salis)
            elif isinstance(irasas, Serialas):
                print(irasas.pavadinimas, irasas.metai, irasas.trukme, irasas.salis, irasas.sezonai, irasas.serijos)
    
    def gauti_filma_seriala(self):
        pass

class Ziurovas():
    ziurovo_sarasas = []

    def __init__(self, vardas):
        self.vardas = vardas


kolekcija = Kolekcija()

kolekcija.prideti_filma("Lawrence of Arabia", 1962, 218, "UK")
kolekcija.prideti_filma("Everything Everywhere All at Once", 2022, 139, "USA")
kolekcija.prideti_seriala("The Office", 2005, 22, "USA", 9, 6)
kolekcija.prideti_seriala("Cowboy Bebop", 1998, 24, "Japan", 1, 26)

kolekcija.spausdinamas_katalogas()