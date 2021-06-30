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

#adaugari
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

def adaugare_UI(list_chelt):
    # interfata de adaugare a unei noi cheltuieli

    print("Introduceti informatiile pentru noua cheltuiala:")
    new_chelt = citire()
    list_chelt = adaugare(list_chelt,new_chelt)
    print("Cheltuiala adaugata!")

def adaugare(list_chelt,chelt):
    # Adauga o noua cheltuiala la lista de cheltuieli
    # Date de intreare : list_chelt - lista curenta  de cheltuieli , chelt - cheltuiala ce trebuie adaugata
    # Date de iesire : new_l - noua lista
    new_l = list_chelt
    new_l.append(chelt)
    return new_l

def test_adaugare():
    # teste pt functia adaugare
    lista = [] 
    x = construct(12,200,'mancare')
    adaugare(lista,x)
    assert lista == [construct(12,200,'mancare')]

    x = construct(15,120,'altele')
    adaugare(lista,x)    
    assert lista == [construct(12,200,'mancare') , construct(15,120,'altele')]

    lista.clear()

#actualizari
def update(list_chelt,chelt,chelt_act):
    #Functia actualizeaza datele dintr-o cheltuiala cu altele introduse
    #Date de intrare : list_chelt - lista de cheltuieli , chelt - cheltuiala cu datele actuale, chelt_act - cheltuiala cu noile date
    #Iesire : Cheltuiala specificata apare in lista cu noile date
    for obj in list_chelt:
        if obj == chelt:
            set_zi(obj,get_zi(chelt_act))
            set_suma(obj,get_suma(chelt_act))
            set_tip(obj,get_tip(chelt_act))
            
def update_UI(list_chelt):
    # meniu actualizari
    print("Pentru a actualiza o cheltuiala introduceti datele respectivei cheltuieli")
    chelt_act = citire()
    if chelt_act not in list_chelt:
        print("Cheltuiala nu exista! Verificati cheltuielile actuale folosinf comanda 'show' ")
    else:
        print("Introduceti noile date:")
        new_act = citire()
        update(list_chelt,chelt_act,new_act)
        print("Cheltuiala a fost actualizata!")

def test_update():
    # teste pentru functia update
    lista = []
    lista.append(construct(25,100,'mancare'))
    update(lista,lista[0],construct(3,22,'telefon'))
    assert lista == [construct(3,22,'telefon')]

    update(lista,construct(4,50,'imbracaminte'),construct(5,50,'mancare'))
    assert lista == [construct(3,22,'telefon')]

