import os
from tqdm import tqdm
import numpy as np
from random import choices

from vtkplotter import Mesh, write, Sphere, settings
settings.screeshotScale = 2

import brainrender
brainrender.BACKGROUND_COLOR = [.2, .2, .2]
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = True

from brainrender.scene import Scene
from brainrender.Utils.data_io import listdir
from brainrender.colors import makePalette


# ---------------------------------- params ---------------------------------- #

meshes_fld = 'J:\\layer23_v185\\meshes'
N = 8  # once you start going > 25 neurons it might take a few to several minutes to render

random_neurons = True
random_alpha = False

add_silhouette = True
cartoon = True
brainrender.SHADER_STYLE = 'cartoon'


# ------------------------------- render scene ------------------------------- #

# Get files and create a brainrender scene
files = listdir(meshes_fld)
scene = Scene(add_root=False, display_inset=False)
# scene.plotter.axes = 1



print('rendering neurons')
meshes = scene.add_from_file(*choices(files, k=N))


cols = ['salmon', 'lightgreen']
colors = makePalette(N, *cols)

for mesh, col in zip(meshes, colors):
    mesh.c(col)

    if add_silhouette:
        outline = mesh.silhouette().lw(0.5).c('k')
        scene.add_vtkactor(outline)





# Define the camera perspective
bespoke_camera = dict(
    position = [173494.166, 143864.531, 443358.233] ,
    focal = [366875.0, 230795.0, 43543.5],
    viewup = [0.098, -0.981, -0.166],
    distance = 452553.725,
    clipping = [250165.374, 708410.547],
)



scene.render(camera=bespoke_camera, zoom=1.5)


scene.close()
# scene.export_for_web('test.html')
