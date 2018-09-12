
VELIKOST = 30#velikost kroga
ROB = 30#rob okoli labirinta
A = 50 #širina polj
B = 10 #odmik kroga od roba polja
GOR, DOL, LEVO, DESNO = 'gor', 'dol', 'levo', 'desno'
ZACETNA = ROB + B #začetna lokacija


class Krog:
    def __init__(self, lokacija, barva=None):
        self.lokacija = lokacija
        self.barva = barva


    def premakni_se(self, kam):
        if kam == GOR:
            self.lokacija[1] -= A
        elif kam == DOL:
            self.lokacija[1] += A
        elif kam == LEVO:
            self.lokacija[0] -= A
        elif kam == DESNO:
            self.lokacija[0] += A

    def spremeni_barvo(self):
        slovar = {None: 'yellow', 'yellow': 'orange',
                  'orange': 'red', 'red': 'blue'}
        for i in slovar:
            if self.barva == i:
                self.barva = slovar.get(i)
                break


class Igra:
    def __init__(self):
        self.sirina = 10 * A + 2 * ROB
        self.visina = 10 * A + 2 * ROB

        self.krog = Krog([ZACETNA, ZACETNA])

        self.DOL = 'Down'
        self.GOR = 'Up'
        self.LEVO = 'Left'
        self.DESNO = 'Right'

        self.stevec = 1

        self.navodila = ('KROG\n'
                         ' Krog se je izgubil. Pomagaj krogu skozi labirint!')
        self.poskusi = 'Število poskusov: 1'


    def trk(self):
        self.DOL = 'Down'
        self.GOR = 'Up'
        self.LEVO = 'Left'
        self.DESNO = 'Right'
        self.krog.barva = None
        self.krog.lokacija = [ZACETNA, ZACETNA]
        self.navodila = ('O ne, trčil si!\n'
                         'Poskusi ponovno!')
        self.stevec += 1
        self.poskusi = 'Število poskusov: {0}'.format(self.stevec)
        

    def naloga_1(self):#obrne na glavo
        self.navodila = ('Pozor! Svet se je obrnil na glavo!\n'
                         'Zgoraj je spodaj in spodaj je zgoraj!')
        if (self.krog.lokacija == [ROB + 4 * A + B, ROB + 2 * A + B]
            and self.krog.barva == 'yellow'):
            pass
        else:
            self.DOL, self.GOR = self.GOR, self.DOL
            self.krog.spremeni_barvo()

    def naloga_2(self):#zamenja levo - desno
        self.navodila = ('Končno, spet si na nogah. '
                         'Vendar pa te je visenje na glavo povsem zmedlo.\n'
                         'Kje je levo in kje desno?!')
        if (self.krog.lokacija == [ROB + 6 * A + B, ROB + 2 * A + B] and
            self.krog.barva == 'orange'):
            pass
        else:
            (self.DOL, self.GOR,
             self.LEVO, self.DESNO) = (
                 self.GOR, self.DOL,
                 self.DESNO, self.LEVO)
            self.krog.spremeni_barvo()

    def naloga_3(self):#spet obrne na glavo
        self.navodila = ('Ojoj, kakšna zmeda!\n'
                         'Spet si na glavi in vse smeri '
                         'so obrnjene!')
        if (self.krog.lokacija == [ROB + 3 * A + B, ROB + 3 * A + B]
            and self.krog.barva == 'red'):
            pass
        else:
            self.DOL, self.GOR = self.GOR, self.DOL
            self.krog.spremeni_barvo()

    def naloga_4(self):#smeri zavrti za eno v desno, npr.tipka dol pomeni desno
        self.navodila = ('Kaj pa je zdaj to? Padel si na nos!\n'
                         'Vrti se ti, zato so vse smeri zavrtene '
                         'za eno v desno! (Namig: začni s tipko DOL)')
        if (self.krog.lokacija == [ROB + 3 * A + B, ROB + 9 * A + B] and
            self.krog.barva == 'blue'):
            pass
        else:
            (self.DOL, self.GOR,
             self.LEVO, self.DESNO) = (
                 self.DESNO, self.LEVO,
                 self.DOL, self.GOR)
            self.krog.spremeni_barvo()
            

    #oznake, ki se prikažejo ob koncu igre
    def konec(self):
        self.navodila = ('BRAVOO!! Krog si varno pripeljal iz labirinta!\n'
                         'Uspelo ti je že v {0}. poskusu!'.format(self.stevec))
        self.poskusi = ('Pritisni katerokoli tipko!')

    #ko se igra konča, lahko ponovno začneš s pritiskom katere koli tipke
    def zacni_ponovno(self):
        self.DOL = 'Down'
        self.GOR = 'Up'
        self.LEVO = 'Left'
        self.DESNO = 'Right'
        self.krog.barva = None
        self.navodila = ('Kako slabo paziš na krog!\n'
                             'Spet se je izgubil!')
        self.stevec = 1
        self.poskusi = 'Število poskusov: 1'
        self.krog.lokacija = [ZACETNA, ZACETNA]
       

igra = Igra()
