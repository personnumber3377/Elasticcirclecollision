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


	def update_velocity(self,othercircle: Circle): # Update the velocity of this ball with the other ball.



