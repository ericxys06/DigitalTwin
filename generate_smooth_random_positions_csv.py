import csv
import random

num_frames = 101        # Number of frames
min_pos = 0.0           # Minimum allowed value (cm)
max_pos = 100.0         # Maximum allowed value (cm)
max_step = 3.0          # Maximum change per frame (cm), adjust for smoother/faster motion

positions = []
# Start at a random point within the range
x, y, z = (
    round(random.uniform(min_pos, max_pos), 2),
    round(random.uniform(min_pos, max_pos), 2),
    round(random.uniform(min_pos, max_pos), 2)
)
positions.append((x, y, z))

for _ in range(1, num_frames):
    # Each new position is previous + small random step, clamped to [min_pos, max_pos]
    x = round(min(max(x + random.uniform(-max_step, max_step), min_pos), max_pos), 2)
    y = round(min(max(y + random.uniform(-max_step, max_step), min_pos), max_pos), 2)
    z = round(min(max(z + random.uniform(-max_step, max_step), min_pos), max_pos), 2)
    positions.append((x, y, z))

with open('positions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'z'])
    writer.writerows(positions)

print("Smooth random positions.csv generated!")