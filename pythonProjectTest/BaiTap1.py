#Nhập 1 số nguyên dương n thỏa 0<n<=1000
#a, kiểm tra n có phải số nguyên tố
#b, In ra các số nguyên tố <= n

while True:
    n = int(input("Nhập số nguyên n: "))
    if n > 0 and n <= 1000:
        break

#Định nghĩa hàm kiểm tra số tự nhiên có phải SNT hay ko?
def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

#a,
if LaSNT(n):
    print("{} là số nguyên tố".format(n))
else:
    print("{} không phải là số nguyên tố".format(n))

#b,
print("Các số nguyên tố <= {}:".format(n))
for i in range(2, n+1):
    if LaSNT(i):
        print("%d" % i, end=" ")