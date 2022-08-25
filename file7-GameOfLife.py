# starting the build of simualtion for game of life
# understanding the Conceptual visualization of toroidal boundary conditions
# Conway’s Game of Life has four rules.
# 1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF.
# 2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
# 3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
# 4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.

# first, displaying a grid of values

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]]) # for building grid only (step 1)

# secondly, we can start building simulation by giving values and their probabilities

# x = np.random.choice([0, 255], 3*3, p=[0.4, 0.6]).reshape(3, 3) # for random generation using the values and their probabilities (step 2)
# plt.imshow(x, interpolation='nearest') # imshow() method in matplotlib, represents a matrix of numbers as an image
# plt.show() # plt.show() method displays this matrix of values as an image

# now creating glider (step 3) 

N = 50

def addGlider(i, j, grid):

# adds a glider with top left cell at (i, j)

    glider = np.array([[0, 0, 255], 
                   [255, 0, 255], 
                   [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
    plt.imshow(grid,interpolation='nearest')
    plt.show()
grid = np.zeros(N*N).reshape(N, N)
addGlider(1, 1, grid)



