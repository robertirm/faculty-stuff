"""
9.
Se dau coordonatele pentru n puncte în plan. Determinați toate mulţimile de puncte cu
proprietatea că cel puţin trei puncte din mulţime sunt colineare. Tipăriţi un mesaj dacă
problema nu are soluţie.

"""

def consistent(sol, dim):
    n = len(sol)
    if n == 1:
        return True

    return sol[n-2] < sol[n-1]

 
def solution(dim, puncte, sol):
    if len(sol) < 3:
        return False
    puncte_actuale = []
    for i in sol:
        puncte_actuale.append(puncte[i])
    n = len(puncte_actuale)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k:
                    if isCollinear(puncte_actuale[i] , puncte_actuale[j], puncte_actuale[k]):
                        return True
    return False


def isCollinear(a,b,c):
    aria = a['X']*(b['Y']-c['Y']) + b['X']*(c['Y']-a['Y']) + c['X']*(a['Y']-b['Y'])
    return aria == 0


def solutionFound(dim, puncte, sol):
    global gasit_solutie
    gasit_solutie = True
    multime = ''
    for i in sol:
        punct = '(' + str(puncte[i]['X']) + ',' + str(puncte[i]['Y']) + ')'
        multime += punct + ' , '
    multime = multime[:-3]
    print(multime)


def back_recursiv(dim , puncte, sol):
    sol.append(0)
    for i in range(dim):
        sol[-1] = i
        if consistent(sol, dim):
            if solution(dim, puncte, sol):
                solutionFound(dim, puncte, sol)
            back_recursiv(dim, puncte, sol)
    sol.pop()

def back_iterativ(dim, puncte, sol):
    sol.append(-1)
    while len(sol) > 0:
        choosed = False
        while not choosed and sol[-1] < dim-1:
            sol[-1] = sol[-1] + 1
            choosed = consistent(sol, dim)
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
    
    #back_recursiv(dim, puncte, sol)
    back_iterativ(dim, puncte, sol)

    if gasit_solutie == False:
        print("Nu exista solutie!")


main()