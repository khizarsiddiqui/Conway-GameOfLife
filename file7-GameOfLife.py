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

# now we can think about how to implement the toroidal boundary conditions (step 4)

def update(frameNum, img, grid, N):
# copy grid since we require 8 neighbors for calculation
# and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
# compute 8-neighbor sum using toroidal boundary conditions
# x and y wrap around so that the simulation
# takes place on a toroidal surface
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                        grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

# to be continued
    



