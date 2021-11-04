
#exercice3
n= int(input("donner la longeur de votre liste svp"))
maliste = []
for i in range(n):
    maliste.append(int(input("Entrer la valeur :")))
print("liste est " , maliste)
def Compteurdoccurence(my_list):
    count = {}
    for i in maliste :
        count[i] = count.get(i, 0) + 1
    return count
print(Compteurdoccurence(maliste))
