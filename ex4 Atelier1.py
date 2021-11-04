#Exercice4
def fibonnaci ( N ) :
    if N<2 :
        return N
    else :
        return fibonnaci(N-1) + fibonnaci(N-2)
def calculator():
 print("donner une valeur")
 N=int( input ("la valeux de n est"))
 i=0
 while i<=N :
    print(fibonnaci(i))
    i=i+1
print(calculator())
def comp_chiffre(n):
    if n/10 < 1 :
        return 1
    else:
                  return 1 + comp_chiffre(n/10)
