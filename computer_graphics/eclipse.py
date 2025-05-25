import matplotlib.pyplot as plt

def draw_ellipse_midpoint(rx, ry, xc, yc):
    x = 0
    y = ry

    rx_sq = rx * rx
    ry_sq = ry * ry
    dx = 2 * ry_sq * x
    dy = 2 * rx_sq * y

    x_points = []
    y_points = []

    # Region 1
    p1 = ry_sq - (rx_sq * ry) + (0.25 * rx_sq)
    while dx < dy:
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc - x, yc - y), (xc + x, yc - y)
        ]
        for px, py in points:
            x_points.append(px)
            y_points.append(py)

        x += 1
        dx = 2 * ry_sq * x
        if p1 < 0:
            p1 += ry_sq * (2 * x + 1)
        else:
            y -= 1
            dy = 2 * rx_sq * y
            p1 += ry_sq * (2 * x + 1) - dy

    # Region 2
    p2 = (ry_sq * (x + 0.5)**2) + (rx_sq * (y - 1)**2) - (rx_sq * ry_sq)
    while y >= 0:
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc - x, yc - y), (xc + x, yc - y)
        ]
        for px, py in points:
            x_points.append(px)
            y_points.append(py)

        y -= 1
        dy = 2 * rx_sq * y
        if p2 > 0:
            p2 -= rx_sq * (2 * y + 1)
        else:
            x += 1
            dx = 2 * ry_sq * x
            p2 += dx - rx_sq * (2 * y + 1)

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.scatter(x_points, y_points, color='purple', s=5)
    plt.plot(xc, yc, 'bo', label='Center')
    plt.title("Midpoint Ellipse Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# ----- User Input -----
rx = int(input("Enter radius along X-axis (rx): "))
ry = int(input("Enter radius along Y-axis (ry): "))
xc = int(input("Enter center X-coordinate: "))
yc = int(input("Enter center Y-coordinate: "))

draw_ellipse_midpoint(rx, ry, xc, yc)
