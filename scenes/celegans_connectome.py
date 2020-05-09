import brainrender
brainrender.SHADER_STYLE = 'cartoon'


from brainrender.scene import Scene
from brainrender.atlases.celegans import Celegans

# Specify path to folder with c.elegans connectome
data_folder = '/Users/federicoclaudi/Dropbox (UCL - SWC)/Rotation_vte/Anatomy/Atlases/atlasesforbrainrender/CELEGANS'

# Create brainrender scene
scene = Scene(add_root=False, atlas=Celegans, display_inset=False, 
        use_default_key_bindings=True,
        atlas_kwargs=dict(data_folder=data_folder))


# Exclude some neurons
metadata = scene.atlas.neurons_metadata
neurons = metadata.loc[(metadata.type != 'nonvalid')&(metadata.type != 'other')]


# Add each neuron with the corresponding outline
scene.add_neurons(list(neurons.neuron.values))
for neuron in scene.actors['neurons']:
    scene.add_vtkactor(neuron.silhouette().lw(3).c('k'))

# Render
scene.render()
