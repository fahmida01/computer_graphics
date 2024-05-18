import matplotlib.pyplot as plt

def translate_triangle(x1, y1, x2, y2, x3, y3, tx, ty):
    # Calculate translated coordinates
    x1_new, y1_new = x1 + tx, y1 + ty
    x2_new, y2_new = x2 + tx, y2 + ty
    x3_new, y3_new = x3 + tx, y3 + ty

    # Plot original triangle
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], label='Original Triangle')

    # Plot translated triangle
    plt.plot([x1_new, x2_new, x3_new, x1_new], [y1_new, y2_new, y3_new, y1_new], label='Translated Triangle')

    # Set axis limits
    plt.xlim(min(x1, x2, x3, x1_new, x2_new, x3_new) - 5, max(x1, x2, x3, x1_new, x2_new, x3_new) + 5)
    plt.ylim(min(y1, y2, y3, y1_new, y2_new, y3_new) - 5, max(y1, y2, y3, y1_new, y2_new, y3_new) + 5)

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Triangle Translation')
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# Take user input for triangle vertices
x1, y1 = map(float, input("Enter x and y coordinates of vertex A : ").split(','))
x2, y2 = map(float, input("Enter x and y coordinates of vertex B : ").split(','))
x3, y3 = map(float, input("Enter x and y coordinates of vertex C : ").split(','))

# Take user input for translation vector
tx, ty = map(float, input("Enter translation distances in x and y directions (comma-separated): ").split(','))

# Call translate_triangle function with user input
translate_triangle(x1, y1, x2, y2, x3, y3, tx, ty)
