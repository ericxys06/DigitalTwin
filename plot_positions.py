import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs, ys, zs = [], [], []

with open('/Users/esun/Documents/positions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        xs.append(float(row['x']))
        ys.append(float(row['y']))
        zs.append(float(row['z']))

#git commit test
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, marker='o', markersize=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Path from CSV')
plt.show()