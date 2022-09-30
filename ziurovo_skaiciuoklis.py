import pickle

class Filmas():
    def __init__(self, pavadinimas, metai, trukme, salis):
        self._pavadinimas = pavadinimas
        self.metai = metai
        self._trukme = trukme
        self.salis = salis

    @property
    def trukme(self):
        return self._trukme

    @property
    def pavadinimas(self):
        return self._pavadinimas

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

    def saugoti_kataloga(self):
        with open('data/katalogas.pkl', 'wb') as failas:
            pickle.dump(self.katalogas, failas)

    def uzkrauti_kataloga(self):
        with open('data/katalogas.pkl', 'rb') as failas:
            self.katalogas = pickle.load(failas)
        return self.katalogas

    def itraukti_filma_is_kolekcijos(self, kolekcija, filmo_pavadinimas):
        for irasas in kolekcija:
            if filmo_pavadinimas == irasas.pavadinimas:
                self.katalogas.append(irasas)

    def spausdinti_ziurovo_sarasa(self):
        for irasas in self.katalogas:
            print(irasas.pavadinimas)

    def skaiciuoti_ziurovo_laika(self):
        praziuretas_laikas = 0
        for irasas in self.katalogas:
            if isinstance(irasas, Serialas):
                praziuretas_laikas += irasas.serijos*irasas.trukme
            else:
                praziuretas_laikas += irasas.trukme
        valandos = praziuretas_laikas // 60
        minutes = praziuretas_laikas - (valandos*60)
        print(f"Ziureta {valandos} valandu,{minutes} minuciu")

    def skaiciuoti_ziurovo_sarasa(self):
        filmai = 0
        serialai = 0 
        serijos = 0
        for irasas in self.katalogas:
            if isinstance(irasas, Serialas):
                serialai += 1
                serijos += irasas.serijos
            elif isinstance(irasas, Filmas):
                filmai +=1
        print(f"Matyti {filmai} filmai, {serialai} serialai (viso {serijos} serijos)")

    def saugoti_ziurovo_sarasa(self):
        pass

    

kolekcija = Kolekcija()
ziurovas = Kolekcija()

# kolekcija.prideti_filma("Lawrence of Arabia", 1962, 218, "UK")
# kolekcija.prideti_filma("Everything Everywhere All at Once", 2022, 139, "USA")
# kolekcija.prideti_seriala("The Office", 2005, 22, "USA", 9, 6)
# kolekcija.prideti_seriala("Cowboy Bebop", 1998, 24, "Japan", 1, 26)
kolekcija.uzkrauti_kataloga()
kolekcija.spausdinamas_katalogas()

ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas,"Cowboy Bebop")
ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas,"Lawrence of Arabia")
ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas, "Mad Men")
ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas, "Constantine")
ziurovas.spausdinti_ziurovo_sarasa()
ziurovas.skaiciuoti_ziurovo_laika()
ziurovas.skaiciuoti_ziurovo_sarasa()
# kolekcija.saugoti_kataloga()



