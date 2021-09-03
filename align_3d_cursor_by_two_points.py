import bpy
import random
from math import *

# Align 3D Cursor by Two Points
# Blender 2.8, Blender 2.9

def align3DCursor (x1, y1, z1, x2, y2, z2):
	dx = x2 - x1
	dy = y2 - y1
	dz = z2 - z1	
	dist = sqrt(dx**2 + dy**2 + dz**2)

	bpy.context.scene.cursor.location = (x1, y1, z1)

	phi = atan2(dy, dx) 
	theta = acos(dz/dist) 

	bpy.context.scene.cursor.rotation_euler[1] = theta
	bpy.context.scene.cursor.rotation_euler[2] = phi

point1 = [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)]
point2 = [random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)]

align3DCursor (point1[0], point1[1], point1[2], point2[0], point2[1], point2[2])