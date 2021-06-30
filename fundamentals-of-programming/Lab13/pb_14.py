"""
14.
Se dă o listă de numere întregi a1,...an. 
Generaţi toate permutările listei pentru care numerele au aspect de vale (descresc până la un punct de unde cresc).

"""

def consistent(sol, dim):
    for i in range(0, len(sol)-1):
        if sol[i] == sol[-1]:
            return False 
    return True


def solution(dim, lista, sol):
    if dim != len(sol):
        return False
    
    perm = sol[:]
    for i in range(dim):
        perm[i] = lista[sol[i]]

    m = min(perm)
    for i in range(dim):
        if perm[i] == m:
            index = i
            break

    i = 1
    while i <= index:
        if perm[i-1] < perm[i]:
            return False
        i += 1

    while i < dim:
        if perm[i-1] > perm[i]:
            return False
        i += 1

    return True


def solutionFound(dim, lista, sol):
    for i in range(dim-1):
        print(lista[sol[i]], end=' ')
    print(lista[sol[dim-1]], end='\n')


def back_recursiv(dim , lista, sol):
    sol.append(0)
    for i in range(dim):
        sol[-1] = i
        if consistent(sol, dim):
            if solution(dim, lista, sol):
                solutionFound(dim, lista, sol)
            back_recursiv(dim, lista, sol)
    sol.pop()


def main():
    print("Introduceti lista:")
    lista = list(map(int, input().split()))
    dim = len(lista)
    sol = []
    print("Solutii:")
    back_recursiv(dim , lista, sol)


main()