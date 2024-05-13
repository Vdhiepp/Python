class Personel:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        self.__Salary = None
    def PrintInfo(self):
        print('Name: {}, Age: {}'.format(self.Name, self.Age))

if __name__ == '__main__':
    p1 = Personel('Tony', 35)
    p1.PrintInfo()
    print(p1.Name)
    