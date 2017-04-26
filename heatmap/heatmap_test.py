import numpy as np
import seaborn as sns
import scipy.ndimage as ndimage
#make sure matplotlib is installed

heatmap_data = np.zeros((10,10))

heatmap_data = ([[0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,10,0],
                 [0,0,0,0,0,0,0,10,10,0],
                 [0,0,0,0,0,0,0,10,10,0],
                 [0,0,0,10,0,0,0,10,10,0],
                 [0,0,10,10,10,0,0,10,10,0],
                 [10,10,10,10,10,10,10,10,10,0],
                 [0,10,10,10,10,10,10,10,10,0],
                 [0,10,10,10,10,10,10,10,10,10]])

heatmap_data = ndimage.gaussian_filter(heatmap_data, sigma=1, order=0)

ax = sns.heatmap(heatmap_data, cmap="coolwarm")

sns.plt.show()
