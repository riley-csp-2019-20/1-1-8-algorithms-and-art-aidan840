import turtle as trtl

dice = trtl.Turtle()

wn = trtl.Screen()
wn.bgcolor("light blue")

dice.forward(100)
dice.right(90)
dice.forward(100)
dice.right(90)
dice.forward(100)
dice.right(90)
dice.forward(100)
dice.penup()
dice.goto(60,-50)
dice.pendown()
dice.fillcolor("blue")
dice.begin_fill()
dice.circle(10)
dice.end_fill()
dice.penup()
dice.goto(30,-20)
dice.pendown()
dice.fillcolor("blue")
dice.begin_fill()
dice.circle(10)
dice.end_fill()
dice.penup()
dice.goto(90,-80)
dice.pendown()
dice.fillcolor("blue")
dice.begin_fill()
dice.circle(10)
dice.end_fill()

dice.clear()

dice.forward(100)
dice.right(90)
dice.forward(100)
dice.right(90)
dice.forward(100)
dice.right(90)
dice.forward(100)
dice.penup()
dice.goto(110,5)
dice.pendown()
dice.fillcolor("red")
dice.begin_fill()
dice.circle(10)
dice.end_fill()
dice.penup()
dice.goto(140,-20)
dice.pendown()
dice.fillcolor("red")
dice.begin_fill()
dice.circle(10)
dice.end_fill()
dice.penup()
dice.goto(170,-50)
dice.pendown()
dice.fillcolor("red")
dice.begin_fill()
dice.circle(10)
dice.end_fill()
dice.penup()
dice.goto(170,5)
dice.pendown()
dice.fillcolor("red")
dice.begin_fill()
dice.circle(10)
dice.end_fill()
dice.penup()
dice.goto(110,-50)
dice.pendown()
dice.fillcolor("red")
dice.begin_fill()
dice.circle(10)
dice.end_fill()










wn.mainloop()