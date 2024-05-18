import matplotlib.pyplot as plt

def scale_line(x1, y1, x2, y2, sx, sy):
    # Calculate scaled coordinates
    x1_scaled = x1 * sx
    y1_scaled = y1 * sy
    x2_scaled = x2 * sx
    y2_scaled = y2 * sy

    # Plot original line
    plt.plot([x1, x2], [y1, y2], color='blue', label='Original Line')

    # Plot scaled line
    plt.plot([x1_scaled, x2_scaled], [y1_scaled, y2_scaled], color='red', label='Scaled Line')

    # Set axis limits
    plt.xlim(min(x1, x2, x1_scaled, x2_scaled) - 5, max(x1, x2, x1_scaled, x2_scaled) + 5)
    plt.ylim(min(y1, y2, y1_scaled, y2_scaled) - 5, max(y1, y2, y1_scaled, y2_scaled) + 5)

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Scaling')
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# Take user input for line coordinates and scaling factors
x1, y1 = map(float, input("Enter coordinates of starting point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of ending point (x2 y2): ").split())
sx, sy = map(float, input("Enter scaling factors (sx sy): ").split())

# Call scale_line function with user input
scale_line(x1, y1, x2, y2, sx, sy)
