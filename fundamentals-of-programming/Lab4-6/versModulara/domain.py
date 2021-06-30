from clasa import *

def citire():

    #citeste o cheltuiala introdusa de utilizator
    #Intrare : date oferite de utilizator
    #Date de iesire : new_chelt - o instanta de cheltuiala 
    
    #citeste si valizdeaza ziua
    while True:
        try:
            zi = int(input("Zi :"))
        except ValueError:
            print("Input invalid!")
            continue
        else:
            break

    #citeste si valideaza suma
    while True:
        try:
            suma = float(input("Suma :"))
        except ValueError:
            print("Input invalid!")
            continue
        else:
            break

    #citeste si valideaza tipul
    tipuri_cheltuieli = ['mancare' , 'intretinere' , 'imbracaminte' , 'telefon' , 'altele']
    tip_chelt = input("Tipul : ")
    while tip_chelt not in tipuri_cheltuieli:
        print("Acest tip de cheltuiala nu exista. Inceracti : 'mancare' , 'intretinere', 'imbracaminte' , 'telefon' , 'altele' ")
        tip_chelt = input("Tipul : ")
    
    
    return construct(zi,suma,tip_chelt)

def adaugare(list_chelt,chelt):
    # Adauga o noua cheltuiala la lista de cheltuieli
    # Date de intreare : list_chelt - lista curenta  de cheltuieli , chelt - cheltuiala ce trebuie adaugata
    # Date de iesire : new_l - noua lista
    new_l = list_chelt
    new_l.append(chelt)
    return new_l

def update(list_chelt,chelt,chelt_act):
    #Functia actualizeaza datele dintr-o cheltuiala cu altele introduse
    #Date de intrare : list_chelt - lista de cheltuieli , chelt - cheltuiala cu datele actuale, chelt_act - cheltuiala cu noile date
    #Iesire : Cheltuiala specificata apare in lista cu noile date
    for obj in list_chelt:
        if obj == chelt:
            set_zi(obj,get_zi(chelt_act))
            set_suma(obj,get_suma(chelt_act))
            set_tip(obj,get_tip(chelt_act))

def stergere_zi(list_chelt,zi):
    # Functia sterge toate cheltuielile petru o zi data
    # Date de intrare : list_chelt - lista de cheltuieli , zi  - int
    # Iesire : lista nu contine elementele cerute
    
    for i,o in reversed(list(enumerate(list_chelt))):
        if get_zi(o) == zi:
            del list_chelt[i]
      
def stergere_interval(list_chelt,ziua1,ziua2):
    # Functia sterge toate cheltuielile din intervalul de zile precizat
    # Date de intrare : list_chelt - lista de cheltuieli , ziua1 - prima zi , ziu2 - a doua zi
    # Iesire : new_l - o lista ce nu contine elementele cerute

    if ziua1 > ziua2 :
        ziua1,ziua2 = ziua2,ziua1

    for i,o in reversed(list(enumerate(list_chelt))):
        if ziua1 <= get_zi(o) <= ziua2:
            del list_chelt[i]

def stergere_tip(list_chelt,tip):
    # Functia sterge toate cheltuielile de tipul precizat
    # Date de intrare : list_chelt - lista de cheltuieli , tip - tipul
    # Iesire :lista ce nu contine elementele cerute
    for i,o in reversed(list(enumerate(list_chelt))):
        if get_tip(o) == tip:
            del list_chelt[i]

def cautare_suma(list_chelt , suma):
    # Functia construieste o noua lista cu cheltuielile care au suma mai mare decat cea transmisa
    # Date de intrare : list_chelt - lista de cheltuieli, suma - suma precizata,nr real
    # Date de iesire : new_l - lista de cheltuieli ce respecta conditia 

    new_l = []
    for elem in list_chelt:
        if float(elem.suma) > suma : 
            new_l.append(elem)
    return new_l

def cautare_zi_suma(list_chelt , suma , zi):
    # Functia construieste o noua lista Tipărește toate cheltuielile efectuate înainte de o zi dată și mai mici decât o sumă 
    # Date de intrare : list_chelt - lista de cheltuieli, suma - float , zi -int
    # Date de iesire : new_l - lista de cheltuieli ce respecta conditia 

    new_l = []
    for elem in list_chelt:
        if get_zi(elem) < zi  and get_suma(elem) < suma:
            new_l.append(elem)
    return new_l

