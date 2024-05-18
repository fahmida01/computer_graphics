import matplotlib.pyplot as plt

def plot_shape(points, title):
    # Plot the shape
    x_vals, y_vals = zip(*points)
    plt.plot(x_vals, y_vals, color='blue')
    
    # Set axis limits and labels
    plt.xlim(min(x_vals) - 5, max(x_vals) + 5)
    plt.ylim(min(y_vals) - 5, max(y_vals) + 5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

def shear_shape(points, shear_x, shear_y):
    # Apply shear transformation to the points
    sheared_points = [[x + shear_x * y, y + shear_y * x] for x, y in points]
    return sheared_points

def main():
    # Take user input for shape vertices
    num_points = int(input("Enter the number of vertices for the shape: "))
    shape_points = []
    for i in range(num_points):
        x, y = map(float, input(f"Enter x and y coordinates for vertex {i+1}: ").split())
        shape_points.append([x, y])

    # Take user input for shearing factors
    shear_x = float(input("Enter the shearing factor for x-direction: "))
    shear_y = float(input("Enter the shearing factor for y-direction: "))

    # Plot the original shape
    plot_shape(shape_points, "Original Shape")

    # Shear the shape and plot again
    sheared_shape = shear_shape(shape_points, shear_x, shear_y)
    plot_shape(sheared_shape, "Sheared Shape")

if __name__ == "__main__":
    main()
