import brainrender
from brainrender.scene import Scene
from brainrender.colors import makePalette

# Change some of the default settings
brainrender.BACKGROUND_COLOR = 'blackboard'
brainrender.ROOT_COLOR = 'white'
brainrender.ROOT_ALPHA = .2

# Start by creating a scene with the allen brain atlas atlas
scene = Scene()


# Download streamlines data for injections in the CA1 field of the hippocampus
filepaths, data = scene.atlas.download_streamlines_for_region("MOs")
data = data[:2]

# you can pass either the filepaths or the data
colors = makePalette(len(data), "salmon", "lightgreen")
actors = scene.add_streamlines(data, color=colors, show_injection_site=False)

# Now mody the color of each actor
# Color each actor's vertices based on the X position
color_combos = [['darkblue', 'powderblue'], ['deeppink', 'lightpink']]
for actor, colors in zip(actors, color_combos):
    scals = actor.points()[:, 0]   # pick x coordinates of vertices
    cmap = makePalette(len(scals), colors[0], colors[1]) # make colors
    actor.pointColors(scals, cmap=cmap)

scene.render(camera="sagittal", zoom=1)
