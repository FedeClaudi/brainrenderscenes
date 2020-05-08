"""
    This example shows how to add a 3d object to the scene by loading
    it from file and moving/scaling it to be aligned correctly.

    Note that the mouse skull and brain meshes come from different sources
    so that's why they don't match perfectly.
"""


import brainrender
brainrender.SHADER_STYLE = 'cartoon'
brainrender.ROOT_ALPHA = 1

from brainrender.scene import Scene

scene = Scene()

# Load skull from file
skull = scene.add_from_file('meshes/skull.stl')
skull.c('ivory').alpha(1)

# Align skull and brain (scene.root)
skull_com = skull.centerOfMass()
root_com = scene.root.centerOfMass()

skull.origin(skull.centerOfMass())
skull.rotateY(90).rotateX(180)
skull.x(root_com[0] - skull_com[0])
skull.y(root_com[1] - skull_com[1])
skull.z(root_com[2] - skull_com[2])
skull.x(3500)
skull.rotateZ(-25)
skull.y(7800)
skull.scale([1300, 1500, 1200]) 



# Cut skull actor to show brain inside
scene.cut_actors_with_plane('sagittal', actors=skull)

# Improve looks
s1 = scene.root.silhouette().lw(3).c('k')
s2 = skull.silhouette().lw(3).c('k')
scene.add_vtkactor(s1, s2)

scene.render()