class student :
    roll= " "
    gpa= " "
    def _init_(self, roll, gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
         print(f"roll:{self.roll},gpa={self.gpa}")

rahim = student (101,3.57)
rahim.display()

karim = student (102,3.80)
karim.display ()
