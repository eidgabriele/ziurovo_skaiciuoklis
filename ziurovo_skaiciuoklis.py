import pickle
from tkinter import *

class Filmas():
    def __init__(self, pavadinimas, metai, trukme, salis):
        self._pavadinimas = pavadinimas
        self.metai = metai
        self._trukme = trukme
        self.salis = salis

    def __str__(self):
        return f"{self.pavadinimas}, {self.metai}, {self.trukme}min, {self.salis}"

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

    def __str__(self):
        return f"{self.pavadinimas}, {self.metai}, {self.trukme}min, {self.salis}, {self.sezonai}-as sezonas, {self.serijos}-os serijos"

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
         

    def saugoti_kataloga(self, failo_pavadinimas):
        with open('data/'+failo_pavadinimas+'.pkl', 'wb') as failas:
            pickle.dump(self.katalogas, failas)

    def uzkrauti_kataloga(self, failo_pavadinimas):
        with open('data/'+failo_pavadinimas+'.pkl', 'rb') as failas:
            self.katalogas = pickle.load(failas)
        return self.katalogas

    def itraukti_filma_is_kolekcijos(self, kolekcija, filmo_pavadinimas):
        for irasas in kolekcija:
            if filmo_pavadinimas == irasas.pavadinimas:
                self.katalogas.append(irasas)

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


def uzdaryti():
    langas.destroy()

def rodyti_kataloga():
    saraso_laukas.delete(0, END)
    saraso_laukas.insert(END, *kolekcija.katalogas)

def rodyti_ziurova():
    saraso_laukas.delete(0, END)
    saraso_laukas.insert(END, *ziurovas.katalogas)

def kursoriaus_reiksme():
    statusas["text"]=saraso_laukas.curselection()

kolekcija = Kolekcija()
ziurovas = Kolekcija()


kolekcija.uzkrauti_kataloga("kolekcija")
# ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas,"Cowboy Bebop")
# ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas,"Lawrence of Arabia")
# ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas, "Mad Men")
# ziurovas.itraukti_filma_is_kolekcijos(kolekcija.katalogas, "Constantine")
# ziurovas.saugoti_kataloga("ziurovas")
ziurovas.uzkrauti_kataloga("ziurovas")
ziurovas.spausdinamas_katalogas()


langas = Tk()
langas.geometry("550x400")
pasirinkciu_freimas = Frame(langas)
saraso_freimas = Frame(langas)
statuso_freimas = Frame(langas)

langas.grid_rowconfigure(1, weight=1)
langas.grid_columnconfigure(0, weight=1)



statuso_freimas.grid(row=3, column=0, padx=5, pady=5)
statusas = Label(langas, text="cia bus statuso pranesimai", bd=2, relief=SUNKEN, anchor=W)
statusas.grid(row=6, column=0, sticky=W+E)

saraso_freimas.grid(row=2,  column=0,  padx=10,  pady=5)
scrollbaras = Scrollbar(saraso_freimas)
saraso_laukas = Listbox(saraso_freimas, width=85, height=8, yscrollcommand=scrollbaras.set)
scrollbaras.config(command=saraso_laukas.yview)
scrollbaras.grid(row=0, column=1, sticky=NSEW)
saraso_laukas.grid(row=0,column=0, sticky=NSEW)
# saraso_laukas.get(saraso_laukas.curselection())


pasirinkciu_freimas.grid(row=0,  column=0,  padx=10,  pady=5)
m_uzkrauti_visa_kolekcija = Button(pasirinkciu_freimas, text="Kolekcija", command=rodyti_kataloga)
m_uzkrauti_visa_kolekcija.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
m_uzkrauti_ziurovo_kataloga = Button(pasirinkciu_freimas, text="Ziurovo katalogas", command= rodyti_ziurova)
m_uzkrauti_ziurovo_kataloga.grid(row=1, column=1, padx=10, pady=5)
m_iseiti = Button(pasirinkciu_freimas, text="Iseiti", command=uzdaryti)
m_iseiti.grid(row=1, column=2, padx=10, pady=5)
m_ivesti = Button(pasirinkciu_freimas, text="ivesti", command=kursoriaus_reiksme)
m_ivesti.grid(row=2, column=2, padx=10, pady=5)




langas.mainloop()

