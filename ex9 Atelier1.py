#exercice9
def chercheur_delement(mat, n, x):
    if (n == 0):
        return -1
    for i in range(n):
        for j in range(n):
            if (mat[i][j] == x):
                print(" l'element est trouve a (", i, ",", j, ")")
                return 1
    print(" l'element n'existe pas ")
    return 0
