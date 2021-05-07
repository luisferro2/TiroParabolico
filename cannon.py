# Standard library.
from random import randrange

# Third party related imports.
from turtle import clear, goto, dot,       \
                   update, ontimer, setup, \
                   hideturtle, up, tracer, \
                   onscreenclick, done
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 7#(x + 200) / 25# 200/25
        speed.y = (y + 200) / 7 #(y + 200) / 25


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= randrange(1, 4)  # 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    #Reposition balls when they reach the edge of the screen
    for target in targets:
        if not inside(target):
            target.x = randrange(-150, 150)
            target.y = randrange(-150, 150)
            draw()

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)

onscreenclick(tap)
move()

done()