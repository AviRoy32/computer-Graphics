import math
import matplotlib.pyplot as plt

# ----- Transformation Functions -----

def translate_shape(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]


def rotate_shape(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    return [
        (x * math.cos(angle_rad) - y * math.sin(angle_rad),
         x * math.sin(angle_rad) + y * math.cos(angle_rad))
        for x, y in points
    ]

def scale_shape(points, sx, sy):
    return [(x * sx, y * sy) for x, y in points]

def reflect_shape(points, axis):
    if axis == 'x':
        return [(x, -y) for x, y in points]
    elif axis == 'y':
        return [(-x, y) for x, y in points]
    elif axis == 'origin':
        return [(-x, -y) for x, y in points]
    else:
        raise ValueError("Invalid axis. Use 'x', 'y', or 'origin'.")

def shear_shape(points, shx, shy):
    return [(x + shx * y, y + shy * x) for x, y in points]

# ----- Drawing Function -----

def draw_shape(points_old, points_new, title):
    plt.figure()
    x_old, y_old = zip(*points_old)
    x_new, y_new = zip(*points_new)

    # Ensure closed shape
    if points_old[0] != points_old[-1]:
        x_old += (x_old[0],)
        y_old += (y_old[0],)

    if points_new[0] != points_new[-1]:
        x_new += (x_new[0],)
        y_new += (y_new[0],)

    plt.plot(x_old, y_old, 'ro-', label='Original/Previous Shape')
    plt.plot(x_new, y_new, 'go-', label='Transformed Shape')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

# ----- Input Shape Function -----

def get_shape():
    points = []
    try:
        n = int(input("Enter the number of points in the shape: "))
        if n < 1:
            print("A shape must have at least one point.")
            return []
        for i in range(n):
            x = float(input(f"Enter x{i+1}: "))
            y = float(input(f"Enter y{i+1}: "))
            points.append((x, y))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    return points

# ----- Main Menu -----

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Apply Composite Transformation to a Shape")
        print("2. Exit")
        main_choice = input("Choose an option (1-2): ")

        if main_choice == '1':
            points = get_shape()
            if not points:
                continue

            transformed_points = points[:]
            title = "Step-by-Step Transformations"

            while True:
                print("\n--- Transformation Menu ---")
                print("1. Translate")
                print("2. Rotate")
                print("3. Scale")
                print("4. Reflect")
                print("5. Shear")
                print("6. Done (Show Final Result)")

                choice = input("Choose a transformation (1-6): ")

                if choice == '1':
                    tx = float(input("Enter translation in x (tx): "))
                    ty = float(input("Enter translation in y (ty): "))
                    new_points = translate_shape(transformed_points, tx, ty)
                    draw_shape(transformed_points, new_points, f"{title} → Translate({tx},{ty})")
                    transformed_points = new_points
                    title += f" → Translate({tx},{ty})"

                elif choice == '2':
                    angle = float(input("Enter rotation angle (degrees): "))
                    direction = input("Direction (clockwise/anticlockwise): ").lower()
                    if direction == "clockwise":
                        angle = -angle
                    new_points = rotate_shape(transformed_points, angle)
                    draw_shape(transformed_points, new_points, f"{title} → Rotate({angle}°)")
                    transformed_points = new_points
                    title += f" → Rotate({angle}°)"

                elif choice == '3':
                    sx = float(input("Enter scaling in x (sx): "))
                    sy = float(input("Enter scaling in y (sy): "))
                    new_points = scale_shape(transformed_points, sx, sy)
                    draw_shape(transformed_points, new_points, f"{title} → Scale({sx},{sy})")
                    transformed_points = new_points
                    title += f" → Scale({sx},{sy})"

                elif choice == '4':
                    axis = input("Reflect across which axis? (x/y/origin): ").lower()
                    if axis in ['x', 'y', 'origin']:
                        new_points = reflect_shape(transformed_points, axis)
                        draw_shape(transformed_points, new_points, f"{title} → Reflect({axis})")
                        transformed_points = new_points
                        title += f" → Reflect({axis})"
                    else:
                        print("Invalid axis.")

                elif choice == '5':
                    shx = float(input("Enter shearing factor in x (shx): "))
                    shy = float(input("Enter shearing factor in y (shy): "))
                    new_points = shear_shape(transformed_points, shx, shy)
                    draw_shape(transformed_points, new_points, f"{title} → Shear({shx},{shy})")
                    transformed_points = new_points
                    title += f" → Shear({shx},{shy})"

                elif choice == '6':
                    print(f"\nFinal transformed points: {transformed_points}")
                    draw_shape(points, transformed_points, title + " (Final)")
                    break

                else:
                    print("Invalid choice. Please select from 1 to 6.")

        elif main_choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

# ----- Run Program -----

# ----- Run Program -----

if __name__ == "__main__":
    main()
