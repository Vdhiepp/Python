#Viết hàm tính tổng số nguyên
def Sum(*n):
    s = 0
    for i in n:
        s += i
    return s

a, b = 5, 10
c = Sum(a, b, 34)
print(c)
