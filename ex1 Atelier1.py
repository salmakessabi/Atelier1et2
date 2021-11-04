# exercice 1
def factoriel(n):
    #declarer la fonction qui calcule le factoriel
    if n==1 :
        return 1
    elif n==0:
        print("donner un nombre superieur a zero")
    else:
        factoriel=1
        while n >1 :
            factoriel *=n
            n= n-1
        return factoriel
SOM= 1 + factoriel(5)/5 + factoriel(4)/4  +  factoriel(3)/3 +  factoriel(2)/2
