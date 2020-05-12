## Description
Using `brainrender` to visualise detailed EM reconstruction of neurons from layer 2/3 or the visual cortex. 

For a more detailed description of the microns project visit: https://microns-explorer.org/phase1. 


## Usage
First head to https://microns-explorer.org/phase1, to download the dataset (it's about 10GB)


Then use `create_neurons_objs.py` to extract meshes for the reconstruction of individual neurons. This script will create a .obj file for each neuron to make it easier to render them at a later stage, but it will take a while to complete.

Finally you can use `visualize_neurons.py` to create a `brainrender` scene and populate it with the meshes for individual neurons. There's a few variables and parameter you can tweak to get different rendering styles.














-----------
**Citations**

* Dorkenwald, S., Turner, N.L., Macrina, T., Lee, K., Lu, R., Wu, J., Bodor, A.L., Bleckert, A.A., Brittain, D., Kemnitz, N., et al. (2019). Binary and analog variation of synapses between cortical pyramidal neurons. bioRxiv 2019.12.29.890319; doi: https://doi.org/10.1101/2019.12.29.890319

* Schneider-Mizell, C. Bodor, A.L., Collman, F.  Brittain,D. Bleckert, AA, Dorkenwald, S., Turner N.L. Macrina, T.  Lee, K. Lu, R.  Wu, J. et al. (2020)  Chandelier cell anatomy and function suggest a variably distributed but common signal. bioRxiv 2020.03.31.018952v1; doi: https://doi.org/10.1101/2020.03.31.018952


* Zhou, P. et al. EASE: EM-Assisted Source Extraction from calcium imaging data. bioRxiv 2020.03.25.007468; doi: https://doi.org/10.1101/2020.03.25.007468