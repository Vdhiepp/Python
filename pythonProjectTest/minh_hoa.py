# cài đặt lớp Student mô tả các đối tượng sinh viên
class Student:
    # hàm thiết lập (constructor)
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
    
    # hàm in thông tin
    def print_info(self):
        print("ID: " + self.id)
        print("Name: " + self.name)
        print("Grade: " + str(self.grade))

# khởi tạo một đối tượng sinh viên
sv1 = Student("63134128", "Lê Văn A", 8.88)

print(sv1.id)
print(sv1.name)
print(sv1.grade)

# gọi hàm in thông tin sv
sv1.print_info()
    