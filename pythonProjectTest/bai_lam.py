# nạp thư viện toán học
import math

# định nghĩa lớp Point2D
class Point:
    def __init__(self, x=0, y=0): 
        self.x = x
        self.y = y
    
    # phương thức tính khoảng cách đến một điểm khác
    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    # phương thức in tọa độ của điểm
    def print_info(self):
        print("({},{})".format(self.x, self.y))

# tạo danh sách các điểm
n = int(input("Nhập số điểm trong mặt phẳng: "))
point_list = []
# nhập tọa độ từng điểm và đưa vào danh sách
for i in range(n):
    print("nhập điểm thứ {}:".format(i+1))
    x = int(input("x = "))
    y = int(input("y = "))
    p = Point(x, y) 
    point_list.append(p)
      
# a) in ra ds các điểm đã nhập
print("a) In ra danh sách các điểm đã nhập:")
for p in point_list:
    p.print_info()

# b) tìm điểm ở xa gốc tọa độ nhất
goc_toa_do = Point(0, 0)
max_distance = point_list[0].distance(goc_toa_do)
max_point = point_list[0]

for p in point_list[1:]:
    dist = p.distance(goc_toa_do)
    if dist > max_distance:
        max_distance = dist
        max_point = p

# in ra điểm xa nhất
print("b) Điểm xa gốc tọa độ nhất là: ")
max_point.print_info()    

# c) Tìm cặp điểm ở gần nhau nhất
min_distance = float('inf')
closest_pair = None

for i in range(len(point_list)):
    for j in range (i+1, len(point_list)):
        dist = Point.distance(point_list[i], point_list[j])
        if dist < min_distance:
            min_distance = dist
            closest_pair = point_list[i], point_list[j]

# In ra cặp điểm gần nhau nhất
print("c) Cặp điểm gần nhau nhất là:")
closest_pair[0].print_info()
closest_pair[1].print_info()
print("Khoảng cách giữa hai điểm: ", min_distance)
