import matplotlib.pyplot as plt

def translate_line(x1, y1, x2, y2, tx, ty):
    # Calculate translated coordinates
    x1_new = x1 + tx
    y1_new = y1 + ty
    x2_new = x2 + tx
    y2_new = y2 + ty

    # Plot original line
    plt.plot([x1, x2], [y1, y2], label='Original Line')

    # Plot translated line
    plt.plot([x1_new, x2_new], [y1_new, y2_new], label='Translated Line')

    # Set axis limits
    plt.xlim(min(x1, x2, x1_new, x2_new) - 5, max(x1, x2, x1_new, x2_new) + 5)
    plt.ylim(min(y1, y2, y1_new, y2_new) - 5, max(y1, y2, y1_new, y2_new) + 5)

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Translation')
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# Take user input for line coordinates
x1 = float(input("Enter x-coordinate of the starting point of line segment: "))
y1 = float(input("Enter y-coordinate of the starting point of line segment: "))
x2 = float(input("Enter x-coordinate of the ending point of line segment: "))
y2 = float(input("Enter y-coordinate of the ending point of line segment: "))

# Take user input for translation vector
tx = float(input("Enter translation distance in x-direction: "))
ty = float(input("Enter translation distance in y-direction: "))

# Call translate_line function with user input
translate_line(x1, y1, x2, y2, tx, ty)
