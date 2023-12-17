# import turtle animation package
import turtle
 
# set screen and background color
window = turtle.Screen()
window.bgcolor("black")
 
# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("brown")
pumpkin.dot(200)
pumpkin.forward(60)
pumpkin.dot(200)

# The turtle to "draw" the pumpkin
draw = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
draw.penup()
draw.setposition(-200, -100)
draw.pensize(35)
draw.pendown()
draw.forward(600)
draw.pensize(2)

#Function to carve pumpkin 
def draw_pumpkin(colour):
   draw.color(colour)

   # Make eyes
   def make_eye(start, position):
       draw.setheading(0)
       draw.penup()
       draw.setposition(*start)
       draw.pendown()
       draw.begin_fill()
       draw.forward(position * 40)
       draw.setheading(position * 135)
       draw.forward(position * 70)
       draw.end_fill()

   make_eye((-20, 20), 1)
   make_eye((80, 20), -1)

   # Make mouth
   draw.penup()
   draw.setposition(-20, -30)
   draw.setheading(45)
   draw.pendown()
   draw.pensize(1)
   draw.begin_fill()
   for _ in range(5):
       draw.forward(15)
       draw.right(90)
       draw.forward(15)
       draw.left(90)
   draw.setheading(260)
   draw.forward(20)
   draw.setheading(180)
   draw.forward(99)
   draw.end_fill()

   # Make nose
   draw.penup()
   draw.setposition(30, 0)
   draw.setheading(90)
   draw.shape("triangle")
   draw.stamp()

# Call the function with a color to carve the pumpkin
draw_pumpkin("yellow")

# Write text on animation
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.sety(175)
text.write("ANGRY PUMPKIN - Turtle drew this!", font=("Trattatello", 28, "bold"), align="center")

# Execute turtle animation completion
turtle.done()