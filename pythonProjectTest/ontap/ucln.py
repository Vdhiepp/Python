while True:
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    if a > 0 and b > 0:
        break

def tinh_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    Ucln = tinh_ucln(a, b)
    print("UCLN: ", Ucln)