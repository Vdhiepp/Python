#Viết chương trình có các hàm sau:
##a, Hàm kiểm tra 1 số tự nhiên có phải số nguyên tố hay không?
##b, Hàm in ra các số nguyên tố <= n. Sử dụng hàm ở câu a.
##c, Hàm tìm SNT nhỏ nhất > n.

def LaSNT(n):
    #Nếu n < 2 thì không phải SNT
    if n < 2 : return False
    #Nếu n >= 2 thì: nếu trong đoạn [2,n//2] có 1 ước số của n thì n không phải SNT
    for i in range(2, n//2 + 1):
        if n % i == 0: return False
    #Nếu không phải 2 trường hợp trên ->n là SNT
    return True

def InSNT(n):
    for i in range(2, n + 1):
        if LaSNT(i):
            print("%d" % i, end=" ")

def TimSNT(n):
    i = n + 1
    while not LaSNT(i):
        i += 1
    return i

#Chương trình chính
if __name__ == '__main__':
    n = 37
    print(LaSNT(n))
    print("Các số nguyên tố nhỏ hơn hoặc bằng {}:".format(n))
    InSNT(n)
    print("\nSố nguyên tố nhỏ nhất lớn hơn {} là {}".format(n, TimSNT(n)))
