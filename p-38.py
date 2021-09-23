class triangle :

    def _init_(self, base, height):
        self.base=base
        self.height=height
    def calculate_area(self):
         area=0.5*self.base*self.height
         print("area=",area)

t1=triangle(10,20)
t1.calculate_area( )
