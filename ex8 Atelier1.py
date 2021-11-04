#exercice8
all_freq = {}
test_str=str(input("donner svp le mot"))
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(" les nom de caractere de ce mot est  :\n "
              + str(all_freq))
