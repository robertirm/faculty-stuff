"""
    BUBBLE SORT

    Compara elementele consecutive ,daca nu sunt in ordinea dorita le interschimbam
    Procesul de comparare continua pana cand nu mai avem elemente consecutive ce trebuie 
    interschimbate(toate perechile respecta relatia de ordine data)

    Complexitate:
    ~ ca timp
        -caz defavorabil: θ(n^2) lista este sortata descrescator
        -caz mediu: θ(n^2)
        -caz favorabil: θ(n) lista este sortata
            complexitate generala: O(n^2)
    ~ca spatiu
        -in-place -> θ(1)
""" 

from operator import lt

def bubbleSort(lista, *, key = lambda x :x, reverse=False, cmp =lt):
    for i in range(len(lista)-1):
        for j in range(0, len(lista)-i-1):

            if reverse==False:
                if cmp(key(lista[j+1]), key(lista[j])):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
                if not cmp(key(lista[j+1]), key(lista[j])):
                    lista[j], lista[j+1] = lista[j+1], lista[j]



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
    bubbleSort(lista,cmp=comparatie,reverse=True)
    print(lista)

test()