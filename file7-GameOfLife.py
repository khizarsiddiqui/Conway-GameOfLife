# starting the build of simualtion for game of life
# understanding the Conceptual visualization of toroidal boundary conditions
# Conway’s Game of Life has four rules.
# 1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF.
# 2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
# 3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
# 4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.

# first, displaying a grid of values

import sys, argparse
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
ON = 255
OFF = 0
vals = [ON, OFF]
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

# applying conway's rules (step 5)

# any cell that is ON is turned OFF if it has fewer than two neighbors that are ON or if it has more than three neighbors that are ON.
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF

# applies only to OFF cells: a cell is turned ON if exactly three neighbors are ON.
            else:
                if total == 3:
                    newGrid[i, j] = ON

# update data
            img.set_data(newGrid)
            grid[:] = newGrid[:]
            return img,
    
# Sending Command Line Arguments to the Program (step 6)
# main() function

def main():
# command line arguments are in sys.argv[1], sys.argv[2], ...
# sys.argv[0] is the script name and can be ignored
# parse arguments
      parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
# add arguments
      parser.add_argument('--grid-size', dest='N', required=False)
      parser.add_argument('--mov-file', dest='movfile', required=False)
      parser.add_argument('--interval', dest='interval', required=False)
      parser.add_argument('--glider', action='store_true', required=False)
      parser.add_argument('--gosper', action='store_true', required=False)
      args = parser.parse_args()