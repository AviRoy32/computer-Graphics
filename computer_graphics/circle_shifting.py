import matplotlib.pyplot as plt

def draw_circle_midpoint(radius):
    x = 0
    y = radius
    p = 1 - radius

    x_points = []
    y_points = []

    while x <= y:
        # 8 symmetry points
        points = [
            (x, y), (y, x), (-x, y), (-y, x),
            (-x, -y), (-y, -x), (x, -y), (y, -x)
        ]
        for point in points:
            x_points.append(point[0])
            y_points.append(point[1])

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    # Plot the circle
    plt.figure(figsize=(6,6))
    plt.scatter(x_points, y_points, color='blue')
    plt.gca().set_aspect('equal')
    plt.title("Midpoint Circle Drawing Algorithm")
    plt.grid(True)
    plt.show()

# Example usage
draw_circle_midpoint(radius=100)