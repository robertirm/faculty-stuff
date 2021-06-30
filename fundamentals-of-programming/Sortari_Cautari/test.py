def divide(lista):
    # maxim din lista
    if len(lista) == 1:
            return lista[0]
        
    mid = len(lista) // 2
    max1 = divide(lista[:mid])
    max2 = divide(lista[mid:])
    if max1 < max2:
        return max2
    else:
        return max1


lista = [2,5,6,1,8,2,5,9]
print(divide(lista))