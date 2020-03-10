import turtle

#making a window/drawing board display
wn = turtle.Screen()
wn.bgcolor('orange')
wn.title("Workshop turtle")


# making a turtle. Bringing it to life
sks = turtle.Turtle()


#shape of turtle initially its an arrow
sks.shape('turtle')


#moving the turtle
sks.forward(100)


# making a square with --> for loop
for i in range(4):
	sks.forward(50)
	sks.right(90)


turtle.done()