def cmmdc_2_nr(a,b):
    
    #Functia s cmmdc-ul pentru doua numere
    #Date de intrare : a,b (numerele introduse)
    #Date de iesire : se returneaza cmmdc-ul lor
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    # se utilizeaza algoritmul lui Euclid prin scaderi repetate
    while a!=b :
        if a > b:
            a = a-b
        else :
            b = b-a
    
    return a


a = input("Introduceti primul numar:")
a = int(a)
while a < 0:
    a = input("Input invalid. Introduceti un numar natural.")
    a = input()
    
b = input("Introduceti al doilea numar:")
b = int(b)
while a < 0:
    b = input("Input invalid. Introduceti un numar natural.")
    b = input()

print("Cel mai mare divizor comun este ", cmmdc_2_nr(a,b))