import matplotlib.pyplot as plt

def draw_circle(radius):
    x = 0
    y = radius
    p = 1 - radius  # Initial value of decision parameter

    # Plot initial point
    plot_points(x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_points(x, y)

def plot_points(x, y):
    # Plot points in all octants
    plt.scatter(x, y, color='blue')
    plt.scatter(y, x, color='blue')
    plt.scatter(y, -x, color='blue')
    plt.scatter(x, -y, color='blue')
    plt.scatter(-x, -y, color='blue')
    plt.scatter(-y, -x, color='blue')
    plt.scatter(-y, x, color='blue')
    plt.scatter(-x, y, color='blue')

# Get user input for the radius of the circle
radius = int(input("Enter the radius of the circle: "))
draw_circle(radius)

plt.gca().set_aspect('equal', adjustable='box')
plt.title('Midpoint Circle Algorithm')
plt.grid(True)
plt.show()
