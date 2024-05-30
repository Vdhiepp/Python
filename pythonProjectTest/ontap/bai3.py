class NhanVien:
    def __init__(self, ma, namsinh):
        self.ma = ma
        self.namsinh = namsinh

    def tinhTuoi(self, namhientai):
        return namhientai - self.namsinh


def nhapds(n):
    ds = []
    for _ in range(n):
        ma = int(input("Nhap ma: "))
        namsinh = int(input("Nam sinh: "))
        nhanvien = NhanVien(ma, namsinh)
        ds.append(nhanvien)
    return ds


def inds(ds):
    for nhanvien in ds:
        print("Ma:", nhanvien.ma)
        print("Nam sinh:", nhanvien.namsinh)
        print("Tuoi: ", nhanvien.tinhTuoi(2024))

if __name__ == "__main__":
    n = int(input("Nhap so luong nhan vien: "))
    dsnv = nhapds(n)
    inds(dsnv)
