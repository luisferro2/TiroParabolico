# Standard library.
from random import randrange

# Third party related imports.
from turtle import clear, goto, dot,       \
                   update, ontimer, setup, \
                   hideturtle, up, tracer, \
                   onscreenclick, done
from freegames import vector

ball = vector(-200, -200)  # Position of the ball.
speed = vector(0, 0)  # Speed of the ball.
targets = []  # Target balls.


def tap(x, y):
    """
    Change the speed of the cannon ball with the tap.

    A tap on coordinates x, y needs to be adjusted to make the
    coordinates positive. It is also scaled down so it´s not too quick.

    Parameters:
    x: int -- x coordinate.
    y: int -- y coordinate.

    Returns:
    None
    """

    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # The coordinates of the tap indicate the speed vector of
        # ball. Sum 200 to make the lower left corner the (0, 0).
        speed.x = (x + 200) / 7  # Faster throw, it was / 25.
        speed.y = (y + 200) / 7


def inside(xy):
    """Returns whether or not the given xy vector fits to screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Clears screen, draws cannon ball and target balls on screen."""
    clear()  # Clears the screen before drawing new balls.

    # Draw the target balls.
    for target in targets:
        goto(target.x, target.y)  # Move pointer to position.
        dot(20, "blue")

    # Draw the cannon ball.
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    # Update the screen.
    update()


def move():
    """
    Manage the movement of balls and their interactions.

    
    This function generates the target balls, it moves them to the
    left, it moves the cannon ball downwards to simulate gravity,
    it removes the target balls that are hit by the cannon ball
    and repositions the target balls once they hit the screen.

    Parameters:
    None

    Returns:
    None
    """

    # Generate a target balls, 1/40 chance.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move target balls left
    for target in targets:
        target.x -= randrange(1, 4)  # Speed increased, it was 0.5.

    # Move the cannon ball down (simulate gravity).
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Copy the list of target balls.
    dupe = targets.copy()
    targets.clear()

    # Remove the target balls that were hit.
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    #Reposition balls when they reach the edge of the screen
    for target in targets:
        if not inside(target):
            target.x = randrange(-150, 150)
            target.y = randrange(-150, 150)
            draw()  # Draw all balls.

    # Wait 50 ms to call move function.
    ontimer(move, 50)


# Initial steps.
setup(420, 420, 370, 0)
hideturtle()  # Turtle invisible.
up()  # No drawing when moving.
tracer(False)  # Turtle animation off.

onscreenclick(tap)  # Call tap when screen is clicked.
move()

done()  # The event loop.