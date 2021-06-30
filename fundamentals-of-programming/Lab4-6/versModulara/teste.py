from domain import *

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

def test_update():
    # teste pentru functia update
    lista = []
    lista.append(construct(25,100,'mancare'))
    update(lista,lista[0],construct(3,22,'telefon'))
    assert lista == [construct(3,22,'telefon')]

    update(lista,construct(4,50,'imbracaminte'),construct(5,50,'mancare'))
    assert lista == [construct(3,22,'telefon')]

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
    lista = [construct(1,5,'mancare'),construct(2,5,'mancare'),construct(3,56,'intretinere')]
    assert raport_sortare_tip(lista) == [[construct(1,5,'mancare'),construct(2,5,'mancare')] , [] , [] , [construct(3,56,'intretinere')] , [] ]

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

def test_undo():
    #teste pentu functia copiere_lista
    lista = [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]
    lista1 = copiere_lista(lista)
    assert  lista1== [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]
    adaugare(lista,construct(1,1,'telefon'))
    assert  lista1== [construct(12,200,'mancare') , construct(25,100,'altele') , construct(5,50,'mancare')]

    #

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
