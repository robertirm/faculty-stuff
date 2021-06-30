from domain import *

def meniu_batch():
    list_chelt=[]
    undo_list=[]
    print("Comenzi acceptate:")
    print("add (zi) (suma) (tip) - adauga o noua cheltuiala")
    print("delete (tip) - sterge cheltuielle de tipul precizat")
    print("report - afiseaza ziua cu cheltuili maxime")
    print("show - afiseaza lista de cheltuieli")
    print("undo - reface ultima operatie")
    print("exit - iesire\n")
    ok = True
    while ok:
        comenzi = input("\nintroduceti comenzile separate de ';' pentru ajutor: ")
        lista_comenzi = comenzi.split(";")
        
        for cmd in lista_comenzi:
            param = cmd.split(" ")
            for i,cm in reversed(list(enumerate(param))):
                if cm == '':
                    del param[i]
            if param[0] == 'exit':
                ok = False
            else :
                efectuare_batch(list_chelt,param,undo_list)

def efectuare_batch(list_chelt,param,undo_list):
    erori = verificare_batch(param)
    if erori != []:
        print("EROARE ",erori)
    else:
        print("REALIZAT")
        if param[0] == 'add':
            retinere_undo(undo_list,list_chelt)
            list_chelt = adaugare(list_chelt,construct(param[1],param[2],param[3]))
        elif param[0] == 'delete':
            retinere_undo(undo_list,list_chelt)
            stergere_tip(list_chelt,param[1])
        elif param[0] == 'show':
            afisare_tot_UI(list_chelt)
        elif param[0] == 'undo':
            undo(undo_list,list_chelt)
        elif param[0] == 'report':
            print(raport_ziua_maxima(list_chelt))

def verificare_batch(param):
    tipuri = ("mancare" , "telefon" , "imbracaminte" , "intretinere" , "altele")
    erori = []
    if param[0] == 'add':
        if len(param) !=4:
            erori.append("parametrii insuficienti!")
        else:
            if is_int(param[1]) == False:
                erori.append("ziua trebuie sa fie numar intreg!")
            if is_float(param[2]) == False:
                erori.append("suma trebuie sa fie un numar!")
            if param[3] not in tipuri:
                erori.append("tipul nu este valid!")
    elif param [0] == 'delete':
        if len(param) !=2:
            erori.append("parametrii insuficienti!")
        elif param[1] not in tipuri:
            erori.append("tipul nu este valid!")
    elif param [0] == 'show':
        if len(param) != 1:
            erori.append("nu poate avea parametrii!")
    elif param[0] == 'undo':
        if len(param) != 1:
            erori.append("nu poate avea parametrii!")
    elif param[0] == 'report':
        if len(param) != 1:
            erori.append("nu poate avea parametrii!")
    elif param[0] == 'exit':
        if len(param) != 1:
            erori.append("nu poate avea parametrii!")        
    else:
        erori.append("comanda invalida!")

    return erori