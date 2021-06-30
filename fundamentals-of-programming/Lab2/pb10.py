'''10.Pentru un număr natural n dat găsiți numărul natural minim m format cu
aceleași cifre. Ex. n=3658, m=3568.'''

def nr_min_aceleasi_cifre(n):
    cifre = [0,0,0,0,0,0,0,0,0,0]    
    n = int(n)

    # parcurgem cifrele de la dreapta la stanga si le contorizam
    while n:                        
        ultima_cifra = int(n % 10)
        cifre[ ultima_cifra ] += 1
        n //= 10
       
    # daca in nr initial apare cifra 0 , aceasta nu va fi prima cifra din noul nr
    m = 0      #numarul nou format                   
    if cifre[0] > 0:
        ind = 1
        while cifre[ ind ] == 0:
            ind += 1
        m = ind
        cifre[ ind ] -= 1

    # parcurgem lista "cifre" de la stanga la dreapta si construim noul nr prin
    # adaugarea cifrei "i" de "cifre[i]" ori  
    for i in range(10):           
        while cifre[ i ] > 0:    
            m = m * 10 + i
            cifre[ i ] -= 1
        
    return m


x = input("Introduceti un numar natural : ")

# verificare date de intrare
while x.isdigit() == False:     
    x = input("Input invalid. Introduceti un numar natural : ")
    
# output    
print("Cel mai mic numar ce poate fi realizat cu cifrele numarului introdus este " , nr_min_aceleasi_cifre(x))
