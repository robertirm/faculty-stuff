"""
    INSERTION SORT

    Se parcurg elementele. Se insereaza elementul curent pe pozitia corecta in subsecventa deja sortata
    In subsecventa ce contine elementele deja sortate se tin elementele sortate se tin elementele sortate 
    pe parcursul algoritmului, astfel dupa ce parcurgem toate elementele secventa este sortata in intregime.

    Complexitate:
    ~ ca timp
            caz defavorabil: nr max de iteratii cand lista este ordonata descrescator
                    T(n) = n(n-1) / 2 ---> θ(n^2)
            caz mediu:  θ(n^2)
            caz favorabil : lista e sortata ---> θ(n)
                    complexitate generala = O(n^2)

    ~ ca spatiu ---> θ(1)

"""


from operator import lt

def insertSort(lista , *, key = lambda x :x , reverse=False,cmp =lt):

    for i in range(1, len(lista)):
        ind = i-1
        a = key(lista[i])

        if reverse == False:
            while ind >= 0 and cmp(a , key(lista[ind])):
                lista[ind + 1] = lista [ind]
                ind = ind - 1

        else:
            while ind >= 0 and not cmp(a , key(lista[ind])):
                lista[ind + 1] = lista [ind]
                ind = ind - 1
        
        lista[ind+1] = a



def sumaCifrelor(n):
    s = 0
    while n:
        s = s + n % 10
        n = n//10
    return s

def comparatie(x,y):
    return sumaCifrelor(x) < sumaCifrelor(y)

def test():
    lista = [13,65,2,78,51,21,69,8,32,55]
    insertSort(lista,cmp=comparatie,reverse=True)
    print(lista)

test()