#stergeri
def stergere_UI(list_chelt):
    # meniul pentru cerintele de stergere
    print("\n MENIU STERGERI")
    print("Selectati dupa ce criteriu vreti sa stergeti anumite cheltuieli.Introduceti nr acestiua.")
    print("1.Șterge toate cheltuielile pentru ziua dată")
    print("2.Șterge cheltuielile pentru un interval de timp (se dă ziua de început și sfârșit, se șterg toate cheltuielile pentru perioada dată) ")
    print("3.Șterge toate cheltuielile de un anumit tip")
    while True:
        try:
            nr = int(input("Nr. optiunii :"))
        except ValueError:
            print("INPUT INVALID")
            continue
        else:
            break
    
    if nr == 1:
        #Șterge toate cheltuielile pentru ziua dată
        while True:
            try:
                zi = int(input("Ziua dorita:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break
        
        stergere_zi(list_chelt,zi)
        print("S-au sters! Folositi 'show' pentru a vedea noua lista de cheltuieli!")
    
    elif nr == 2:
        #Șterge cheltuielile pentru un interval de timp 
        #se dă ziua de început și sfârșit, se șterg toate cheltuielile pentru perioada dată
        while True:
            try:
                zi1 = int(input("Ziua dorita:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break
        while True:
            try:
                zi2 = int(input("Ziua dorita:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break
        
        stergere_interval(list_chelt,zi1,zi2)
        print("S-au sters! Folositi 'show' pentru a vedea noua lista de cheltuieli!")

    elif nr == 3:
        #Șterge toate cheltuielile de un anumit tip
        tip_chelt = input("Tipul precizat : ")
        tipuri_cheltuieli = ['mancare' , 'intretinere' , 'imbracaminte' , 'telefon' , 'altele']
        while tip_chelt not in tipuri_cheltuieli:
            print("Acest tip de cheltuiala nu exista. Inceracti : 'mancare' , 'intretinere', 'imbracaminte' , 'telefon' , 'altele' ")
            tip_chelt = input("Tipul : ")
        
        stergere_tip(list_chelt,tip_chelt)
        print("S-au sters! Folositi 'show' pentru a vedea noua lista de cheltuieli!")

    else :
        print("Optiunea nu exista!")
      
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

def test_stergere():
    # teste pt functia stergere

    # test stergere_zi
    lista=[construct(12,200,'mancare') , construct(12,120,'altele') , construct(12,200,'mancare') , construct(25,10,'telefon')]
    stergere_zi(lista,12)
    assert  lista == [construct(25,10,'telefon')]
    lista=[construct(12,200,'mancare') , construct(15,120,'altele') , construct(12,200,'telefon') , construct(25,10,'mancare')]
    stergere_zi(lista,30)
    assert lista == [construct(12,200,'mancare') , construct(15,120,'altele') , construct(12,200,'telefon') , construct(25,10,'mancare')]
    lista = []
    stergere_zi(lista,30)
    assert lista == []

    #test stergere_interval
    lista=[ construct(4,660,'intretinere'),construct(3,200,'imbracaminte'),construct(15,120,'mancare') , construct(12,200,'mancare')]
    stergere_interval(lista,2,5)
    assert lista == [construct(15,120,'mancare') , construct(12,200,'mancare')]
    stergere_interval(lista,31,30)
    assert lista == [construct(15,120,'mancare') , construct(12,200,'mancare')]
    stergere_interval(lista,17,11) 
    assert lista == []

    #test stergere_tip
    lista=[construct(3,200,'imbracaminte') , construct(4,620,'intretinere'),construct(15,120,'mancare') , construct(12,200,'mancare')]
    stergere_tip(lista,'mancare')
    assert lista == [construct(3,200,'imbracaminte') , construct(4,620,'intretinere')]
    stergere_tip(lista,'altele')
    assert lista == [construct(3,200,'imbracaminte') , construct(4,620,'intretinere')]
    stergere_tip(lista,'intretinere')
    assert lista == [construct(3,200,'imbracaminte')]

#cautari
def cautari_UI(list_chelt):
    # meniul pentru cerintele de Cautari

    print("\n MENIU CAUTARI")
    print("Selcetiati un din optiunile de mai jos . Introduceti nr optiunii.")
    print("1.Tipărește toate cheltuielile mai mari decât o sumă dată")
    print("2.Tipărește toate cheltuielile efectuate înainte de o zi dată și mai mici decât o sumă (se dă suma și ziua,se tipăresc toate cheltuielile mai mici ca suma dată și efectuate înainte de ziua specificată) ")
    print("3.Tipărește toate cheltuielile de un anumit tip.")
    while True:
        try:
            nr = int(input("Nr. optiunii :"))
        except ValueError:
            print("INPUT INVALID")
            continue
        else:
            break
    
    if nr == 1:
        while True:
            try:
                suma = int(input("Suma precizata:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break
        print("Cheltuielile ce au suma mai mare ca " ,suma , " sunt :")
        afisare_tot_UI( cautare_suma(list_chelt,suma))

    elif nr == 2:
        while True:
            try:
                zi = int(input("Ziua dorita:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break

        while True:
            try:
                suma = int(input("Suma precizata:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break

        print("Cheltuielile cautate sunt :")
        afisare_tot_UI(cautare_zi_suma(list_chelt,suma,zi))
    
    elif nr == 3:
        tip_chelt = input("Tipul precizat : ")
        tipuri_cheltuieli = ['mancare' , 'intretinere' , 'imbracaminte' , 'telefon' , 'altele']
        while tip_chelt not in tipuri_cheltuieli:
            print("Acest tip de cheltuiala nu exista. Inceracti : 'mancare' , 'intretinere', 'imbracaminte' , 'telefon' , 'altele' ")
            tip_chelt = input("Tipul : ")

        print("Cheltuielile cautate sunt :")
        #print(cautare_tip(list_chelt,tip_chelt))
        afisare_tot_UI(cautare_tip(list_chelt,tip_chelt))

    else:
        print("Optiunea nu exista!")

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

def test_cautari():
    # test cautare_suma
    lista = [construct(2,70,'altele') , construct(5,80,'mancare') , construct(23,150,'intretinere')]

    assert cautare_suma(lista,120.5) == [construct(23,150,'intretinere')]
    assert cautare_suma(lista,100) == [construct(23,150,'intretinere')]
    assert cautare_suma(lista,5000) == []

    # test cautare_zi_suma
    assert cautare_zi_suma(lista,100,10) == [construct(2,70,'altele') , construct(5,80,'mancare')]
    assert cautare_zi_suma(lista,50,2) == []
    assert cautare_zi_suma(lista,500,5) == [construct(2,70,'altele')]

    #test cautare_tip
    assert cautare_tip(lista,'mancare') == [construct(5,80,'mancare')]
    assert cautare_tip(lista,'telefon') == []

#rapoarte
def rapoarte_UI(list_chelt):
    # meniul pentru cerintele de rapoarte
    print("\n MENIU RAPOARTE")
    print("Selcetiati un din optiunile de mai jos . Introduceti nr optiunii.")
    print("1.Tipărește suma totală pentru un anumit tip de cheltuială ")
    print("2.Găsește ziua în care suma cheltuită e maximă ")
    print("3.Tipărește toate cheltuielile ce au o anumită sumă ")
    print("4.Tipărește cheltuielile sortate după tip ")
    while True:
        try:
            nr = int(input("Nr. optiunii :"))
        except ValueError:
            print("INPUT INVALID")
            continue
        else:
            break

    if nr == 1:
        tip_chelt = input("Tipul precizat : ")
        tipuri_cheltuieli = ['mancare' , 'intretinere' , 'imbracaminte' , 'telefon' , 'altele']
        while tip_chelt not in tipuri_cheltuieli:
            print("Acest tip de cheltuiala nu exista. Inceracti : 'mancare' , 'intretinere', 'imbracaminte' , 'telefon' , 'altele' ")
            tip_chelt = input("Tipul : ")

        print("Suma totala pentru tipul ",tip_chelt,' este ',raport_suma_totala_tip(list_chelt,tip_chelt))
        
    elif nr == 2:
        print("Ziua cu cheltuielile maxime este :",raport_ziua_maxima(list_chelt))

    elif nr == 3:
        pass
    elif nr == 4:
        pass
    else:
        print("Optiunea nu exista!")

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
                s = s + get_suma(obj)
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
    pass

def test_rapoarte():
    # teste pt functia raport_suma_total_tip
    lista=[construct(12,200,'mancare') , construct(15,120,'altele') , construct(12,200,'mancare')]
    assert raport_suma_totala_tip(lista,'mancare') == 400
    lista=[Cheltuiala(12,200,'mancare') , Cheltuiala(15,120,'altele')]
    assert raport_suma_totala_tip(lista,'telefon') == 0
    lista= []
    assert raport_suma_totala_tip(lista,'telefon') ==0

    # teste pt functia raport_ziua_maxima
    lista =[construct(6,100,'telefon'),construct(2,200,'mancare')]  
    assert raport_ziua_maxima(lista) == 2
    lista =[construct(2,200,'telefon'),construct(6,100,'mancare'),construct(6,101,'telefon')]
    assert raport_ziua_maxima(lista) == 6
    lista =[construct(2,200,'telefon'),construct(6,100,'mancare')]
    assert raport_ziua_maxima(lista) == 2

    #teste pt functia raport_suma
    lista = [construct(2,100,'mancare'),construct(5,100,'imbracaminte')]
    assert raport_suma(lista,100) == [construct(2,100,'mancare'),construct(5,100,'imbracaminte')]
    lista = [construct(2,500,'intretinere')]
    assert raport_suma(lista,100) == []
    
    #teste pt functia raport_sortare_tip
            
#fitre
def filtrare_UI(list_chelt):    
    # face operatiile de stergere
    print("\n MENIU FILTRARI")
    print("Selcetiati una din optiunile de mai jos . Introduceti nr optiunii.")
    print("1.Elimină toate cheltuielile de un anumit tip")
    print("2.Elimină toate cheltuielile mai mici decât o sumă dată")
    while True:
        try:
            nr = int(input("Nr. optiunii :"))
        except ValueError:
            print("INPUT INVALID")
            continue
        else:
            break

    if nr == 1:
        #Elimină toate cheltuielile de un anumit tip
        
        tip_chelt = input("Tipul precizat : ")
        tipuri_cheltuieli = ['mancare' , 'intretinere' , 'imbracaminte' , 'telefon' , 'altele']
        while tip_chelt not in tipuri_cheltuieli:
            print("Acest tip de cheltuiala nu exista. Inceracti : 'mancare' , 'intretinere', 'imbracaminte' , 'telefon' , 'altele' ")
            tip_chelt = input("Tipul : ")

        print("Cheltuielile ramase sunt : ")
        print(filtru_tip(list_chelt,tip_chelt))
        
    elif nr == 2:
        while True:
            try:
                suma = int(input("Suma precizata:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break
        print("Cheltuielile ramase sunt :")
        print(cautare_suma(list_chelt,suma))
        pass

    else :
        print("Optiunea nu exista!")

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

def test_filtrare():
    # testare filtrare_tip
    lista = [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]
    assert filtru_tip(lista , 'mancare') == [construct(25,100,'altele')]
    lista = [construct(12,200,'mancare') , construct(25,100,'altele')]
    assert filtru_tip(lista , 'altele') == [construct(12,200,'mancare')]
    assert filtru_tip([] , 'telefon') == []
    
    # testare filtru_suma
    lista = [construct(12,75,'telefon') , construct(13,25,'mancare') , construct(1,120,'altele')]
    assert filtru_suma(lista , 100) == [construct(1,120,'altele')]
    assert filtru_suma(lista,50) == [construct(12,75,'telefon') , construct(1,120,'altele')]
    assert filtru_suma([] , 'mancare') == []
    assert filtru_suma(lista,0) == [construct(12,75,'telefon') , construct(13,25,'mancare') , construct(1,120,'altele')]

#undo
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

def undo(undo_list,list_chelt):
    # Functia restituie ultima instanta a listei inainte ca aceasta sa fie modificata
    # Date de intrare : undo_list - lista cu listele modificate pe parcursul derularii programului,list_chelt - lista de cheltuieli
    # Iesire : list_chelt se restituie la forma anterioara ultimei operatii
    if undo_list == []:
        print("Nu se poate efectua !")
        return

    list_chelt[:] = undo_list[-1]
    undo_list.pop()

def test_undo():
    #teste pentu functia copiere_lista
    lista = [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]
    lista1 = copiere_lista(lista)
    assert  lista1== [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]
    adaugare(lista,construct(1,1,'telefon'))
    assert  lista1== [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]

    #

#diverse
def afisare_tot_UI(list_chelt):
    # afiseaza lista de cheltuieli
    for elem in list_chelt:
        print(elem)

    if not list_chelt:
        print("Lista goala!")

def ajutor_UI():
    # lista de comenzi si rolul lor

    print("Comenzile acceptate sunt urmatoarele :")
    print("helpme - afiseaza toate comenzile acceptate")
    print("exit - opreste programul")
    print("show - arata toate cheltuielile retinute ")
    print("add - adauga o noua cheltuiala")
    print("delete - sterge cheltuielile dupa niste conditii precizate")
    print("search - efectueaza cautarii dupa niste criterii precizate")
    print("report - efectueaza rapoarte dupa niste criterii precizatre")
    print("filter - efectueaza niste filtre dupa niste conditii precizate")

def teste():
    # ruleaza toate testele
    test_adaugare()
    test_stergere()
    test_rapoarte()
    test_filtrare()
    test_cautari()
    test_update()
    test_undo()

def exemplu(list_chelt):
    list_chelt.append(Cheltuiala(25,250,'mancare'))
    list_chelt.append(Cheltuiala(2,50,'telefon'))
    list_chelt.append(Cheltuiala(6,25,'altele'))
    list_chelt.append(Cheltuiala(18,150,'mancare'))
    list_chelt.append(Cheltuiala(21,200,'imbracaminte'))

#principal
def run():
    # programul principal
    teste()
    
    list_chelt = []
    undo_list = []

    print('Tastati comanda helpme pentru a afla toate comenzile permise sau introduceti o comanda dintre cele permise.')
    while True:
        cmd = input(">>>")
        if cmd == 'exit':
            print("Inchidere program!")
            return
        elif cmd == 'helpme':
            ajutor_UI()
        elif cmd == 'show':
            print("Cheltuielile actuale sunt :")
            afisare_tot_UI(list_chelt)
        elif cmd == 'add':
            retinere_undo(undo_list,list_chelt)            
            adaugare_UI(list_chelt)
        elif cmd == 'delete':
            retinere_undo(undo_list,list_chelt)   
            stergere_UI(list_chelt)
        elif cmd == 'update':
            retinere_undo(undo_list,list_chelt)   
            update_UI(list_chelt)
        elif cmd == 'search':
            cautari_UI(list_chelt)
        elif cmd == 'report':
            rapoarte_UI(list_chelt)
        elif cmd == 'filter':
            filtrare_UI(list_chelt)
        elif cmd == 'exemplu':
            retinere_undo(undo_list,list_chelt)
            exemplu(list_chelt)
        elif cmd == 'undo':
            undo(undo_list,list_chelt)
        else:
            print("COMANDA INVALIDA!")

run()

