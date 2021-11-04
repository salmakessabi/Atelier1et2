#exercice2
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')
if __name__ == '__main__':
    dec_val=int(input("donner la valeur du nombre decimal svp"))
    DecimalToBinary(dec_val)
