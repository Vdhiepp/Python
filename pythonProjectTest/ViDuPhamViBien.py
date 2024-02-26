def MyFunc():
    x = 100
#Gọi hàm MyFunc
MyFunc()
#Thử đọc giá trị biến x
#print('x = %d' % x)

def MyFunc2():
    global x2
    x2 = 100

#Gọi hàm MyFunc2
MyFunc2()

#Thử đọc giá trị biến x2
print('x2 = %d' % x2)