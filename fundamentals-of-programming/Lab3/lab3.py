def read(userList):
    # Functia memoreaza lista introdusa de utilizator
    # date de intrare : userList - lista care memoreaza datele de la utilizator
    userList.clear()
    input_list = input("Introduceti o lista de numere intregi : ")
    
    if '.' in input_list:
        print("Input invalid")
        input_list = ""
        read(userList)
    elif input_list.upper().isupper() == False:   
        for nr in input_list.split():
            userList.append(int(nr))
        print("Lista valida.")
    else:
        print("Input invalid")
        input_list = ""
        read(userList)

def noListRead(operatie,userList):
    # Functia verifica daca se doreste executarea unei comenzi ce lucreaza pe o lista ce nu a fost introdusa
    # date de intrare : operatie - fucntia care se doreste executata , userList - lista utilizata
    if operatie == read:
        read(userList)
    elif not userList:
        print("Lista nu exista. Introduceti una cu comanda 'citire'")        
    else:
        operatie(userList)
    
def solve8(userList):
    # Cerinta 8 : Secv. de lung. max. ce au toate elementele in intervalul [0,10]
    # date de intrare : userList - lista pe care se lucreaza
    # date de iesire : se afiseaza secventele cerute

    userList.append(-1) #rezolva cazul cand ultima secventa se termina la sfarsitul listei initiale
    
    final_list = []
    new_l = []
    for i in userList:
        if not ( 0 <= i <= 10):
            final_list.append(new_l)
            new_l = []
        else :
            new_l.append(i)

    maxList = max(final_list , key = len)
    if len(maxList) != 0:
        for l in final_list:
            if len(l) == len(maxList):
                print(l)
    else:
        print(maxList)    

    userList.pop()       

def cifrecomune(n1,n2):
    # functia afla daca doua nr au cel putin doua cifre comune
    # date de intrare : n1,n2-nr naturale
    # date de iesire : True, daca numerele au prop ceruta si False , in caz contrar
    cfc = 0
    cif1 = [0,0,0,0,0,0,0,0,0,0]
    cif2 = [0,0,0,0,0,0,0,0,0,0]

    if n1<0:
        n1 = n1 *(-1)
    if n2 <0:
        n2 = n2 * (-1)
    
    while n1:                        
        ultima_cifra = int(n1 % 10)
        cif1[ ultima_cifra ] += 1
        n1 //= 10
    while n2:
        ultima_cifra = int(n2 % 10)
        cif2[ ultima_cifra ] += 1
        n2 //= 10
    for i in range(0,10):
        if cif1[i]!=0 and cif2[i]!=0:
            cfc =cfc +1

    if cfc >= 2:
        return True
    else:
        return False

def solve14(userList):
    # Cerinta 14 :  Secv. de lung. max. in care oricare doua elemente consecutive au cel putin 2 cifre distincte comune
    # date de intrare : userList - lista pe care se lucreaza
    # date de iesire : se afiseaza secventele cerute

    userList.append(0) #rezolva cazul cand ultima secventa se termina la sfarsitul listei initiale
    
    final_list = []
    new_l = [userList.pop(0)]
    for i,item in enumerate(userList):
        if cifrecomune(item,new_l[-1]) == False:
            final_list.append(new_l)
            new_l = [userList[i]]
        else :
            new_l.append(item)

    maxList = max(final_list , key = len)
    if len(maxList) > 1:
        for l in final_list:
            if len(l) == len(maxList):
                print(l)
    else:
        print([])    

    userList.pop()  

def tests_solve8():
    print("Teste proprietatea 8:")
    x = [1,2,3,4,5]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve8(x)
    print("------------------------------")
    x = [1,2,3,4,5,85,54,88,120,-96,-98]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve8(x)
    print("------------------------------")
    x = [1,2,3,45,1,2,3,-98,1,2,3,98]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve8(x)
    print("------------------------------")
    x = [11,12,13,14,15]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve8(x)
    print("------------------------------")
    x = [11,21,31,41,51,1,1,1]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve8(x)
    print("------------------------------")
    x = [-1,-2,-3,-4,-5]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve8(x)
    print("------------------------------")

