# """
#     This tutorial shows how to download and render neurons from the MouseLight project
#     using the MouseLightAPI class. 

#     You can also download data manually from the neuronbrowser website and render them by
#     passing the downloaded files to `scene.add_neurons`.
# """
# import brainrender
# brainrender.SHADER_STYLE = 'cartoon'


# from brainrender.scene import Scene
# from brainrender.colors import makePalette

# from brainrender.Utils.MouseLightAPI.mouselight_api import MouseLightAPI
# from brainrender.Utils.MouseLightAPI.mouselight_info import mouselight_api_info, mouselight_fetch_neurons_metadata
# from brainrender.Utils.AllenMorphologyAPI.AllenMorphology import AllenMorphology

# from allensdk.core import swc

fp = '/Users/federicoclaudi/Documents/Github/brainrenderscenes/morphologies/bailey/CNG version/Layer-2-3-Ethanol-4.CNG.swc'

import neurom as nm


nrn = nm.load_neuron(fp)


# Initialize nrn as above
from neurom import viewer
fig, ax = viewer.draw(nrn)
fig.show()
fig, ax = viewer.draw(nrn, mode='3d') # valid modes '2d', '3d', 'dendrogram'
fig.show()


# swcfile = '/Users/federicoclaudi/Documents/Github/brainrenderscenes/morphologies/bailey/CNG version'


# am = AllenMorphology()


# # Render 
# am.add_neuron(swcfile, color='salmon')
# am.render(zoom=1)


# # # Show neurons and ZI in the same scene:
# # scene = Scene()
# # scene.add_neurons(swcfile, neurite_radius=14)


# # # colors = makePalette('salmon', 'orangered', len(neurons_files)+1)

# # # for neuron, color in zip(scene.actors['neurons'], colors):
# # #     for mesh in neuron.values():
# # #         mesh.c(color)


# # scene.render() 