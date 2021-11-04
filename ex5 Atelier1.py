#Exercice5
def comp_chiffre(n):
    if n/10 < 1 :
        return 1
    else:
        return 1+comp_chiffre(n/10)
n=int(input("donner la valuer du nombre"))
print(comp_chiffre(n))
