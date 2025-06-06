import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# === Load the CSV ===
csv_file = "print_path_contours.csv"  # Use the full path if needed

frames, xs, ys, zs = [], [], [], []

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        frames.append(int(row["Frame"]))
        xs.append(float(row["X"]))
        ys.append(float(row["Y"]))
        zs.append(float(row["Z"]))

# === Plotting ===
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, label='Print Path', linewidth=1.5)

ax.scatter(xs[0], ys[0], zs[0], color='green', label='Start')
ax.scatter(xs[-1], ys[-1], zs[-1], color='red', label='End')

ax.set_title("3D Print Head Path for Soccer Ball")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.view_init(elev=30, azim=45)
plt.tight_layout()
plt.show()
