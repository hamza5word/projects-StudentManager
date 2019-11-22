class Point :
    """
    Class Point Attributes :
    x
    y
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point("+str(self.x)+","+str(self.y)+")"

class Pixel(Point) :
    def __init__(self, x=0, y=0, color=0):
        Point.__init__(self,x,y)
        self.color = color

    def __repr__(self):
        return Point.__repr__(self) + " Color : "+str(self.color)

if __name__ == '__main__':
        p = Point(2,5)
        print(p)