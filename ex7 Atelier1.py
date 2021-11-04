#exercice7
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
s = "cacheter"
print(" la chaine de carractere est  : ", end="")
print(s)

print(" le reverse de cette chaine est : ", end="")
print(reverse(s))
