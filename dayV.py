import turtle

turtle.setup(500, 500)
turtle.title("Валентинка")
valen = turtle.Turtle()
valen.penup()
valen.goto(35, -50)
valen.pendown()
valen.color("red", "pink")
def serdce():  
    valen.begin_fill()
    valen.left(160)
    valen.forward(140)
    valen.circle(-90, 190)
    valen.setheading(60)
    valen.circle(-90, 190)
    valen.forward(141)
    valen.fillcolor("pink")
    valen.end_fill()

def write():
    valen.penup()
    valen.goto(-60, -170)
    valen.write("I love you!", font=("Monotype Corsiva", 25, "normal"))
    valen.pendown()


lefth()
write()

valen.ht()
valen.screen.mainloop()
