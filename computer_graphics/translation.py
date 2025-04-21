import matplotlib.pyplot as plt

def translate_shape(points, tx, ty):
    """Translate a list of (x, y) points by tx and ty."""
    return [(x + tx, y + ty) for x, y in points]

def plot_shapes(original, translated, tx, ty):
    """Plot original and translated shapes."""
    # Close the shapes by adding the first point to the end
    original_closed = original + [original[0]]
    translated_closed = translated + [translated[0]]

    x_orig, y_orig = zip(*original_closed)
    x_trans, y_trans = zip(*translated_closed)

    plt.figure(figsize=(6, 6))
    plt.plot(x_orig, y_orig, label='Original Shape', color='blue', marker='o')
    plt.plot(x_trans, y_trans, label=f'Translated Shape\n(tx={tx}, ty={ty})', color='red', marker='o')

    plt.title('2D Translation in Computer Graphics')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.gca().set_aspect('equal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

# Define shape and translation values
original_points = [(1, 1), (4, 1), (2.5, 4), (4, 9)]
tx, ty = 3, 2

translated_points = translate_shape(original_points, tx, ty)
plot_shapes(original_points, translated_points, tx, ty)
