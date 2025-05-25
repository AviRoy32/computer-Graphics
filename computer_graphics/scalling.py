import matplotlib.pyplot as plt

def scale_shape(points, sx, sy):
    """Scales a shape's points by factors sx and sy."""
    return [(x * sx, y * sy) for x, y in points]

def plot_scaled_shape(original, scaled, sx, sy):
    """Plots original and scaled shapes."""
    x_orig, y_orig = zip(*original)
    x_scaled, y_scaled = zip(*scaled)

    plt.figure(figsize=(6, 6))
    plt.plot(x_orig, y_orig, label='Original Shape', color='blue', marker='o')
    plt.plot(x_scaled, y_scaled, label=f'Scaled Shape\n(Sx={sx}, Sy={sy})', color='green', marker='o')

    plt.title('2D Scaling in Computer Graphics')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.gca().set_aspect('equal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# Triangle shape (closed)
original_shape = [(1, 1), (2, 3), (3, 1), (1, 1)]
sx, sy = 2, 1.5

scaled_shape = scale_shape(original_shape, sx, sy)
plot_scaled_shape(original_shape, scaled_shape, sx, sy)
