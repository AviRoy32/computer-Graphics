
import matplotlib.pyplot as plt

def translate_point(x, y, tx, ty):
    return x + tx, y + ty

def get_points():
    points = []
    n = int(input("Enter the number of points: "))
    for i in range(n):
        x = float(input(f"Point {i+1} - x: "))
        y = float(input(f"Point {i+1} - y: "))
        points.append((x, y))
    return points

original_points = get_points()
tx = float(input("Enter translation in x-direction (tx): "))
ty = float(input("Enter translation in y-direction (ty): "))
translated_points = [translate_point(x, y, tx, ty) for x, y in original_points]

x_orig, y_orig = zip(*(original_points + [original_points[0]]))
x_trans, y_trans = zip(*(translated_points + [translated_points[0]]))

plt.plot(x_orig, y_orig, label="Original", color='blue')
plt.plot(x_trans, y_trans, label="Translated", color='red')
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("2D Translation")
plt.show()