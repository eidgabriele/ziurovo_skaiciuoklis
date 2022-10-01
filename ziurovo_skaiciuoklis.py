import pickle
from tkinter import *
from tkinter import ttk

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
        statusas["text"] = f"{pavadinimas} buvo itrauktas i kolekcija."

    def prideti_seriala(self, pavadinimas, metai, trukme, salis, sezonai, serijos):
        serialas = Serialas(pavadinimas, metai, trukme, salis, sezonai, serijos)
        self.katalogas.append(serialas)
        statusas["text"] = f"{pavadinimas} buvo itrauktas i kolekcija."

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
    kolekcijos_pasirinkciu_freimas.tkraise()
    kolekcijos_pasirinkciu_freimas.grid(row=1,  column=0,  padx=10,  pady=5)
    kolekcijos_pasirinkciu_freimas.config(background="white")
    kolekcijos_pasirinkciu_freimas.place(height=125, width=510, x=15, y=60)
    saraso_laukas.delete(0, END)
    saraso_laukas.insert(END, *kolekcija.katalogas)

def rodyti_ziurova():
    ziurovo_pasirinkciu_freimas.tkraise()
    ziurovo_pasirinkciu_freimas.grid(row=1,  column=0,  padx=10,  pady=5)
    ziurovo_pasirinkciu_freimas.config(background="white")
    ziurovo_pasirinkciu_freimas.place(height=120, width=510, x=15, y=60)
    saraso_laukas.delete(0, END) 
    saraso_laukas.insert(END, *ziurovas.katalogas)
    
def kursoriaus_reiksme():
    statusas["text"]=saraso_laukas.curselection()

    
def serialai_off():
    e_sezonas.configure(state=DISABLED)
    e_sezonas.update()
    e_serijos.configure(state=DISABLED)
    e_serijos.update()
    statusas["text"]="off"

def serialai_on():
    e_sezonas.configure(state=NORMAL) 
    e_sezonas.update()
    e_serijos.configure(state=NORMAL)
    e_serijos.update()
    statusas["text"]="on"

def kolekcijos_ivedimas():
    print(radio_button.get())
    try:
        pavadinimas = str(e_pavadinimas.get())
        metai = int(e_metai.get())
        trukme = int(e_trukme.get())
        salis = str(e_salis.get())
        if radio_button.get()==1:
            sezonas = int(e_sezonas.get())
            serijos = int(e_serijos.get())
    except ValueError as e:
        print(e)
        statusas["text"] = f"Ivesta netinkama reiksme: {e}"
    else:
        if radio_button.get()==0:
            kolekcija.prideti_filma(pavadinimas, metai, trukme, salis)
            statusas["text"]= f"Filmas {pavadinimas} buvo itrauktas i kolekcija"
        elif radio_button.get()==1:
            kolekcija.prideti_seriala(pavadinimas, metai, trukme, salis, sezonas, serijos)
            statusas["text"]= f"Serialas {pavadinimas} buvo itrauktas i kolekcija"


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


# grafines sasajos pagr langai freimai
langas = Tk()
langas.geometry("550x400")
pasirinkciu_freimas = Frame(langas)
kolekcijos_pasirinkciu_freimas = Frame(langas)
ziurovo_pasirinkciu_freimas = Frame(langas)
saraso_freimas = Frame(langas)
statuso_freimas = Frame(langas)
langas.grid_rowconfigure(1, weight=1)
langas.grid_columnconfigure(0, weight=1)


#pranesimu juosta
statuso_freimas.grid(row=3, column=0, padx=5, pady=5)
statusas = Label(langas, text="cia bus statuso pranesimai", bd=2, relief=SUNKEN, anchor=W)
statusas.grid(row=6, column=0, sticky=W+E)
# saraso listboxo elementai
saraso_freimas.grid(row=2,  column=0,  padx=10,  pady=5)
scrollbaras = Scrollbar(saraso_freimas)
saraso_laukas = Listbox(saraso_freimas, width=85, height=8, yscrollcommand=scrollbaras.set)
scrollbaras.config(command=saraso_laukas.yview)
scrollbaras.grid(row=0, column=1, sticky=NSEW)
saraso_laukas.grid(row=0,column=0, sticky=NSEW)

