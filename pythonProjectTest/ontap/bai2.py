while True:
    n = int(input("Nhap vao so nguyen n: "))
    if 0 < n < 1000:
        break

def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("So nguyen to < ", n)
    for i in range (2, n+1):
        if LaSNT(i):
            print("{}".format(i), end=" ")
    print("")
    for i in range(2, n + 1):
        if LaSNT(i):
            print("%d" % i, end=" ")
    print("")
    for i in range(2, n + 1):
        if LaSNT(i):
            print(f"{i}", end=" ")
