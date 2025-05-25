import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Set image dimensions
WIDTH, HEIGHT = 300, 300

def boundary_fill_iterative(x, y, fill_color, boundary_color, img):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            current_color = img.getpixel((x, y))
            if current_color != boundary_color and current_color != fill_color:
                img.putpixel((x, y), fill_color)
                stack.extend([
                    (x + 1, y), (x - 1, y),
                    (x, y + 1), (x, y - 1)
                ])

def main():
    print("--- Boundary Fill Algorithm ---")
    
    # Get polygon points from user
    n = int(input("Enter number of polygon vertices: "))
    polygon = []
    for i in range(n):
        x = int(input(f"Enter x{i+1}: "))
        y = int(input(f"Enter y{i+1}: "))
        polygon.append((x, y))
    
    seed_x = int(input("Enter seed X: "))
    seed_y = int(input("Enter seed Y: "))

    # Colors as (R, G, B)
    boundary_color = (0, 0, 0)  # Black
    fill_color = (255, 0, 0)    # Red

    # Create white image
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)

    # Draw the polygon
    draw.polygon(polygon, outline=boundary_color)

    # Apply boundary fill (iterative)
    boundary_fill_iterative(seed_x, seed_y, fill_color, boundary_color, img)

    # Show the result
    plt.imshow(img)
    plt.title("Boundary Fill")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()