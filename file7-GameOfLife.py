# starting the build of simualtion for game of life
# understanding the Conceptual visualization of toroidal boundary conditions

# first, displaying a grid of values

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest') # imshow() method in matplotlib, represents a matrix of numbers as an image
plt.show() # plt.show() method displays this matrix of values as an image