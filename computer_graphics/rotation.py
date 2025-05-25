#Rotation
import matplotlib.pyplot as plt
import math

def rotate_point(x, y, angle_deg):
    angle_rad = math.radians(angle_deg)
    return (
        x * math.cos(angle_rad) - y * math.sin(angle_rad),
        x * math.sin(angle_rad) + y * math.cos(angle_rad)
    )

def rotate_shape(points, angle_deg, clockwise=False):
    if clockwise:
        angle_deg = -angle_deg
    return [rotate_point(x, y, angle_deg) for x, y in points]

def get_points():
    points = []
    n = int(input("Enter the number of points: "))
    for i in range(n):
        x = float(input(f"Point {i+1} - x: "))
        y = float(input(f"Point {i+1} - y: "))
        points.append((x, y))
    return points

original_points = get_points()
angle = float(input("Enter rotation angle (degrees): "))
direction = input("Enter direction (clockwise/anticlockwise): ").strip().lower()
clockwise = True if direction == "clockwise" else False

rotated_points = rotate_shape(original_points, angle, clockwise)

x_orig, y_orig = zip(*(original_points + [original_points[0]]))
x_rot, y_rot = zip(*(rotated_points + [rotated_points[0]]))

plt.plot(x_orig, y_orig, label="Original", color='blue')
plt.plot(x_rot, y_rot, label=f"Rotated {angle}° {'Clockwise' if clockwise else 'Anticlockwise'}", color='orange')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("2D Rotation")
plt.show()