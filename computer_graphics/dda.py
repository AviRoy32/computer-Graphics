import matplotlib.pyplot as plt

def draw_line_digital_diff_analyzer(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = int(max(abs(dx), abs(dy)))

    dx = dx / steps
    dy = dy / steps

    x = x0
    y = y0

    x_coords = []
    y_coords = []

    for _ in range(steps):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += dx
        y += dy

    # Plot the pixels
    plt.figure(figsize=(6, 4))
    plt.plot(x_coords, y_coords)
    plt.title("Line Drawing using DDA Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

# Taking user input
x0 = int(input("Enter starting x coordinate: "))
y0 = int(input("Enter starting y coordinate: "))
x1 = int(input("Enter ending x coordinate: "))
y1 = int(input("Enter ending y coordinate: "))

draw_line_digital_diff_analyzer(x0, y0, x1, y1)