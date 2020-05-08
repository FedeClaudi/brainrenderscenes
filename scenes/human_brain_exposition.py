import brainrender
# brainrender.SHOW_AXES = True
brainrender.SHADER_STYLE = 'cartoon'
import numpy as np
from brainrender.scene import Scene
from brainrender.colors import makePalette

from vtkplotter import write, merge

# fp = '/Users/federicoclaudi/Desktop/meshes/cleanobjs/human_brain/lh.pial.obj'
# fp = '/Users/federicoclaudi/Desktop/meshes/cleanobjs/human_brain.obj'

# TODO improve positioning and scaling !! 

fp = '/Users/federicoclaudi/Desktop/meshes/cleanobjs/human_brain.obj'


cam = dict(
    position = [-0.056, -471.127, -42.595] ,
    focal = [-0.382, -3.655, 5.239],
    viewup = [-0.01, -0.102, 0.995],
    distance = 469.913,
    clipping = [290.137, 701.5] ,
)


for n, (rot, alpha, lw) in enumerate(zip([0, 30, 60, 90], [1, .6, .3, .1], [6, 4, 2, 1])):

    scene = Scene(add_root=False, display_inset=False, use_default_key_bindings=True)

    act = scene.add_from_file(fp).color('lightgray').alpha(1).rotateX(45)
    act.smoothWSinc(niter=15, passBand=0.1, edgeAngle=15, featureAngle=60)

    pos = act.centerOfMass()
    pos0 = pos.copy()
    pos[0] -= 58

    plane = scene.atlas.get_plane_at_point(pos, [1, 0, 0], 1, 1)
    cut0 = scene.cut_actors_with_plane(plane, returncut=True, close_actors=True)
    cut0.x(57).wireframe(False).alpha(1) # 57


    pos = pos0.copy()
    pos[0] += 58
    plane = scene.atlas.get_plane_at_point(pos, [-1, 0, 0], 1, 1)
    cut = scene.cut_actors_with_plane(plane, returncut=True, close_actors=True)
    cut.x(-67).wireframe(False).alpha(1) # 67
    scene.add_vtkactor(cut0, cut)




    act2 = merge(act, cut)
    act2.pos([0, 0, 0])
    act2.rotateX(45)

    act2.rotateZ(rot).alpha(alpha)

    scene.add_vtkactor(act2)

    act.alpha(0)
    cut.alpha(0)
    cut0.alpha(0)

    sil = act2.silhouette(featureAngle=40).lw(lw).c('k').alpha(alpha)
    scene.add_vtkactor(sil)

    # write(cut0, 'meshes/humanbrain2_righthemisphere.obj')
    # write(cut, 'meshes/humanbrain2_leftthemisphere.obj')
    # write(act, 'meshes/humanbrain2_subctx.obj')

    scene.render(interactive=False, zoom=1.25+.1*n, camera=cam)
    scene.take_screenshot()
    scene.close()



