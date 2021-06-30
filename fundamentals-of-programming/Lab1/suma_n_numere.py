
def suma_numere():  
    # Functia calculeaza si afiseaza suma a n numere intregi introduse de catre utilizator
    # Date de intrare : n (cardinalul multimii numerelor introduse) si cele n numerele(in variabila x)
    # Date de iesire :  s (suma celor n numere)   

    s = 0
    n = input("Introduceti cate numere doriti sa insumati : ")
    n = int(n)

    while n <= 0:
        n = input("Input invalid. Introduceti un numar natural strict pozitiv")
        n = int(n)

    print("Introduceti cele ",n," numere,apasand tasta enter dupa includerea fiecaruia.")
    for i in range(1,n+1,1):
        x = input()
        x = int(x)
        s = s + x
    
    print("Suma numerelor introduse este ",s)



suma_numere()







