#Khai báo lớp tkinter
import tkinter as tk
#Tạo cửa sổ
window = tk.Tk()
#Thêm nhãn chứa câu "Hello"
greeting = tk.Label(text="Hello, Tkinter Hello, Tkinter Hello, Tkinter Hello, Tkinter")
#Đưa nhãn vào window
greeting.pack()
#Chạy Tkinter event loop
window.mainloop()