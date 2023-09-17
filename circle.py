#!/bin/python3

import numpy as np
import math

'''

Big thanks to https://stackoverflow.com/questions/6247153/angle-from-2d-unit-vector !

constexpr int radToDeg(float rad) { return rad*(180/M_PI); }

int vectorAngle(int x, int y) {
    if (x == 0) // special cases
        return (y > 0)? 90
            : (y == 0)? 0
            : 270;
    else if (y == 0) // special cases
        return (x >= 0)? 0
            : 180;
    int ret = radToDeg(atanf((float)y/x));
    if (x < 0 && y < 0) // quadrant Ⅲ
        ret = 180 + ret;
    else if (x < 0) // quadrant Ⅱ
        ret = 180 + ret; // it actually substracts
    else if (y < 0) // quadrant Ⅳ
        ret = 270 + (90 + ret); // it actually substracts
    return ret;
}

'''



class Circle:
	def __init__(self, radius: float, position: np.array, velocity: np.array, mass: float):

		self.radius = radius
		self.position = position
		self.velocity = velocity
		self.checked = False

	def get_mag_vel(self):

		return math.sqrt(sum([x**2 for x in self.velocity]))

	def get_mov_angle(self):

		# Gets the current movement angle in degrees.

		# Big thanks to https://stackoverflow.com/questions/6247153/angle-from-2d-unit-vector !

		x_vel = self.velocity[0]
		y_vel = self.velocity[1]
		if x_vel == 0.0:
			if y > 0:
				return math.pi/2
			elif y == 0:
				return 0.0
			else:
				return (3*math.pi)/2
		ret = math.atan(float(y/x))
		
		if (x < 0 and y < 0) or x < 0:
			ret = math.pi + ret
		elif y < 0:
			ret = (3*math.pi/2)+(math.pi/2+ret)
		return ret

	def get_angle_vec(self, vector: np.array):

		x_vel = vector[0]
		y_vel = vector[1]

		if x_vel == 0.0:
			if y > 0:
				return math.pi/2
			elif y == 0:
				return 0.0
			else:
				return (3*math.pi)/2

		ret = math.atan(float(y/x))
		
		if (x < 0 and y < 0) or x < 0:
			ret = math.pi + ret
		elif y < 0:
			ret = (3*math.pi/2)+(math.pi/2+ret)

		return ret


	def update_velocity(self,othercircle: Circle): # Update the velocity of this ball with the other ball.
		
		if self.checked:
			return

		x_vel = self.velocity[0]
		y_vel = self.velocity[1]

		# Now we use the equations as described in the wikipedia article.
		v_1 = self.get_mag_vel()
		v_2 = othercircle.get_mag_vel()

		theta_1 = self.get_mov_angle()
		theta_2 = othercircle.get_mov_angle()

		vector_to_other = -1*self.position+othercircle.position # The vector from A to B is  (-1 * A) + B
		phi = self.get_angle_vec(vector_to_other)
		m_1 = self.mass
		m_2 = othercircle.mass

		new_x_vel = (((vel_mag)*math.cos(theta_1 - phi)*(m_1 - m_2) + (2*m_2*v_2*math.cos(theta_2 - phi)))/(m_1+m_2))*math.cos(phi) + v_1*math.sin(theta_1 - phi)*math.cos(phi+math.pi/2)
		new_y_vel = (((vel_mag)*math.cos(theta_1 - phi)*(m_1 - m_2) + (2*m_2*v_2*math.cos(theta_2 - phi)))/(m_1+m_2))*math.sin(phi) + v_1*math.sin(theta_1 - phi)*math.sin(phi+math.pi/2)

		return