def tests_solve14():
    print("Teste proprietatea 14:")
    x = [132,1232,3321,4,5]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve14(x)
    print("------------------------------")
    x = [998,998,3,4,5,85,889,898,120,-96,-98]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve14(x)
    print("------------------------------")
    x = [169,691,9666911.5,45,1,2,3,-98,1,2,3,98,619,6669911,11619]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve14(x)
    print("------------------------------")
    x = [11,12,13,14,15]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve14(x)
    print("------------------------------")
    x = [11,21,31,41,51,1122,2211,1212]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve14(x)
    print("------------------------------")
    x = [-1,-2,-355,-35,-533]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve14(x)
    print("------------------------------")   

def isPrime(n):
    #functia afla daca un numar este prim
    #date de intrare : n - numar intreg
    #date de iesire : True, daca n este prim si False in caz contrar
    #daca n este un nr negativ , se returzeaza False
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d = d + 2 
    return True 

def tests_isPrime():
    assert isPrime(1) == False
    assert isPrime(0) == False
    assert isPrime(17) == True
    assert isPrime(25) == False
    assert isPrime(44) == False
    assert isPrime(-5) == False
    assert isPrime(2) == True

def solve4(userList):
    # Cerinta 4 : Secv. de lung. max. ce au toate elementele numere prime
    # date de intrare : userList - lista pe care se lucreaza

    userList.append(-1) #rezolva cazul cand ultima secventa se termina la sfarsitul listei initiale
    
    final_list = []
    new_l = []
    for i in userList:
        if isPrime(i) == False:
            final_list.append(new_l)
            new_l = []
        else :
            new_l.append(i)

    maxList = max(final_list , key = len)
    if len(maxList) != 0:
        for l in final_list:
            if len(l) == len(maxList):
                print(l)
    else:
        print(maxList)    

    userList.pop()  

def tests_solve4():
    print("Teste proprietatea 4:")
    x = [22,13,17,4,8,55]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve4(x)
    print("------------------------------")
    x = [17,13,3,4,5,7,23,898,120,-96,-98]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve4(x)
    print("------------------------------")
    x = [17,13,25,5,45,1,2,3,-98,1,2,3,98,17,13,47]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve4(x)
    print("------------------------------")
    x = [6,12,20,14,15]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve4(x)
    print("------------------------------")
    x = [5,7,11,13,17,19,37,13]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve4(x)
    print("------------------------------")
    x = [-1,-2,-355,-35,-533]
    print("~~~Pentru ",x,"secventele cerute sunt:")
    solve4(x)
    print("------------------------------")

def userHelp():
    print("Comenzile acceptate sunt : ")
    print("ajutor - arata toate comenzile permise")
    print("stop - opreste programul")
    print("citire - citeste o lista introdusa de la tastatura")
    print("p8 - rezolva cerinta 8")
    print("p14 - rezolva cerinta 14")
    print("teste8 - exemple pentru cerinta 8")
    print("teste14 - exemple pentru cerinta 14")
    
def run():
    #programul principal
    print("Tastati comanda ‘ajutor’ pentru a afla toate comenzile premise sau introduceti o comanda dintre cele premise.")
    userList = []
    tests_isPrime()
    while True:
        cmd = input(">>>")
        if cmd == "stop":
            print("Iesire")
            return
        elif cmd == "ajutor":
            userHelp()
        elif cmd == "citire":
            read(userList)
        elif cmd ==  "p8":
            noListRead(solve8,userList)
        elif cmd == "p14":
            noListRead(solve14,userList)
        elif cmd == 'test8':
            tests_solve8()
        elif cmd == 'test14':
            tests_solve14()
        elif cmd == 'p4':
            noListRead(solve4,userList)
        elif cmd == 'test4':
            tests_solve4()
        else:
            print("Comanda nu exista,incercati 'ajutor' ")

run()
