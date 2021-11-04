#exercice3
def somme (x):
    if x==0:
        return 0
    else:
        return x+ somme(x - 1 )
x=int (input ("donner la valeur du nom"))
print("la somme est ", somme(x))
