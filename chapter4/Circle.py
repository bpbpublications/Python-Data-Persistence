class circle(ellipse):
        def __init__(self, r1, r2=None):
                super().__init__(r1,r2)
                self.radius2=self.radius1
        def area(self):
                area=math.pi*pow(self.radius1,2)
                return area
        def perimeter(self):
                perimeter=2*math.pi*self.radius1
                return perimeter
