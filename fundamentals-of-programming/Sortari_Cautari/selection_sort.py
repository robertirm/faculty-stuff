"""
    SELECTION SORT

    Se determina elementul avand cea mai mica cheie si se interschimba cu cel de pe prima pozitie
    Procesul este reluat pana cand toate elementele au fost considerate

    Complexitate:
    ~ ca timp
        nr total de comparatii : n(n-1) / 2 ---------> θ(n^2)
        caz favorabil = caz defavorabil = caz mdeiu
            complexitate generala = O(n^2)
    ~ ca spatiu
        algoritm in-place
        memoria necesara este θ(1)

"""

from operator import lt


def selectionSort(lista, *, key = lambda x: x , reverse=False, cmp=lt):
    for i in range(0, len(lista)-1):
        ind = i 

        # cautam cel mai mic element din restul listei
        for j in range(i+1, len(lista)):
            if reverse == False:
                if cmp(key(lista[j]) , key(lista[ind])):
                    ind = j
            else:
                if not cmp(key(lista[j]) , key(lista[ind])):
                    ind = j

        # si il intershimbam cu primul
        if i < ind:
            lista[i],lista[ind] = lista[ind],lista[i]

 
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
    selectionSort(lista)
    print(lista)

test()