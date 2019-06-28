import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess

file_name = ""

rows = int(subprocess.check_output(["wc","-l",file_name]).decode("utf-8").split()[0])
cols = 2

points = np.memmap('memmapped.dat', dtype=np.float32,
              mode='w+', shape=(rows, cols))

values = None
row = 0

with open(file_name,"r") as f:
    while True:
        temp = f.readline()
        if(temp == ""):
            print "End of File reached!"
            break
        else:
            temp = temp.split()
            try:
                points[row][0] = temp[0]  # x value
                points[row][1] = temp[1]  # y value
            except:
                pass
        row += 1

# print points[:,0]     #
# print points[:,1]     #

plt.plot(points[:,0],points[:, 1])
plt.show()
