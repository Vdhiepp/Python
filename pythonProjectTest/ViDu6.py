#Một máy ATM có các loại tiền: 100, 20 và 5 USD. Một người cần rút số tiền m.
##a, Tìm phương án rút tốt nhất (có ít tờ tiền nhất)
##b, Liệt kê tất cả các cách rút được số tiền m. Có tất cả bao nhiêu cách?

##Lặp lại nhập số tiền cho đến khi thỏa điều kiện
while True:
    m = int(input("Nhập số tiền cần rút: "))
    if m <= 0 or m % 5 != 0 :
        print("Số tiền không thỏa mãn.")
    else:
        break
##a, Tìm phương án tốt nhất
### Cách làm: ưu tiên rút mệnh giá cao trước
soTo100 = m // 100  #chia lấy phần nguyên
m = m % 100         #số tiền còn lại
soTo20 = m // 20
m = m % 20          #số tiền còn lại
soTo5 = m // 5
###In kết quả
print("Phương án rút tiền tốt nhất: ")
print("{} tờ 100 + {} tờ 20 + {} tờ 5.".format(soTo100,soTo20,soTo5))

