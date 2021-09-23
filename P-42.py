'''class A :
    def display1(self):
        print(" i am inside A class")
class B(A) :
    def display2(self):
        print(" i am inside B class")
class C(B) :
    def display3(self):
        super().display1()
        super().display2()
        print(" i am inside C class")
ob1=C()
ob1.display3()
'''
#magic method

class bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __str__(self):
         return(f"name={self.name},color={self.color}")
    def display (self):
        print(f"name={self.name},color={self.color}")
        bike1=bike("yamaha r15","blue")
        bike2=bike("yamaha fz","red")
        print(str(bike1))