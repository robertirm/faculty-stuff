import math #pentru functia radical

def verificare_nr_prim(x):
    #Functia afla daca numarul transmis este prim sau nu
    #Date de intrare : x - numarul introdus de utilizator
    #Date de iesire : true daca x este prim , false in caz contrar
    
    if x <= 1:
        return True
    elif x%2 == 0:
        return False
    else:
        radical = int(math.sqrt(x))
        for i in range( 3 , radical ):
            if x % i == 0:
                print(i)
                return False
    return True

#citirea  si validarea datelor de intrare
n = input("Introduceti un numar natural:")
n = int(n)
while n <= 0:
    n = input("Input invalid.Introduceti un numar natural nenul:")
    n = int(n)

# afisarea raspunsului
if bool(verificare_nr_prim(n)) == True:
    print("Numarul ",n," este prim.")
else:
    print("Numarul ",n," nu este prim.")
