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

class Ziurovas():
    ziurovo_sarasas = []

    def __init__(self, vardas):
        self.vardas = vardas