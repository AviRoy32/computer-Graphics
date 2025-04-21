import matplotlib.pyplot as plt

def drawline(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    points_x = []
    points_y = []

    p = 2 * dy - dx

    while x <= x1:
        points_x.append(x)
        points_y.append(y)
        if p >= 0:
            y += 1
            p += 2 * dy - 2 * dx
        else:
            p += 2 * dy
        x += 1

    # Plotting the line
    plt.figure(figsize=(6, 4))
    plt.plot(points_x, points_y, color='black')
    plt.title('Bresenham Line Drawing Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    #plt.gca().invert_yaxis()  # To mimic traditional graphics coordinates
    plt.show()

# Get input from user
x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

# Ensure x0 < x1 for simplicity
if x0 > x1:
    x0, x1 = x1, x0
    y0, y1 = y1, y0

drawline(x0, y0, x1, y1)