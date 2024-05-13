import datetime

class Xe:
    # Thuộc tính tĩnh
    max_nam_luu_hanh = 20

    def __init__(self, bien_so, hang_san_xuat, nam_san_xuat=None):
        self.bien_so = bien_so
        self.hang_san_xuat = hang_san_xuat
        if nam_san_xuat is None:
            self.nam_san_xuat = datetime.datetime.now().year
        else:
            self.nam_san_xuat = nam_san_xuat

    def nhap_thong_tin(self):
        self.bien_so = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 2 ký tự số): ")
        self.hang_san_xuat = input("Nhập hãng sản xuất: ")
        self.nam_san_xuat = int(input("Nhập năm sản xuất: "))

    def xuat_thong_tin(self):
        print("Biển số:", self.bien_so)
        print("Hãng sản xuất:", self.hang_san_xuat)
        print("Năm sản xuất:", self.nam_san_xuat)
        print("Số năm lưu hành:", self.tinh_so_nam_luu_hanh())

    def tinh_so_nam_luu_hanh(self):
        current_year = datetime.datetime.now().year
        return current_year - self.nam_san_xuat


# Chương trình chính
def main():
    danh_sach_xe = []
    n = int(input("Nhập số lượng xe: "))

    # Nhập thông tin xe
    for i in range(n):
        print(f"Nhập thông tin cho xe thứ {i + 1}:")
        xe = Xe('', '')
        xe.nhap_thong_tin()
        danh_sach_xe.append(xe)

    # In ra thông tin các xe có thời gian lưu hành dài nhất
    max_nam_luu_hanh = max(xe.tinh_so_nam_luu_hanh() for xe in danh_sach_xe)
    print("\nThông tin các xe có thời gian lưu hành dài nhất:")
    for xe in danh_sach_xe:
        if xe.tinh_so_nam_luu_hanh() == max_nam_luu_hanh:
            xe.xuat_thong_tin()

    # Xóa các xe có biển số bắt đầu bằng '79'
    danh_sach_xe = [xe for xe in danh_sach_xe if not xe.bien_so.startswith('79')]

    print("\nDanh sách xe sau khi xóa các xe có biển số bắt đầu bằng '79':")
    for xe in danh_sach_xe:
        xe.xuat_thong_tin()


if __name__ == "__main__":
    main()