import os
from tqdm import tqdm
import numpy as np

from meshparty import trimesh_io
from vtkplotter import Mesh, write


"""
    Takes mesh data from the microns dataset and saves it as .obj files
    This id done by loading the data with mesh part, converting to 
    vtkplotter actors and saving with vtkplotter write.
    It might take a while... 

"""

# Specify the path to where you unzipped your data and where you want to save the .obj files
data_fld = '' 
output_fld = os.path.join(data_fld, 'meshes')
if not os.path.isfile(output_fld):
    os.mkdir(output_fld)


# start creating .obj files, see you in a couple hours
for f in tqdm(os.listdir(data_fld)):
    try:
        # load with trimesh
        meshmeta = trimesh_io.MeshMeta()
        mesh = meshmeta.mesh(os.path.join(data_fld, f)) # mesh gets cached

        # Convert to vtkplotter and save to obj
        vtkmesh = Mesh([np.array(mesh.vertices), np.array(mesh.faces)])
        write(vtkmesh, os.path.join(output_fld, f.split('.')[0]+'.obj'))
    except:
        print(f'Failed to open and convert {f}') # not all .h5 files seem to have data