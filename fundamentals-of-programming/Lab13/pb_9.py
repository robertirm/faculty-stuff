"""
9.
Se dau coordonatele pentru n puncte în plan. Determinați toate mulţimile de puncte cu
proprietatea că cel puţin trei puncte din mulţime sunt colineare. Tipăriţi un mesaj dacă
problema nu are soluţie.

"""
lista_solutii = []

def consistent(dim, sol):
    return len(sol) == dim
 

def solution(dim, puncte, sol):
    # construim o multime cu punctele alese
    puncte_actuale = []
    for i in range(len(sol)):
        if sol[i] == 1 or sol[i] == 0:
            puncte_actuale.append(puncte[i])
    n = len(puncte_actuale)
    # daca sunt mai putin de 3 elemente nu poate fi solutie
    if n < 3:
        return False
    
    # verificam daca exista 3 puncte sunt coliniare
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k:
                    if isCollinear(puncte_actuale[0] , puncte_actuale[1], puncte_actuale[2]):
                        return True

    return False


def solutionFound(dim, puncte, sol):
    global gasit_solutie
    gasit_solutie = True
    multime = ''
    for i in range(len(sol)):
        punct = '(' + str(puncte[i]['X']) + ',' + str(puncte[i]['Y']) + ')'
        multime += punct + ' , '
    multime = multime[:-3]
    print(multime)


def isCollinear(a,b,c):
    aria = a['X']*(b['Y']-c['Y']) + b['X']*(c['Y']-a['Y']) + c['X']*(a['Y']-b['Y'])
    return aria == 0


def back_recursiv(dim, puncte, sol):
    sol.append(0)
    for i in range(2):
        sol[-1] = i
        if consistent(dim, sol):
            if solution(dim, puncte, sol):
                solutionFound(dim, puncte, sol)
        else:
            back_recursiv(dim, puncte, sol)
    sol.pop()


def back_iterativ(dim, puncte, sol):
    sol.append(-1)
    while len(sol) > 0:
        choosed = False
        while not choosed and sol[-1] < 1:
            sol[-1] = sol[-1] + 1
            if len(sol) <= dim : choosed= True
            else: choosed:False
        if choosed:
            if solution(dim, puncte, sol):
                solutionFound(dim, puncte, sol)
            sol.append(-1)
        else:
            sol = sol[:-1]


def main():
    dim = int(input("Numarul de puncte in plan : "))
    puncte = []
    sol = []
    # citim coordonatele punctelor si le stocam intr-o lista de dicitonare 
    for i in range(dim):
        print("Punctul ", i+1) 
        x = int(input('x = ')) 
        y = int(input('y = '))
        puncte.append({'X':x , 'Y':y})
    
    global gasit_solutie
    gasit_solutie = False
    
    back_recursiv(dim, puncte, sol)
    #back_iterativ(dim, puncte, sol)

    if gasit_solutie == False:
        print("Nu exista solutie!")


main()

