class Cheltuiala:
    # Elemente cu eticheta Cheltuiala de forma:
    # zi - nr nat  ,  suma - nr real , tip - string
    nr_cheltuieli = 0

    def __init__(self,zi,suma,tip):
        self.zi = zi
        self.suma = suma
        self.tip = tip
        Cheltuiala.nr_cheltuieli += 1

    def __eq__(self,other):
        return (self.zi == other.zi) and (self.tip == other.tip) and (self.suma == other.suma)

    def __repr__(self):
        return "Cheltuiala({},{},'{}')".format(self.zi,self.suma,self.tip)

#getters
def get_zi(chelt):
    return chelt.zi

def get_suma(chelt):
    return chelt.suma

def get_tip(chelt):
    return chelt.tip

#setters
def set_tip(chelt,tip):
    chelt.tip = tip

def set_zi(chelt,zi):
    chelt.zi = zi

def set_suma(chelt,suma):
    chelt.suma = suma

def construct(ziua,suma,tip):
    return Cheltuiala(ziua,suma,tip)

def afisare_tot_UI(list_chelt):
    # afiseaza lista de cheltuieli
    for elem in list_chelt:
        print(elem)

    if not list_chelt:
        print("Lista goala!")
