import numpy as np
import matplotlib.pyplot as plt

grid = np.load('new_york.npy')
plt.imshow(grid)
plt.tight_layout()
plt.show()
