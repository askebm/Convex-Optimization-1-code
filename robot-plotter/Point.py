
class Point(object):
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y
	# adding two pos 
	def __add__(self, o): 
		return self.a + o.a  
