import matplotlib.pyplot as plt
import math


# Function for translating points
def translate_point(x, y, tx, ty):
    x_new = x + tx
    y_new = y + ty
    return x_new, y_new


# Function for scaling points
def scale_point(x, y, sx, sy):
    return x * sx, y * sy


# Function for reflecting points
def reflect_shape(points, mode="x"):
    if mode == "x":
        return [(x, -y) for x, y in points]
    elif mode == "y":
        return [(-x, y) for x, y in points]
    elif mode == "origin":
        return [(-x, -y) for x, y in points]
    else:
        raise ValueError("Invalid reflection mode")


# Function for rotating points
def rotate_point(x, y, angle_deg):
    angle_rad = math.radians(angle_deg)
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return (x_new, y_new)


def rotate_shape(points, angle_deg, clockwise=False):
    if clockwise:
        angle_deg = -angle_deg
    return [rotate_point(x, y, angle_deg) for x, y in points]


# Function to get user input for points
def get_points():
    original_points = []
    n = int(input("Enter the number of points in the shape: "))
    print("Enter the points as x y coordinates:")
    for i in range(n):
        x = float(input(f"  Point {i + 1} - x: "))
        y = float(input(f"  Point {i + 1} - y: "))
        original_points.append((x, y))
    return original_points


# Function for translation
def translate():
    original_points = get_points()
    tx = float(input("Enter translation in x-direction (tx): "))
    ty = float(input("Enter translation in y-direction (ty): "))
    translated_points = [translate_point(x, y, tx, ty) for x, y in original_points]

    x_orig, y_orig = zip(*original_points + [original_points[0]])
    x_trans, y_trans = zip(*translated_points + [translated_points[0]])

    plt.figure(figsize=(6, 6))
    plt.plot(x_orig, y_orig, label='Original Shape', color='blue')
    plt.plot(x_trans, y_trans, label='Translated Shape', color='red')
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.title('2D Translation in Computer Graphics')
    plt.legend()
    plt.show()


# Function for scaling
def scale():
    original_points = get_points()
    sx = float(input("Enter scaling factor along X (sx): "))
    sy = float(input("Enter scaling factor along Y (sy): "))
    scaled_points = [scale_point(x, y, sx, sy) for x, y in original_points]

    if original_points[0] != original_points[-1]:
        original_points.append(original_points[0])
        scaled_points.append(scaled_points[0])

    x_orig, y_orig = zip(*original_points)
    x_scaled, y_scaled = zip(*scaled_points)

    plt.figure(figsize=(6, 6))
    plt.plot(x_orig, y_orig, label='Original Shape', color='blue', marker='o')
    plt.plot(x_scaled, y_scaled, label='Scaled Shape', color='green', marker='o')
    plt.title('2D Scaling in Computer Graphics')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.show()


# Function for reflection
def reflect():
    original_points = get_points()
    print("\nChoose reflection mode:")
    print(" 1. Reflect over X-axis")
    print(" 2. Reflect over Y-axis")
    print(" 3. Reflect over Origin")
    mode = input("Enter mode (x, y, origin): ").strip().lower()

    reflected_points = reflect_shape(original_points, mode=mode)

    x_orig, y_orig = zip(*original_points)
    x_reflected, y_reflected = zip(*reflected_points)

    plt.figure(figsize=(8, 8))
    plt.plot(x_orig, y_orig, label='Original', marker='o')
    plt.plot(x_reflected, y_reflected, label=f'Reflected over {mode}-axis', marker='o')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.title(f"Reflection in Computer Graphics (Reflected over {mode}-axis)")
    plt.show()


# Function for rotation
def rotate():
    original_points = get_points()
    angle_deg = float(input("Enter the rotation angle in degrees: "))
    direction = input("Enter rotation direction (clockwise/anticlockwise): ").strip().lower()

    clockwise = True if direction == "clockwise" else False

    rotated_points = rotate_shape(original_points, angle_deg, clockwise)

    x_orig, y_orig = zip(*original_points)
    x_rot, y_rot = zip(*rotated_points)

    plt.figure(figsize=(8, 8))
    plt.plot(x_orig, y_orig, label='Original', marker='o')
    plt.plot(x_rot, y_rot, label=f'Rotated {angle_deg}° {"Clockwise" if clockwise else "Anticlockwise"}', marker='o')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.title(f"2D Rotation: {angle_deg}° {'Clockwise' if clockwise else 'Anticlockwise'}")
    plt.show()


# Main menu
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Translation")
        print("2. Scaling")
        print("3. Reflection")
        print("4. Rotation")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            translate()
        elif choice == '2':
            scale()
        elif choice == '3':
            reflect()
        elif choice == '4':
            rotate()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
