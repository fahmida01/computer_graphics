import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Faster Bouncing Ball")
screen.bgcolor("white")

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 0)

# Increase the speed of the ball
ball.dx = 5  # Increase this value for a faster horizontal movement
ball.dy = -5  # Increase this value for a faster vertical movement

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the screen edges
    if ball.xcor() > screen.window_width() / 2 or ball.xcor() < -screen.window_width() / 2:
        ball.dx *= -1  # Reverse the direction on collision with the left or right edge

    if ball.ycor() > screen.window_height() / 2 or ball.ycor() < -screen.window_height() / 2:
        ball.dy *= -1  # Reverse the direction on collision with the top or bottom edge

    # Update the screen
    screen.update()
