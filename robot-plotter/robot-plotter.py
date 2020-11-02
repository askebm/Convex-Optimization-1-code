

import numpy as np
import matplotlib.pyplot as plt
from Point import Point

q_angle = np.array([ np.pi/4 , -np.pi/8 , -np.pi/8 ])
links   = np.array([10,10,10])
base    = Point(0,0)

j1      = Point( 
		base.x + links[0] * np.cos(q_angle[0]), 
		base.y + links[0] * np.sin(q_angle[0]) )

j2      = Point( 
		j1.x + links[1] * np.cos( q_angle[0] + q_angle[1] ), 
		j1.y + links[1] * np.sin(q_angle[0] + q_angle[1]) )


j3      = Point( 
		j2.x + links[2] * np.cos( q_angle[1] + q_angle[2] ), 
		j2.y + links[2] * np.sin(q_angle[1] + q_angle[2]) )

joints  = np.array([j1,j2,j3])

for joint in joints:
	print(joint.x,joint.y)

x_axis = np.array([base.x,j1.x,j2.x,j3.x])
y_axis = np.array([base.y,j1.y,j2.y,j3.y])
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.plot(x_axis,y_axis)
print("x_axis : ",x_axis)
print("y_axis : ",y_axis)
plt.show()








