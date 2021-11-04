
#Exercice1 Atelier2
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list() #declarer une liste vide
odd_elements = list1[1::2] #une liste qui commence par l'element de position 1 de la liste 1 et saute par 2
print("Element at odd-index positions from list one")
print(odd_elements)
even_elements = list2[0::2] #une liste qui commence par l'element de position 0 de la liste 2 et saute par 2
print("Element at even-index positions from list two")
print(even_elements)
 #donc la liste even-element prende les valeurs des element : 0,2,4,6
print("Printing Final third list")
res.extend(odd_elements) #ajouter les elements de la liste odd_element
res.extend(even_elements)
#ajouter les elements de la liste even_element apres avoir deja ajouter les element de odd_element
print(res)
