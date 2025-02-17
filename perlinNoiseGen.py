from perlin_noise import PerlinNoise
import numpy as np
import matplotlib.pyplot as plt

noise = PerlinNoise(octaves=7, seed=42124)
width, height = 500, 500

grid = np.array([[noise([i / width, j / height]) for j in range(width)] for i in range(height)])

plt.imshow(grid, cmap='gray')
plt.colorbar()
plt.show()
