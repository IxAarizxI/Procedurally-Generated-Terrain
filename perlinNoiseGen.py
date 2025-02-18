from perlin_noise import PerlinNoise
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

noise = PerlinNoise(octaves=5, seed=42) 
width, height = 500, 500

grid = np.array([[noise([i / (width * 0.6), j / (height * 0.6)]) for j in range(width)] for i in range(height)])

grid = (grid - np.min(grid)) / (np.max(grid) - np.min(grid))

grid = grid**1.5

grid = gaussian_filter(grid, sigma=1.5)

terrain_colors = [
    (0.00, "#004488"), 
    (0.20, "#1f78b4"), 
    (0.35, "#33a02c"), 
    (0.50, "#b2df8a"), 
    (0.65, "#fdbf6f"),  
    (0.80, "#8E6E57"),  
    (0.90, "#a9a9a9"), 
    (1.00, "#ffffff"), 
]

terrain_cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("terrain_cmap", terrain_colors)

plt.imshow(grid, cmap=terrain_cmap)
plt.colorbar()
plt.show()
