from tkinter import *

def bmi_calculator():
    height = float(h_entry.get())
    weight = float(w_entry.get())
    bmi = weight/(height**2)
    output_label.configure(text='BMI: {:.1f}'.format(bmi))
    if bmi < 18.5:
        status = "Suy dinh dưỡng"
    elif 18.5 <= bmi < 25:
        status = "Bình thường"
    elif 25 <= bmi < 30:
        status = "Hơi béo phì"
    else:
        status = "Béo phì"

    output_label_status.configure(text='Trạng thái: {}'.format(status))

root = Tk()
root.title('BMI Calculator')
root.geometry("400x200")

h_mess_label = Label(text="Nhập chiều cao(m)", font={'Verdana', 16})
w_mess_label = Label(text="Nhập cân nặng(kg)", font={'Verdana', 16})
output_label = Label(font={'Verdana', 16})
output_label_status = Label(font={'Verdana', 16})

h_entry = Entry(font={'Verdana', 16}, width=4)
w_entry = Entry(font={'Verdana', 16}, width=4)

calc_button = Button(text='Tính', font={'Verdana', 16}, command=bmi_calculator)

#Sắp xếp vị trí
h_mess_label.grid(row=0, column=0)
w_mess_label.grid(row=1, column=0)
h_entry.grid(row=0, column=1)
w_entry.grid(row=1, column=1)
calc_button.grid(row=0, column=2, rowspan=2)
output_label.grid(row=2, column=0, rowspan=2)
output_label_status.grid(row=3, column=1, columnspan=3)

#Chạy Tkinter event loop
mainloop()