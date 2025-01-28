import turtle

# create a new turtle object
t = turtle.Turtle()

# set the speed of the turtle
t.speed(1)

# draw a triangle using the turtle
for i in range(3):  # we have 3 sides for a triangle
    t.forward(100)  # move the turtle forward 100 units
    t.right(120)   # turn the turtle right by 120 degrees to create an angle of 60 degrees

# hide the turtle and show the plot
t.hideturtle()
turtle.done()
