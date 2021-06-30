def longestSublist(a):

    lung = len(a)

    # construim sirul l si p
    l = [0]*lung
    p = [0]*lung

    l[lung - 1] = 1 
    p[lung - 1] = -1

    for k in range(lung-2,-1,-1):
        p[k] = -1
        l[k] = 1
        for i in range(k+1,lung):
            if a[i] >= a[k] and l[k] < l[i] + 1:
                l[k] = l[i] + 1
                p[k] = i

    # determinam lungimea maxima posibila
    j = 0
    for i in range(0,lung):
        if l[j] < l[i]:
            j = i

    # contruim sublista
    rez = []
    while j != -1:
        rez = rez + [a[j]]
        j = p[j]

    return rez   

print(longestSublist([3,2,3,1,4,5,6,8,5]))