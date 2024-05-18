import math
import matplotlib.pyplot as plt

def rotate_line(x1, y1, x2, y2, angle):
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Perform rotation
    x3 = x1 * math.cos(angle_rad) - y1 * math.sin(angle_rad)
    y3 = x1 * math.sin(angle_rad) + y1 * math.cos(angle_rad)
    x4 = x2 * math.cos(angle_rad) - y2 * math.sin(angle_rad)
    y4 = x2 * math.sin(angle_rad) + y2 * math.cos(angle_rad)
    
    # Plot original line
    plt.plot([x1, x2], [y1, y2], color='blue', label='Original Line')
    plt.text(x2 + 0.1, y2 + 0.1, "Original line")
    
    # Plot rotated line
    plt.plot([x3, x4], [y3, y4], color='red', label='Line after rotation')
    plt.text(x4 + 0.1, y4 + 0.1, "Line after rotation")

    # Set axis limits
    plt.xlim(min(x1, x2, x3, x4) - 5, max(x1, x2, x3, x4) + 5)
    plt.ylim(min(y1, y2, y3, y4) - 5, max(y1, y2, y3, y4) + 5)

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Rotation')
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# Take user input for line coordinates and rotation angle
x1, y1 = map(float, input("Enter coordinates of starting point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of ending point (x2 y2): ").split())
angle = float(input("Enter angle for rotation in degrees: "))

# Call rotate_line function with user input
rotate_line(x1, y1, x2, y2, angle)
