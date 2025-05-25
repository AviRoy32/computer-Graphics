import matplotlib.pyplot as plt

# Initialize global clipping window values
xmin, ymin, xmax, ymax = 0, 0, 0, 0

# Cohen-Sutherland Outcode
def compute_outcode(x, y):
    code = 0
    if x < xmin: code |= 1  # Left
    if x > xmax: code |= 2  # Right
    if y < ymin: code |= 4  # Bottom
    if y > ymax: code |= 8  # Top
    return code

# Cohen-Sutherland Line Clipping
def cohen_sutherland_clip(x1, y1, x2, y2):
    outcode1 = compute_outcode(x1, y1)
    outcode2 = compute_outcode(x2, y2)
    accept = False

    while True:
        if not (outcode1 | outcode2):
            accept = True
            break
        elif outcode1 & outcode2:
            break
        else:
            x, y = 0, 0
            outcode_out = outcode1 if outcode1 else outcode2

            if outcode_out & 8:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode_out & 4:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode_out & 2:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode_out & 1:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2)

    return (x1, y1, x2, y2) if accept else None

# Inside check
def inside(p, edge):
    x, y = p
    x1, y1, x2, y2 = edge
    if x1 == x2:
        return x >= x1 if x1 == xmin else x <= x1
    if y1 == y2:
        return y >= y1 if y1 == ymin else y <= y1
    return False

# Compute intersection point
def compute_intersection(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3, x4, y4 = edge
    if x3 == x4:
        x = x3
        y = y1 + (y2 - y1) * (x3 - x1) / (x2 - x1)
    else:
        y = y3
        x = x1 + (x2 - x1) * (y3 - y1) / (y2 - y1)
    return (x, y)

# Sutherland-Hodgman Polygon Clipping
def clip_polygon(polygon):
    edges = [
        (xmin, ymin, xmin, ymax),
        (xmax, ymin, xmax, ymax),
        (xmin, ymax, xmax, ymax),
        (xmin, ymin, xmax, ymin)
    ]

    for edge in edges:
        new_polygon = []
        for i in range(len(polygon)):
            current = polygon[i]
            prev = polygon[i - 1]
            if inside(current, edge):
                if not inside(prev, edge):
                    new_polygon.append(compute_intersection(prev, current, edge))
                new_polygon.append(current)
            elif inside(prev, edge):
                new_polygon.append(compute_intersection(prev, current, edge))
        polygon = new_polygon

    return polygon

# Draw clipped line
def draw_line_clipping(x1, y1, x2, y2):
    clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)
    plt.figure()
    plt.title("Line Clipping (Cohen-Sutherland)")
    plt.axvline(xmin, color='r')
    plt.axvline(xmax, color='r')
    plt.axhline(ymin, color='r')
    plt.axhline(ymax, color='r')
    plt.plot([x1, x2], [y1, y2], 'b--', label='Original Line')
    if clipped_line:
        cx1, cy1, cx2, cy2 = clipped_line
        plt.plot([cx1, cx2], [cy1, cy2], 'g-', linewidth=2, label='Clipped Line')
    else:
        print("Line is completely outside the clipping window.")
    plt.xlim(min(x1, x2, xmin) - 1, max(x1, x2, xmax) + 1)
    plt.ylim(min(y1, y2, ymin) - 1, max(y1, y2, ymax) + 1)
    plt.legend()
    plt.grid()
    plt.show()

# Draw clipped polygon
def draw_polygon_clipping(polygon):
    clipped = clip_polygon(polygon)
    if clipped:
        clipped.append(clipped[0])
        cx, cy = zip(*clipped)
        plt.plot(cx, cy, 'g-', label="Clipped Polygon")
        plt.fill(cx, cy, 'green', alpha=0.3)
    else:
        print("Polygon is completely outside the window.")

    polygon.append(polygon[0])
    px, py = zip(*polygon)
    plt.plot(px, py, 'b--', label="Original Polygon")

    plt.axvline(xmin, color='r')
    plt.axvline(xmax, color='r')
    plt.axhline(ymin, color='r')
    plt.axhline(ymax, color='r')
    plt.xlim(min(px + (xmin,)) - 1, max(px + (xmax,)) + 1)
    plt.ylim(min(py + (ymin,)) - 1, max(py + (ymax,)) + 1)
    plt.legend()
    plt.grid()
    plt.title("Polygon Clipping (Sutherland-Hodgman)")
    plt.show()

# Get user input for a line
def get_line_input():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    return x1, y1, x2, y2

# Get user input for polygon
def get_polygon_input():
    n = int(input("Enter number of vertices: "))
    polygon = []
    for i in range(n):
        x = float(input(f"Enter x{i+1}: "))
        y = float(input(f"Enter y{i+1}: "))
        polygon.append((x, y))
    return polygon

# Main function with menu
def main():
    global xmin, ymin, xmax, ymax
    print("---- Set Clipping Window ----")
    xmin = float(input("Enter xmin: "))
    ymin = float(input("Enter ymin: "))
    xmax = float(input("Enter xmax: "))
    ymax = float(input("Enter ymax: "))

    while True:
        print("\n--- MENU ---")
        print("1. Line Clipping (Cohen-Sutherland)")
        print("2. Polygon Clipping (Sutherland-Hodgman)")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\n-- Line Clipping --")
            x1, y1, x2, y2 = get_line_input()
            draw_line_clipping(x1, y1, x2, y2)
        elif choice == '2':
            print("\n-- Polygon Clipping --")
            polygon = get_polygon_input()
            draw_polygon_clipping(polygon)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()