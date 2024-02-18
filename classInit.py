class Rectangle:
    length = 12
    width = 10

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def getArea(self):
        result = self.length * self.width
        return result
    
    def getPerimeter(self):
        result = self.length + self.width
        return result
    
r1 = Rectangle(12,10)

print(r1.getArea())
print(r1.getPerimeter())