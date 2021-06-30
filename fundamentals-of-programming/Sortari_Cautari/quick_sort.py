"""
    QUICK SORT

    Bazat pe “divide and conquer”
    -Divide: se împarte lista în 2 astfel încât elementele din dreapta pivotului sunt
        mai mici decât elementele din stânga pivotului.
    -Conquer: se sortează cele două subliste
    -Combine: trivial – dacă partiționarea se face în același listă

    Complexitate:
    ~ca timp
        caz favorabil: partitionarea exact la mijloc T(n) = 2*T(n/2) + θ(n) ---> θ(n*logn)
        caz defavorabil: partitionarea tot timpul rezulta intr-o partitie cu un singur elementi si o partitie cu n-1 elemente
        caz mediu: θ(n* log2(n)) 

"""

def partition(lista, left , right):
    pivot = lista[left]
    i = left
    j = right
    while i != j:
        while lista[j] >= pivot and i<j:
            j = j - 1
        lista[i] = lista[j]
        while lista[i] <= pivot and i<j:
            i = i + 1
        lista[j] = lista[i]
    lista[i] = pivot
    return i

def quicksort(lista,left,right):
    pos = partition(lista, left, right)

    if left < pos-1:
        quicksort(lista, left, pos-1)
    if pos+1 < right:
        quicksort(lista, pos+1, right)

lista = [5,24,8,6,54,984,5,5,8,2,19,98,95,1]
quicksort(lista, 0, len(lista)-1)
print(lista)