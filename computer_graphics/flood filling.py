import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Set image dimensions
WIDTH, HEIGHT = 300, 300

def flood_fill_iterative(x, y, fill_color, target_color, img):
    """Iterative 4-connected flood fill to avoid recursion errors."""
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        current_color = img.getpixel((x, y))

        if current_color == target_color and current_color != fill_color:
            img.putpixel((x, y), fill_color)
            if x + 1 < WIDTH: stack.append((x + 1, y))
            if x - 1 >= 0: stack.append((x - 1, y))
            if y + 1 < HEIGHT: stack.append((x, y + 1))
            if y - 1 >= 0: stack.append((x, y - 1))

def main():
    print("--- Flood Fill Algorithm (Iterative) ---")
    
    # Get polygon points from user
    n = int(input("Enter number of polygon vertices: "))
    polygon = []
    for i in range(n):
        x = int(input(f"Enter x{i+1}: "))
        y = int(input(f"Enter y{i+1}: "))
        polygon.append((x, y))
    
    seed_x = int(input("Enter seed X: "))
    seed_y = int(input("Enter seed Y: "))

    # Colors
    fill_color = (255, 0, 0)   # Red
    polygon_color = (0, 0, 0)  # Black
    background_color = (255, 255, 255)  # White

    # Create white image
    img = Image.new("RGB", (WIDTH, HEIGHT), background_color)
    draw = ImageDraw.Draw(img)

    # Draw polygon with border
    draw.polygon(polygon, outline=polygon_color, fill=background_color)

    # Target color is the area to be filled (usually background inside polygon)
    target_color = img.getpixel((seed_x, seed_y))

    # Apply flood fill (iterative)
    flood_fill_iterative(seed_x, seed_y, fill_color, target_color, img)

    # Show the result
    plt.imshow(img)
    plt.title("Flood Fill (Iterative)")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()