def printPat(n):
    #Code here
    stri = ""
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            for k in range(i):
                stri += str(j) + " "
        stri += "$"
    print(stri)
