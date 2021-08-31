import bpy
from mathutils import Vector

# Get Median Point From selected Vertices
# Blender 2.8, Blender 2.9

def medianPoint (obj):
	me = obj.data
	verts_sel = [v.co for v in me.vertices if v.select]
	if len(verts_sel)>0:
		pivot = sum(verts_sel, Vector()) / len(verts_sel)
		return pivot
	else:
		return "Vertices not selected"

obj = bpy.context.object
median = medianPoint (obj)
print (median)