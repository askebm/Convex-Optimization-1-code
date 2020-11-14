import yaml
import numpy as np
import matplotlib.pyplot as plt
from Point import Point
 
with open('plt_conf.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

robot_angles    = config['joint_angles']
link_lengths    = config['link_lengths']
base            = Point(config['base'][0]['x'], config['base'][1]['y'])
 
j1      = Point( 
		base.x + link_lengths[0]['l1'] * np.cos( eval(robot_angles[0]['j1'])), 
		base.y + link_lengths[0]['l1'] * np.sin( eval(robot_angles[0]['j1'])) )

j2      = Point( 
		j1.x + link_lengths[1]['l2'] * np.cos( eval(robot_angles[0]['j1']) + eval(robot_angles[1]['j2']) ), 
		j1.y + link_lengths[1]['l2'] * np.sin( eval(robot_angles[0]['j1']) + eval(robot_angles[1]['j2']) ))
 

j3      = Point( 
		j2.x + link_lengths[2]['l3'] * np.cos( eval(robot_angles[0]['j1']) + eval(robot_angles[1]['j2']) + eval(robot_angles[2]['j3']) ), 
		j2.y + link_lengths[2]['l3'] * np.sin( eval(robot_angles[0]['j1']) + eval(robot_angles[1]['j2']) + eval(robot_angles[2]['j3']) ) )

joints  = np.array([j1,j2,j3])

# Obstacle
obstacle = plt.Circle( ( config['obstacle'][0]['x'] , config['obstacle'][1]['y'] ) , config['obstacle'][2]['r'],color='b' )
 
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.add_patch(obstacle)
x_axis = np.array([base.x,j1.x,j2.x,j3.x])
y_axis = np.array([base.y,j1.y,j2.y,j3.y])
plt.plot(x_axis,y_axis)
plt.show()








