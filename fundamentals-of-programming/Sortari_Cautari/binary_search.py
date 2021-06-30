"""
    BINARY SEARCH

            / θ(1)          , n = 1
    T(n) = -
            \ T(n/2) + θ(1)  , altfel
    
    caz favorabil : θ(1)
    caz defavorabil : θ(log2(n))
    caz mediu : θ(log2(n))
        complexitate generala : O(log2(n))
"""


def binarySearch(lista, el):
    if len(lista) == 0:
        return 0
    if el < lista[0]:
        return 0
    if el >= lista[len(lista)-1]:
        return len(lista)
        
    right = len(lista)
    left = 0
    while right-left > 1:
        m = (left+right)//2

        if el <= lista[m]:
            right = m
        else:
            left = m
        
    return m


def test():
    lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    print(binarySearch(lista, 9))

test()