def cautare_tip(list_chelt , tip):
    # Functia construieste o noua lista cu cheltuielile care au tipul precizat
    # Date de intrare : list_chelt - lista de cheltuieli, tip -string
    # Date de iesire : new_l - lista de cheltuieli ce respecta conditia 

    new_l=[]
    for elem in list_chelt:
        if get_tip(elem) == tip:
            new_l.append(elem)
    return new_l

def raport_suma_totala_tip(list_chelt,tip):
    # Functia calculeaza suma totala a cheltuielilor de un tip precizat
    # Date de intrare : list_chelt - lista de cheltuieli , tip - tipul
    # Date de iesire : s - suma ceruta
    
    s = 0
    for o in list_chelt:
        if get_tip(o) == tip:
            s = s + float(get_suma(o))
    return s

def raport_ziua_maxima(list_chelt):
    # Functia gaseste ziua în care suma cheltuită e maxima 
    # Date de intrare : list_chelt - lista de cheltuieli
    # Date de iesire : zi_max - int 
    # OBS: daca sunt mai multe zile cu aceeasi suma cheltuita , se afiseaza cea mai veche adaugata 

    zile = []
    sume = []
    for obj in list_chelt:
       if get_zi(obj) not in zile:
           zile.append(get_zi(obj))

    
    for zi in zile:
        s = 0 
        for obj in list_chelt:
            if zi == get_zi(obj):
                s = s + int(get_suma(obj))
        sume.append(s)
    
    imax = max(range(len(sume)), key = sume.__getitem__)

    x = zile[imax]
    zile.clear()
    sume.clear()
    return x
        
def raport_suma(list_chelt,suma):
    # Functia gaseste toate cheltuielile ce au suma egala cu una precizata
    # Date de intrare : list_chelt - lista de cheltuieli , suma - float 
    # Date de iesire : new_chelt - lista cu cheltuielile dorite 
    new_chelt = []
    for obj in list_chelt:
        if get_suma(obj) == suma:
            new_chelt.append(obj)
    return new_chelt

def raport_sortare_tip(list_chelt):
    # Functia imparte lista de cheltuieli in alte liste , fiecare fiind de un anumit tip
    # Date de intrare : list_chelt - lista de cheltuieli
    # Date de iesire : lista - lista formata din alte liste fiecare avand cheltuieli de un tip
    lista = []
    lista.append(cautare_tip(list_chelt,"mancare"))
    lista.append(cautare_tip(list_chelt,"telefon"))
    lista.append(cautare_tip(list_chelt,"imbracaminte"))
    lista.append(cautare_tip(list_chelt,"intretinere"))
    lista.append(cautare_tip(list_chelt,"altele"))
    return lista

def filtru_tip(list_chelt, tip):
    # Functia creeaza o lista cu valorile care nu sunt de un tip precizat
    # Date de intrare : list_chelt - lsita de cheltuieli , tip - tipul precizat(string)
    # Date de iesire : list_filt - lista cu valorile dorite

    list_filt = []
    for o in list_chelt:
        if get_tip(o) != tip:
            list_filt.append(o)

    return list_filt

def filtru_suma(list_chelt, suma):
    # Functia creeaza o lista cu valorile mai mari decat suma precizata
    # Date de intrare : list_chelt - lista de cheltuieli , suma - suma precizata(float)
    # Date de iesire : new_l - lista cu valorile cerute

    new_l = []
    for o in list_chelt:
        if get_suma(o) > suma:
            new_l.append(o)

    return new_l

def copiere_lista(list_chelt):
    #Functia creeaza o copie a unei liste
    #Date de intrare : list_chelt- lista de cheltuieli
    #Date de iesire : lista - copia 
    lista = []
    for obj in list_chelt:
        newobj = construct(get_zi(obj),get_suma(obj),get_tip(obj))
        lista.append(newobj)
    return lista

def retinere_undo(undo_list,list_chelt):
    # Functia adauga lista curenta intr-un istoric al tuturor listelor 
    undo_list.append(copiere_lista(list_chelt))

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):

    try:
        float(s)
        return True
    except ValueError:
        return False

def undo(undo_list,list_chelt):
    # Functia restituie ultima instanta a listei inainte ca aceasta sa fie modificata
    # Date de intrare : undo_list - lista cu listele modificate pe parcursul derularii programului,list_chelt - lista de cheltuieli
    # Iesire : list_chelt se restituie la forma anterioara ultimei operatii
    if undo_list == []:
        print("Nu se poate efectua !")
        return

    list_chelt[:] = undo_list[-1]
    undo_list.pop()
