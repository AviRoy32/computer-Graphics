import matplotlib.pyplot as plt

def point_clipping(x, y, xmin, ymin, xmax, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

def plot_point_and_window(x, y, xmin, ymin, xmax, ymax):
    fig, ax = plt.subplots()

    rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, edgecolor='blue', facecolor='none', linewidth=2)
    ax.add_patch(rect)

    if point_clipping(x, y, xmin, ymin, xmax, ymax):
        plt.plot(x, y, 'go', label='Point Inside')  # Green if inside
    else:
        plt.plot(x, y, 'ro', label='Point Outside')  # Red if outside

    ax.set_xlim(min(xmin, x) - 10, max(xmax, x) + 10)
    ax.set_ylim(min(ymin, y) - 10, max(ymax, y) + 10)
    ax.set_aspect('equal')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Point Clipping")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function
def main():
    xmin = float(input("Enter xmin: "))
    ymin = float(input("Enter ymin: "))
    xmax = float(input("Enter xmax: "))
    ymax = float(input("Enter ymax: "))
    x = float(input("Enter x of point: "))
    y = float(input("Enter y of point: "))

    if point_clipping(x, y, xmin, ymin, xmax, ymax):
        print("The point is inside the clipping window.")
    else:
        print("The point is outside the clipping window.")

    plot_point_and_window(x, y, xmin, ymin, xmax, ymax)

# ✅ Corrected entry point
if __name__ == "__main__":
    main()
