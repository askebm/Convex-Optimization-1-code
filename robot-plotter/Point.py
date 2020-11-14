
class Point(object):
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.y = y
        self.x = x
        # adding two pos 
    def __add__(self, o): 
        return Point(self.x + o.x,self.y + o.y)
    def __repr__(self):
        return "{% s,% s}" % (self.x, self.y)  
