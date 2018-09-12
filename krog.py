import tkinter as tk
import model

VELIKOST = model.VELIKOST
ROB = model.ROB
A = model.A
B = model.B
ZACETNA = model.ZACETNA


class Krog:
    def __init__(self, okno):
        self.igra = model.Igra()
        self.okno = okno
        self.igralna_plosca = tk.Canvas(
            width=10 * A + 2 * ROB,
            height=10 * A + 2 * ROB
        )
        self.zgoraj = tk.Frame(self.okno)
        self.spodaj = tk.Frame(self.okno)
        
        self.zgoraj.pack()
        self.igralna_plosca.pack()
        self.spodaj.pack()

        self.navodila = tk.Label(self.zgoraj, text=self.igra.navodila,
                                 height=2, font=('TkDefaultFont', 12))
        self.stevec_poskusov = tk.Label(self.spodaj, text=self.igra.poskusi,
                              font=('TkDefaultFont', 12))

        self.navodila.grid(row=0, column=0)
        self.stevec_poskusov.grid(row=0, column=0)
        
        self.okno.bind('<Key>', self.obdelaj_tipko)
        self.osvezi_prikaz()


    def obdelaj_tipko(self, event):
        #na koncu
        if self.igra.krog.lokacija == [ROB + 9 * A + B, ROB + 9 * A + B]:
            self.igra.zacni_ponovno()
            self.osvezi_prikaz()
        #gor
        elif event.keysym == self.igra.GOR:
            if self.igralna_plosca.find_overlapping(
                self.igra.krog.lokacija[0] + 0.5 * VELIKOST,
                self.igra.krog.lokacija[1] - B - VELIKOST,
                self.igra.krog.lokacija[0],
                self.igra.krog.lokacija[1] - 1
                ) != ():
                if self.igra.krog.lokacija == [
                    ROB + 3 * A + B, ROB + 9 * A + B]:
                    self.igra.naloga_4()
                    self.igra.krog.premakni_se(model.GOR)
                    self.osvezi_prikaz()
                else:
                    self.igra.trk()
                    self.osvezi_prikaz()        
            else:
                self.igra.krog.premakni_se(model.GOR)
                self.osvezi_prikaz()
        #dol
        elif event.keysym == self.igra.DOL:
            if self.igralna_plosca.find_overlapping(
                self.igra.krog.lokacija[0] + 0.5 * VELIKOST,
                self.igra.krog.lokacija[1] + 2 * VELIKOST,
                self.igra.krog.lokacija[0],
                self.igra.krog.lokacija[1] + VELIKOST + B
                ) != ():
                if self.igra.krog.lokacija == [
                    ROB + 6 * A + B, ROB + 2 * A + B]:
                    self.igra.naloga_2()
                    self.igra.krog.premakni_se(model.DOL)
                    self.osvezi_prikaz()
                else:
                    self.igra.trk()
                    self.osvezi_prikaz()
            else:
                self.igra.krog.premakni_se(model.DOL)
                self.osvezi_prikaz()
        #levo
        elif event.keysym == self.igra.LEVO:
            if self.igralna_plosca.find_overlapping(
                self.igra.krog.lokacija[0] - VELIKOST,
                self.igra.krog.lokacija[1]  + 0.5 * VELIKOST,
                self.igra.krog.lokacija[0] - 1,
                self.igra.krog.lokacija[1]
                ) != ():
                if self.igra.krog.lokacija == [
                    ROB + 3 * A + B, ROB + 3 * A + B]:
                    self.igra.naloga_3()
                    self.igra.krog.premakni_se(model.LEVO)
                    self.osvezi_prikaz()
                else:
                    self.igra.trk()
                    self.osvezi_prikaz()
            else:
                self.igra.krog.premakni_se(model.LEVO)
                self.osvezi_prikaz()
        #desno
        elif event.keysym == self.igra.DESNO:
            if self.igralna_plosca.find_overlapping(
                self.igra.krog.lokacija[0] + 2 * VELIKOST,
                self.igra.krog.lokacija[1] + 0.5 * VELIKOST,
                self.igra.krog.lokacija[0] + VELIKOST + 1,
                self.igra.krog.lokacija[1]
                ) != ():
                if self.igra.krog.lokacija == [
                    ROB + 4 * A + B, ROB + 2 * A + B]:
                    self.igra.naloga_1()
                    self.igra.krog.premakni_se(model.DESNO)
                    self.osvezi_prikaz()
                #za konec igre
                elif self.igra.krog.lokacija == [
                    ROB + 8 * A + B, ROB + 9 * A + B]:
                    self.igra.krog.premakni_se(model.DESNO)
                    self.igra.konec()
                    self.osvezi_prikaz()
                else:
                    self.igra.trk()
                    self.osvezi_prikaz()
            else:
                self.igra.krog.premakni_se(model.DESNO)
                self.osvezi_prikaz()


    def osvezi_prikaz(self):
        #pobriši
        self.igralna_plosca.delete('all')
        #navodila
        self.navodila.configure(text=self.igra.navodila)
        self.stevec_poskusov.configure(text=self.igra.poskusi)
        #cilj
        self.igralna_plosca.create_text(ROB + 9.5 * A, ROB + 9.5 * A,
                                        text='CILJ')
        self.igralna_plosca.create_oval(ROB + 9 * A + B,
                                        ROB + 9 * A + B,
                                        ROB + 9 * A + B + VELIKOST,
                                        ROB + 9 * A + B + VELIKOST)
        #nariše točke z nalogami
        self.igralna_plosca.create_oval(ROB + 5 * A + B + 8,
                                        ROB + 2 * A + B + 8,
                                        ROB + 5 * A + B + 22,
                                        ROB + 2 * A + B + 22,
                                        fill='yellow')
        self.igralna_plosca.create_oval(ROB + 6 * A + B + 8,
                                        ROB + 3 * A + B + 8,
                                        ROB + 6 * A + B + 22,
                                        ROB + 3 * A + B + 22,
                                        fill='orange')
        self.igralna_plosca.create_oval(ROB + 2 * A + B + 8,
                                        ROB + 3 * A + B + 8,
                                        ROB + 2 * A + B + 22,
                                        ROB + 3 * A + B + 22,
                                        fill='red')
        self.igralna_plosca.create_oval(ROB + 3 * A + B + 8,
                                        ROB + 8 * A + B + 8,
                                        ROB + 3 * A + B + 22,
                                        ROB + 8 * A + B + 22,
                                        fill='blue')
        #okvir
        self.igralna_plosca.create_rectangle(ROB, ROB, 10 * A + ROB,
                                             10 * A + ROB, width=2)
        #Labirint:
        #vodoravne črte
        self.igralna_plosca.create_line(ROB, ROB + 1 * A,
                                        ROB + 2 * A, ROB + 1 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 1 * A,
                                        ROB + 9 * A, ROB + 1 * A, width=2)
        self.igralna_plosca.create_line(ROB + 1 * A, ROB + 2 * A,
                                        ROB + 3 * A, ROB + 2 * A, width=2)
        self.igralna_plosca.create_line(ROB + 6 * A, ROB + 2 * A,
                                        ROB + 8 * A, ROB + 2 * A, width=2)
        self.igralna_plosca.create_line(ROB + 9 * A, ROB + 2 * A,
                                        ROB + 10 * A, ROB + 2 * A, width=2)
        self.igralna_plosca.create_line(ROB + 2 * A, ROB + 3 * A,
                                        ROB + 6 * A, ROB + 3 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 3 * A,
                                        ROB + 9 * A, ROB + 3 * A, width=2)
        self.igralna_plosca.create_line(ROB, ROB + 4 * A,
                                        ROB + 2 * A, ROB + 4 * A, width=2)
        self.igralna_plosca.create_line(ROB + 5 * A, ROB + 4 * A,
                                        ROB + 10 * A, ROB + 4 * A, width=2)
        self.igralna_plosca.create_line(ROB + 6 * A, ROB + 5 * A,
                                        ROB + 8 * A, ROB + 5 * A, width=2)
        self.igralna_plosca.create_line(ROB + 1 * A, ROB + 6 * A,
                                        ROB + 3 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB + 5 * A, ROB + 6 * A,
                                        ROB + 7 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 6 * A,
                                        ROB + 9 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB, ROB + 7 * A,
                                        ROB + 1 * A, ROB + 7 * A, width=2)
        self.igralna_plosca.create_line(ROB + 3 * A, ROB + 7 * A,
                                        ROB + 6 * A, ROB + 7 * A, width=2)
        self.igralna_plosca.create_line(ROB + 7 * A, ROB + 7 * A,
                                        ROB + 8 * A, ROB + 7 * A, width=2)
        self.igralna_plosca.create_line(ROB + 1 * A, ROB + 8 * A,
                                        ROB + 7 * A, ROB + 8 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 8 * A,
                                        ROB + 9 * A, ROB + 8 * A, width=2)
        self.igralna_plosca.create_line(ROB + 9 * A, ROB + 9 * A,
                                        ROB + 10 * A, ROB + 9 * A, width=2)
        #navpične črte
        self.igralna_plosca.create_line(ROB + 1 * A, ROB + 2 * A,
                                        ROB + 1 * A, ROB + 3 * A, width=2)
        self.igralna_plosca.create_line(ROB + 1 * A, ROB + 5 * A,
                                        ROB + 1 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB + 1 * A, ROB + 8 * A,
                                        ROB + 1 * A, ROB + 9 * A, width=2)
        self.igralna_plosca.create_line(ROB + 2 * A, ROB + 3 * A,
                                        ROB + 2 * A, ROB + 5 * A, width=2)
        self.igralna_plosca.create_line(ROB + 2 * A, ROB + 6 * A,
                                        ROB + 2 * A, ROB + 8 * A, width=2)
        self.igralna_plosca.create_line(ROB + 2 * A, ROB + 9 * A,
                                        ROB + 2 * A, ROB + 10 * A, width=2)
        self.igralna_plosca.create_line(ROB + 3 * A, ROB,
                                        ROB + 3 * A, ROB + 2 * A, width=2)
        self.igralna_plosca.create_line(ROB + 3 * A, ROB + 4 * A,
                                        ROB + 3 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB + 3 * A, ROB + 8 * A,
                                        ROB + 3 * A, ROB + 9 * A, width=2)
        self.igralna_plosca.create_line(ROB + 4 * A, ROB + 1 * A,
                                        ROB + 4 * A, ROB + 7 * A, width=2)
        self.igralna_plosca.create_line(ROB + 4 * A, ROB + 9 * A,
                                        ROB + 4 * A, ROB + 10 * A, width=2)
        self.igralna_plosca.create_line(ROB + 5 * A, ROB,
                                        ROB + 5 * A, ROB + 2 * A, width=2)
        self.igralna_plosca.create_line(ROB + 5 * A, ROB + 4 * A,
                                        ROB + 5 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB + 5 * A, ROB + 8 * A,
                                        ROB + 5 * A, ROB + 9 * A, width=2)
        self.igralna_plosca.create_line(ROB + 6 * A, ROB + 1 * A,
                                        ROB + 6 * A, ROB + 3 * A, width=2)
        self.igralna_plosca.create_line(ROB + 6 * A, ROB + 9 * A,
                                        ROB + 6 * A, ROB + 10 * A, width=2)
        self.igralna_plosca.create_line(ROB + 7 * A, ROB,
                                        ROB + 7 * A, ROB + 1 * A, width=2)
        self.igralna_plosca.create_line(ROB + 7 * A, ROB + 3 * A,
                                        ROB + 7 * A, ROB + 4 * A, width=2)
        self.igralna_plosca.create_line(ROB + 7 * A, ROB + 6 * A,
                                        ROB + 7 * A, ROB + 9 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 1 * A,
                                        ROB + 8 * A, ROB + 3 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 5 * A,
                                        ROB + 8 * A, ROB + 6 * A, width=2)
        self.igralna_plosca.create_line(ROB + 8 * A, ROB + 8 * A,
                                        ROB + 8 * A, ROB + 10 * A, width=2)
        self.igralna_plosca.create_line(ROB + 9 * A, ROB + 6 * A,
                                        ROB + 9 * A, ROB + 8 * A, width=2)
        #če bi imela datoteko s koordinatami, bi lahko uporabila formulo:
        #def narisi_labirint(dat):
            #with open(dat) as datot:
                #for i in datot:
                    #platno.create_line(eval(i), width=2)
        #vendar pa je v mojem primeru vseeno bolje imeti vse tu, saj iz datoteke
        #dobiš niz, ki ga potem ne moreŠ uporabiti za ustvarjanje črt,
        #tu pa so števila podana s konstantami, ki jih lahko še spreminjam.


        #nariši nov krog
        self.igralna_plosca.create_oval(
            self.igra.krog.lokacija[0],
            self.igra.krog.lokacija[1],
            self.igra.krog.lokacija[0] + VELIKOST,
            self.igra.krog.lokacija[1] + VELIKOST,
            fill=self.igra.krog.barva
        )
      

okno = tk.Tk()
moj_program = Krog(okno)
okno.mainloop()
