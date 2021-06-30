#getters
def get_zi(chelt):
    return chelt["zi"]

def get_suma(chelt):
    return chelt["suma"]

def get_tip(chelt):
    return chelt["tip"]

#setters
def set_tip(chelt,tip):
    chelt["tip"]= tip

def set_zi(chelt,zi):
    chelt["zi"]= zi

def set_suma(chelt,suma):
    chelt["suma"]= suma

def construct(ziua,tip,suma):
    return {
        "zi" : ziua,
        "tip" : tip,
        "suma" : suma
    }

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
    
    
    new_chelt = construct(zi,tip_chelt,suma)
    return new_chelt

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
    x = {'zi': 12,  'tip': 'mancare','suma': 200}
    adaugare(lista,x)
    assert lista == [{'zi': 12,  'tip': 'mancare','suma': 200}]

    x = {'zi': 15, 'tip': 'altele','suma': 120}
    adaugare(lista,x)    
    assert lista == [{'zi': 12,  'tip': 'mancare','suma': 200}, {'zi': 15,  'tip': 'altele','suma': 120}]

    lista.clear()

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
    # Date de intrare : list_chelt - lista de cheltuieli , zi - ziua precizata
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
    # Iesire :new_l - o lista ce nu contine elementele cerute
    for i,o in reversed(list(enumerate(list_chelt))):
        if get_tip(o) == tip:
            del list_chelt[i]

def test_stergere():
    # teste pt functia stergere

    lista = []
    lista.append(construct(12,'mancare',200))
    lista.append(construct(12,'altele',120))
    lista.append(construct(12,'mancare',200))
    lista.append(construct(25,'telefon',10))
    
    # test stergere_zi
    stergere_zi(lista,12)
    assert  lista == [{'zi': 25, 'tip': 'telefon','suma': 10}]
    lista.clear()
    lista.append(construct(12,'mancare',200))
    lista.append(construct(25,'telefon',10))
    stergere_zi(lista,25)
    assert lista == [{'zi': 12, 'tip': 'mancare','suma': 200 }]
    lista.clear()

    #test stergere_interval
    lista.append(construct(4,'intretinere',600))
    lista.append(construct(3,'imbracaminte',200))
    lista.append(construct(15,'mancare',120))
    lista.append(construct(12,'mancare',200))
    stergere_interval(lista,2,5)
    assert lista == [{'zi': 15, 'tip': 'mancare','suma': 120} , {'zi': 12,  'tip': 'mancare','suma': 200}]
    stergere_interval(lista,31,30)
    assert lista == [{'zi': 15, 'tip': 'mancare','suma': 120} , {'zi': 12, 'tip': 'mancare','suma': 200}]
    lista.clear()

    #test stergere_tip
    lista.append(construct(3,'imbracaminte',200))
    lista.append(construct(4,'intretinere',620))
    lista.append(construct(15,'mancare',120))
    lista.append(construct(12,'mancare',200))
    stergere_tip(lista,'mancare')
    assert lista == [{'zi': 3,  'tip': 'imbracaminte','suma': 200} , {'zi': 4,  'tip': 'intretinere','suma': 620}]
    stergere_tip(lista,'altele')
    assert lista == [{'zi': 3,  'tip': 'imbracaminte','suma': 200} , {'zi': 4,  'tip': 'intretinere','suma': 620}]
    

#cautari
def cautari_UI(list_chelt):
    # meniul pentru cerintele de Cautari

    print("\n MENIU CAUTARI")
    print("Selcetiati un din optiunile de mai jos . Introduceti nr optiunii.")
    print("1.Tipărește toate cheltuielile mai mari decât o sumă dată")
    print("2.Tipărește toate cheltuielile efectuate înainte de o zi dată și mai mici decât o sumă ")
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
        if float(get_suma(elem)) > suma : 
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
    lista = []
    lista.append(construct(2,'altele',70))
    lista.append(construct(5,'mancare',80))
    lista.append(construct(23,'intretinere',150))
    
    assert cautare_suma(lista,120.5) == [{'zi': 23,  'tip': 'intretinere','suma': 150}]
    assert cautare_suma(lista,100) == [{'zi': 23,  'tip': 'intretinere','suma': 150}]
    assert cautare_suma(lista,5000) == []

    # test cautare_zi_suma
    
    assert cautare_zi_suma(lista,100,10) == [{'zi': 2,  'tip': 'altele', 'suma': 70,} , {'zi': 5,  'tip': 'mancare','suma': 80}]
    assert cautare_zi_suma(lista,50,2) == []
    assert cautare_zi_suma(lista,500,5) == [{'zi': 2,  'tip': 'altele','suma': 70}]

    #test cautare_tip
    assert cautare_tip(lista,'mancare') == [{'zi': 5,  'tip': 'mancare','suma': 80}]
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
                s = s + int(get_suma(obj))
        sume.append(s)
    
    imax = max(range(len(sume)), key = sume.__getitem__)

    x = zile[imax]
    zile.clear()
    sume.clear()
    return x
        
