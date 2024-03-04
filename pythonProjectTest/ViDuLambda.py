#Tính tổng bình phương các số nguyeen liên tiếp <= n
#CHương chình chính
if __name__ == '__main__':
    n = 5
#Cách 1:
    s = 0
    for i in range(n + 1):
        s += i**2
    #In kết quả
    print("S = {}".format(s))
#Cách 2:
    def Square(x):
        return x**2
    s = 0
    for i in range (n + 1):
        s += Square(i)
    # In kết quả
    print("S = {}".format(s))
#Cách 3: Định nghĩa hàm Lambda
    s = 0
    for i in range (n + 1):
        x = lambda i : i*i
        s += x(i)
    # In kết quả
    print("S = {}".format(s))