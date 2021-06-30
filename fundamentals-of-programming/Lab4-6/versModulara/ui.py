from domain import *
from teste import *

def adaugare_UI(list_chelt):
    # interfata de adaugare a unei noi cheltuieli

    print("Introduceti informatiile pentru noua cheltuiala:")
    new_chelt = citire()
    list_chelt = adaugare(list_chelt,new_chelt)
    print("Cheltuiala adaugata!")

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
        while True:
            try:
                suma = int(input("Suma precizata:"))
            except ValueError:
                print("INPUT INVALID")
                continue
            else:
                break
        print("Cheltuieli cu suma egala cu ",suma," sunt:")
        afisare_tot_UI(raport_suma(list_chelt,suma))

    elif nr == 4:
        print("Cheltuielile sortate dupa tip sunt : ")
        afisare_tot_UI(raport_sortare_tip(list_chelt))
    else:
        print("Optiunea nu exista!")

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


    
