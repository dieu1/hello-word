a = int(input('nhập vào chiều dài: '))
b = int(input('nhập vào chiều rộng: '))

def ucln(m, n):
    while n != 0:
        temp = m
        m = n
        n = temp % n
    return m

def viengach():
    return ucln(a, b)

def soluongviengach():
    dientichmanhsan = a * b
    dientichviengach = ucln(a, b) ** 2
    return dientichmanhsan / dientichviengach

print(f'viên gạch {viengach()} cm X {viengach()} cm')
print(f'số lượng viên gạch cần dùng để lát hết xân là: {soluongviengach()}')