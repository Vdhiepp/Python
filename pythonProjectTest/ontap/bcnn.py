while True:
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    if a > 0 and b > 0:
        break

def tinh_bcnn(a, b):
    maxab = max(a, b)
    while True:
        if maxab % a == 0 and maxab % b == 0:
            return maxab
        maxab += 1

if __name__ == "__main__":
    bcnn = tinh_bcnn(a, b)
    print("BCNN: ", bcnn)