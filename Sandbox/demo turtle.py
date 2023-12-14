import turtle

n = 7

def draw_polygon(n, d, fill_color, x, y):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    angle = 360 / n

    turtle.color('red', fill_color)
    turtle.begin_fill()

    for _ in range(n):
        turtle.forward(d)
        turtle.left(angle)

    turtle.end_fill()



draw_polygon(7, 100, 'orange', 100, -100)
draw_polygon(9, 50, 'red', -100, -100)
draw_polygon(5, 80, 'yellow', -10, 50)

turtle.done()

