while True:
    soKW = int(input("Nhap so KW: "))
    if soKW > 0:
        break

def TinhTienDien(soKW):
    if (soKW<=100):
        return soKW*100
    elif (soKW<=200):
        return 100*100+(soKW-100)*200
    else:
        return 100*100+100*200+(soKW-200)*300

if __name__ == "__main__":
    print(f"So tien dien phai tra la: {TinhTienDien(soKW)} VND")


