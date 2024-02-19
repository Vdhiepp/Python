#Nhập 1 năm dương lịch đổi ra năm âm lịch
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Binh', 'Đinh', 'Mậu', 'Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mẹo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
#Nhập năm dương lịch
namDL = int(input("Nhập năm dương lịch: "))
#Tính can
can1 = namDL % 10
#Tính chi
chi1 = namDL % 12
#Đổi ra năm âm lịch
namAL = can[can1] + " " + chi[chi1]
print(namAL)
