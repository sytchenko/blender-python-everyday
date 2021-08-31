import bpy
import random

# Create Curve by Points Array
# Blender 2.8, Blender 2.9

def curveBezierFromPoints (coords, name, curveType, curveResolution, curveClosed):
#	curveType: 'POLY' | 'BEZIER' | 'NURBS'
	curveData = bpy.data.curves.new (name, type='CURVE')
	curveData.dimensions = '3D'
	curveData.resolution_u = curveResolution

	curve = curveData.splines.new ('BEZIER')
	curve.bezier_points.add (len(coords)-1)

	for i, coord in enumerate(coords):
		x, y, z = coord
		curve.bezier_points[i].co = (x, y, z)
		curve.bezier_points[i].handle_left = (x, y, z)
		curve.bezier_points[i].handle_right = (x, y, z)

	if curveClosed:
		curve.use_cyclic_u = True

	obj = bpy.data.objects.new (name, curveData)

	scn = bpy.context.scene
	bpy.context.collection.objects.link (obj)
	bpy.context.view_layer.objects.active = obj
	bpy.context.active_object.select_set (state=True)

	bpy.ops.object.mode_set (mode="EDIT")
	bpy.ops.curve.spline_type_set (type=curveType)
	bpy.ops.curve.select_all (action='SELECT')
	bpy.ops.curve.handle_type_set (type='AUTOMATIC')
	bpy.ops.object.mode_set (mode="OBJECT")

coords = []
count = 0
while count<=6:
	coords.append ([random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)])
	count += 1

curveBezierFromPoints (coords,'My Curve', 'BEZIER', 5, True)
