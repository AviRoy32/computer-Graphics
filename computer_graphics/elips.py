import matplotlib.pyplot as plt

def draw_midpoint_ellipse(rx, ry):
    x = 0
    y = ry

    rx_sq = rx ** 2
    ry_sq = ry ** 2

    x_points = []
    y_points = []

    # Region 1
    p1 = ry_sq - (rx_sq * ry) + (0.25 * rx_sq)
    dx = 2 * ry_sq * x
    dy = 2 * rx_sq * y

    while dx < dy:
        for px, py in [(x, y), (-x, y), (-x, -y), (x, -y)]:
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
    p2 = (ry_sq * (x + 0.5) ** 2) + (rx_sq * (y - 1) ** 2) - (rx_sq * ry_sq)
    while y >= 0:
        for px, py in [(x, y), (-x, y), (-x, -y), (x, -y)]:
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

    # Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(x_points, y_points, color='blue', s=5)
    plt.title("Midpoint Ellipse Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.gca().set_aspect('equal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Example usage
draw_midpoint_ellipse(rx=400, ry=200)