def raport_suma(list_chelt,suma):
    pass

def raport_sortare_tip(list_chelt):
    pass

def test_rapoarte():
    # teste pt functia raport_suma_total_tip
    lista=[{'zi': 12,  'tip': 'mancare','suma': 200},{'zi': 5,  'tip': 'mancare','suma': 200} , {'zi': 5,  'tip': 'altele','suma': 120}]
    assert raport_suma_totala_tip(lista,'mancare') == 400

    assert raport_suma_totala_tip(lista,'telefon') == 0
    
    lista= []
    assert raport_suma_totala_tip(lista,'telefon') ==0

    # teste pt functia raport_ziua_maxima
    lista.append(construct(6,'telefon',100))
    lista.append(construct(2,'mancare',200))
    assert raport_ziua_maxima(lista) == 2
    
    lista.append(construct(6,'telefon',101))
    assert raport_ziua_maxima(lista) == 6
    lista.clear()
    lista.append(construct(2,'telefon',200))
    lista.append(construct(6,'mancare',200))
    assert raport_ziua_maxima(lista) == 2

    #teste pt 

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
        print(filtru_suma(list_chelt,suma))
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
    lista = []
    lista.append(construct(12,'mancare',200))
    lista.append(construct(25,'altele',100))
    lista.append(construct(5,'mancare',50))
    assert filtru_tip(lista , 'mancare') == [{'zi': 25, 'tip': 'altele','suma': 100}]

    assert filtru_tip(lista , 'altele') == [{'zi': 12,  'tip': 'mancare','suma': 200},{'zi': 5, 'tip': 'mancare','suma': 50}]

    assert filtru_tip([] , 'telefon') == []
    


    # testare filtru_suma
    lista = []
    lista.append(construct(12,'telefon',75))
    lista.append(construct(13,'mancare',25))
    lista.append(construct(1,'altele',120))
    
    assert filtru_suma(lista , 100) == [{'zi': 1,  'tip': 'altele','suma': 120}]

    assert filtru_suma(lista,50) == [{'zi': 12,  'tip': 'telefon','suma': 75},{'zi': 1, 'tip': 'altele','suma': 120}]
    
    assert filtru_suma([] , 'mancare') == []

    assert filtru_suma(lista,0) == [{'zi': 12,  'tip': 'telefon','suma': 75},{'zi': 13,  'tip': 'mancare','suma': 25},{'zi': 1,  'tip': 'altele','suma': 120}]
    
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

def exemplu(list_chelt):
    list_chelt.append({'zi': 25,  'tip': 'mancare','suma': 250})
    list_chelt.append({'zi': 2,  'tip': 'telefon','suma': 50})
    list_chelt.append({'zi': 6,  'tip': 'altele','suma': 25})
    list_chelt.append({'zi': 18, 'tip': 'mancare','suma': 150, })
    list_chelt.append({'zi': 21,  'tip': 'imbracaminte','suma': 200})

#principal
def run():
    # programul principal
    teste()
    
    list_chelt = []

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
            adaugare_UI(list_chelt)
        elif cmd == 'delete':
            stergere_UI(list_chelt)
        elif cmd == 'search':
            cautari_UI(list_chelt)
        elif cmd == 'report':
            rapoarte_UI(list_chelt)
        elif cmd == 'filter':
            filtrare_UI(list_chelt)
        elif cmd == 'exemplu':
            exemplu(list_chelt)
        else:
            print("COMANDA INVALIDA!")

run()

