"""
    This tutorial shows you how to render efferent mesoscale connectivity
    data from the Allen mouse connectome project as streamlines. 

"""
import brainrender
from brainrender.scene import Scene
brainrender.SHADER_STYLE = "cartoon"

brainrender.ROOT_ALPHA = 1
brainrender.ROOT_COLOR = [255, 201, 160]

# Start by creating a scene with the allen brain atlas atlas
scene = Scene(display_inset=False, add_root=False)
# scene.add_mesh_silhouette(scene.root, lw=2)

left = 'meshes/humanbrain2_lefthemisphere.obj'
right = 'meshes/humanbrain2_righthemisphere.obj'
sub = 'meshes/humanbrain2_subctx.obj'


colors = [[255, 201, 160], [255, 178, 131]]
for file, color in zip([right, sub], colors):
    act = scene.add_from_file(file, c=color)
    scene.add_mesh_silhouette(act, featureAngle=40, lw=3)


cam = dict(
    position = [-0.056, -471.127, -42.595] ,
    focal = [-0.382, -3.655, 5.239],
    viewup = [-0.01, -0.102, 0.995],
    distance = 469.913,
    clipping = [290.137, 701.5] ,
)



scene.render(camera=cam)
