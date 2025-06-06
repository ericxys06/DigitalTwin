import bpy
import csv
from math import sin, cos, pi

# === CLEAR SCENE ===
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# === PARAMETERS ===
radius = 1.0
layer_height = 0.05
segments_per_layer = 100
num_layers = int((2 * radius) / layer_height) + 1

# === CREATE PRINT HEAD ===
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.03, location=(0, 0, -radius))
head = bpy.context.object
head.name = "PrintHead"
head.animation_data_clear()

positions = []
frame = 1

# === GENERATE PATH POINTS LAYER BY LAYER ===
for i in range(num_layers):
    z = -radius + i * layer_height
    r = (radius**2 - z**2)**0.5 if abs(z) <= radius else 0
    if r == 0:
        continue
    for j in range(segments_per_layer):
        theta = (2 * pi) * j / segments_per_layer
        x = r * cos(theta)
        y = r * sin(theta)
        head.location = (x, y, z)
        head.keyframe_insert(data_path="location", frame=frame)
        positions.append((frame, x, y, z))
        frame += 1

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = frame

# === EXPORT TO CSV ===
csv_path = bpy.path.abspath("//print_path_contours.csv")
with open(csv_path, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Frame", "X", "Y", "Z"])
    writer.writerows(positions)

# === EXPORT TO GCODE ===
gcode_path = bpy.path.abspath("//print_path_contours.gcode")
with open(gcode_path, mode='w', newline='') as g:
    g.write("; G-code generated from Blender Python script\n")
    g.write("G21 ; Set units to millimeters\n")
    g.write("G90 ; Use absolute positioning\n")
    g.write("G28 ; Home all axes\n")
    for (_, x, y, z) in positions:
        g.write(f"G1 X{x:.3f} Y{y:.3f} Z{z:.3f} F1500\n")
    g.write("M2 ; End of program\n")

print(f"✅ Exported G-code to: {gcode_path}")
