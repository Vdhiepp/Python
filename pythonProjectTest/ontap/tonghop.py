while True:
    n = int(input("Nhap so n: "))
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    soKW = int(input("Nhap so KW: "))
    if n > 0 and n < 1000 and soKW > 0:
        break
#Bai 1
def TinhTienDien(soKW):
    if (soKW<=100):
        return soKW*1500
    elif (soKW<=200):
        return 100*1500+(soKW-100)*1750
    else:
        return 100*1500+100*1750+(soKW-200)*2000

#Bai 2
def LaSNT(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def BCNN(a, b):
    max_ab = max(a, b)
    while True:
        if max_ab % a == 0 and max_ab % b == 0:
            return max_ab
        max_ab += 1

# Bai3
class NhanVien:
    def __init__(self, ma_nv, nam_sinh):
        self.ma_vn = ma_nv
        self.nam_sinh = nam_sinh
    def tinhTuoi(self, nam_hien_tai):
        return nam_hien_tai - self.nam_sinh

def NhapNhanVien(n):
    danh_sach = []
    for _ in range(n):
        ma_nv = int(input("Nhap ma nhan vien: "))
        nam_sinh = int(input("Nhap nam sinh: "))
        nhan_vien = NhanVien(ma_nv, nam_sinh)
        danh_sach.append(nhan_vien)
    return danh_sach

def InNhanVien(danh_sach):
    for nhan_vien in danh_sach:
        print("Ma nhan vien la: ", nhan_vien.ma_vn)
        print("Nam sinh nhan vien la: ", nhan_vien.nam_sinh)
        print("Tuoi nhan vien la: ", nhan_vien.tinhTuoi(2024))

#Main
if __name__ == "__main__":
    #Bai1
    print(f"So tien dien phai tra la: {TinhTienDien(soKW)} VND")

    #Bai2
    if LaSNT(n):
        print("{} la SNT".format(n))
    else: print("{} la SNT".format(n))

    print(f"Cac SNT < {n} la: ")
    for i in range(1, n+1):
        if LaSNT(i):
            print("%d " % i, end=" ")

    ucln = UCLN(a, b)
    print("\nUCLN cua {} va {} la {}".format(a, b, ucln))
    bcnn = BCNN(a, b)
    print(f"BCNN cua {a} va {b} la {bcnn}")

    #Bai3
    dsnv = NhapNhanVien(n)
    InNhanVien(dsnv)