# virsutine mygtuku juosta
pasirinkciu_freimas.grid(row=0,  column=0,  padx=10,  pady=5)
m_uzkrauti_visa_kolekcija = Button(pasirinkciu_freimas, text="Kolekcija", command=rodyti_kataloga)
m_uzkrauti_visa_kolekcija.grid(row=1, column=0, padx=10, pady=5, sticky=W)
m_uzkrauti_ziurovo_kataloga = Button(pasirinkciu_freimas, text="Ziurovo katalogas", command= rodyti_ziurova)
m_uzkrauti_ziurovo_kataloga.grid(row=1, column=1, padx=10, pady=5)
m_iseiti = Button(pasirinkciu_freimas, text="Iseiti", command=uzdaryti)
m_iseiti.grid(row=1, column=2, padx=10, pady=5)
m_ivesti = Button(pasirinkciu_freimas, text="ivesti", command=kursoriaus_reiksme)
m_ivesti.grid(row=1, column=3, padx=10, pady=5)

l_pasirinkti = Label(kolekcijos_pasirinkciu_freimas, text="Prideti nauja", bg="white")
l_pasirinkti.grid(row=0,  column=0,  padx=10,  pady=5)
m_ziurovo_kolekcija_prideti = Button(kolekcijos_pasirinkciu_freimas, text="Prideti i sarasa", command=kolekcijos_ivedimas)
m_ziurovo_kolekcija_prideti.grid(row=0, column=4, padx=10, pady=5, sticky=E)

# filmu ivedimo elementai
l_pavadinimas = Label(kolekcijos_pasirinkciu_freimas, text="Pavadinimas", bg= "white")
l_pavadinimas.grid(row=1, column=0,sticky=E)
e_pavadinimas = Entry(kolekcijos_pasirinkciu_freimas)
e_pavadinimas.grid(row=1, column=1)
l_metai = Label(kolekcijos_pasirinkciu_freimas, text="Metai", bg= "white")
l_metai.grid(row=2, column=0, sticky= E)
e_metai = Entry(kolekcijos_pasirinkciu_freimas)
e_metai.grid(row=2, column=1)
l_trukme = Label(kolekcijos_pasirinkciu_freimas, text="Trukme", bg= "white")
l_trukme.grid(row=3, column=0, sticky= E)
e_trukme = Entry(kolekcijos_pasirinkciu_freimas)
e_trukme.grid(row=3, column=1)
l_salis = Label(kolekcijos_pasirinkciu_freimas, text="Salis", bg= "white")
l_salis.grid(row=4, column=0, sticky= E)
e_salis = Entry(kolekcijos_pasirinkciu_freimas)
e_salis.grid(row=4, column=1)
l_sezonas = Label(kolekcijos_pasirinkciu_freimas, text="Sezonas")
l_sezonas.grid(row=2, column=3, sticky=E)
e_sezonas = Entry(kolekcijos_pasirinkciu_freimas)  
e_sezonas.grid(row=2, column=4)
e_sezonas.configure(state=DISABLED)
l_serijos = Label(kolekcijos_pasirinkciu_freimas, text="Serijos")
l_serijos.grid(row=3, column=3, sticky=E)
e_serijos = Entry(kolekcijos_pasirinkciu_freimas)
e_serijos.grid(row=3, column=4)
e_serijos.configure(state=DISABLED)
radio_button = IntVar()
m_filmas = Radiobutton(kolekcijos_pasirinkciu_freimas, text="Filmas", variable=radio_button, value="0", bg= "white", command=serialai_off)
m_filmas.grid(row=0, column=1, pady=5, sticky=W)
m_serialas = Radiobutton(kolekcijos_pasirinkciu_freimas, text="Serialas", variable=radio_button, value="1", bg= "white", command=serialai_on)
m_serialas.grid(row=0, column=2, pady=5, sticky=W)

langas.mainloop()

