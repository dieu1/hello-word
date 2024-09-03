def UCLN(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def Is_comp(m, n):
    if UCLN(m, n) == 1:
        return ('Hai số này có nguyên tố cùng nhau.')
    else:
        return ('Hai số này không có nguyên tố cùng nhau.')


m = int(input('Nhập vào số m: '))
n = int(input('Nhập vào số n: '))

print(Is_comp(m, n))
