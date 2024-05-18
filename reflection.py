import matplotlib.pyplot as plt

# Define the polygon points
polygon_points = [[10, 100], [110, 100], [110, 200]]

def plot_polygon(points):
    # Plot the x and y axes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='pink', linewidth=0.5)

    # Plot the polygon
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        plt.plot([x1, x2], [y1, y2], color='violet')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Polygon Reflection')

    # Set axis limits
    plt.xlim(min([p[0] for p in points]) - 50, max([p[0] for p in points]) + 50)
    plt.ylim(min([p[1] for p in points]) - 50, max([p[1] for p in points]) + 50)

    # Show plot
    plt.grid(True)
    plt.show()

def reflect_polygon(points):
    # Reflect the polygon across the x-axis
    reflected_points = [[x, -y] for x, y in points]
    return reflected_points

# Plot the original polygon
plot_polygon(polygon_points)

# Reflect the polygon and plot again
reflected_polygon = reflect_polygon(polygon_points)
plot_polygon(reflected_polygon)
