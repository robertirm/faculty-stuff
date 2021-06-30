from operator import gt


def bubble_sort(lista, *, key=lambda x: x, reverse=False, cmp=gt):
    newlist = lista[:]
    n = len(newlist)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if cmp(key(newlist[j]), key(newlist[j+1])):
                newlist[j], newlist[j+1] = newlist[j+1], newlist[j]
    if reverse:
        return reversed(newlist)
    else:
        return newlist


def shell_sort(lista, *, key=lambda x: x, reverse=False, cmp=gt):
    newlist = lista[:]
    n = len(newlist)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            aux = newlist[i]
            j = i
            while j >= gap and cmp(key(newlist[j-gap]), key(aux)):
                newlist[j] = newlist[j-gap]
                j = j - gap
            newlist[j] = aux
        gap = gap//2

    if reverse:
        return reversed(newlist)
    else:
        return newlist


def cmp_combinat(obj1, obj2):
    # medie apoi nume
    if obj1.get_medie() > obj2.get_medie():
        return True
    elif obj1.get_medie() == obj2.get_medie():
        if obj1.get_student() < obj2.get_student():
            return True
        else:
            return False
    else:
        return False

