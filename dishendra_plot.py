import numpy as np
import matplotlib.pyplot as plt

rows, cols = 1031340, 2

points = np.memmap('memmapped.dat', dtype=np.float32,
              mode='w+', shape=(rows, cols))

values = None
with open("dishendra.txt","r") as f:
    for row in range(rows):
        try:
            temp = f.readline().split()
            points[row][0] = temp[0]  # x value
            points[row][1] = temp[1]  # y value
        except:
            pass

# print points[:,0]     # x values
# print points[:,1]     # y values

plt.plot(points[:,0],points[:, 1])
plt.show()
