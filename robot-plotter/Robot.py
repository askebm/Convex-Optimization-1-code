import yaml 
import numpy as np
import Point as pt
from collections import ChainMap
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

class Robot(yaml.YAMLObject):
	"""docstring for Robot"""

	def getDickFromYAMLFuck(self,list_of_dic):
		""" Convert a list of dictionaries from YAML, to a dictionary with evaluated values """
		d = dict(ChainMap( *(list_of_dic) ))
		for k,v in d.items():
			if isinstance(v,str):
				d[k] = eval(v)
		return d
	
	def plotMeDaddy(self):
		"""Plot the robot"""
		x_axis = []
		y_axis = []
		ax = plt.subplot(aspect='equal')
		x_axis.append(self.base[0])
		y_axis.append(self.base[1])
		for i in range(self.num_of_joints):
			x_axis.append(self.joint_points[i].x)
			y_axis.append(self.joint_points[i].y)
			ax.add_artist(self.bodies[i])
		plt.plot(x_axis,y_axis)
		plt.show()

	def summary(self):
		print("joint_points : \n", self.joint_points)
		print("joints : \n", self.joints)
		print("base : \n", self.base)
		print("link lengths : \n", self.links_lengths)
		print("number of joints : \n", self.num_of_joints)
	
	def setAngles(self,q):
		for i in range(self.num_of_joints):
			self.joints[i] = q[i]

	def __init__(self, conf):
		super(Robot, self).__init__()
		
		# YAML config file extraction
		self.conf = conf
		with open(conf) as f:
			self.conf = yaml.load(f, Loader=yaml.FullLoader)
		
		# Place YAML variables in attributes.

		# Attributes
		self.base = pt.Point(0,0) 
		self.num_of_joints = 0 
		self.joints = []
		self.links_lengths = []
		self.bodies = []
		self.joint_points = []
		self.gripper = None
		
		self.joints = list(self.getDickFromYAMLFuck(self.conf['joint_angles']).values())
		self.links_lengths = list(self.getDickFromYAMLFuck( self.conf['link_lengths']).values())
		self.base = list(self.getDickFromYAMLFuck(self.conf['base']).values())
		self.num_of_joints = len(self.links_lengths)
		
		x      = 0
		y      = 0
		x_prev = 0
		y_prev = 0
		q_prev = 0

		# Generate the joint positions
		for i in range(self.num_of_joints):
			x = x_prev + (self.links_lengths[i]) * np.cos( q_prev + self.joints[i] )
			y = y_prev + (self.links_lengths[i]) * np.sin( q_prev + self.joints[i] )
			self.joint_points.append( pt.Point(x, y) )
			self.bodies.append(Ellipse( 
					xy=( (x + x_prev)/2.0, (y + y_prev)/2.0) , 
					width=list( self.getDickFromYAMLFuck(self.conf['bodies']).values())[0], 
					height=np.sqrt((x-x_prev)**2 + (y-y_prev)**2), 
					edgecolor='b', 
					lw=2,
					angle=(q_prev + self.joints[i]) * 180.0/np.pi - 90))

			x_prev = x
			y_prev = y
			q_prev = q_prev + self.joints[i]
			
		
robot = Robot("plt_conf.yaml")
robot.summary()
robot.plotMeDaddy()

