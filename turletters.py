import turtle
for i in range (10):
	print("Hi")
def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
	tur.width(5)
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(30)
        tur.backward(20)
        tur.right(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
    elif letter == "C": 
  	 tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.backward(30)
        tur.left(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "D":
 	tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.circle(25,180)
        tur.pu()
        tur.right(180)
        tur.fd(35)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "E":
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.backward(30)
        tur.left(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.backward(30)
        tur.left(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "F":
  	tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.backward(25)
        tur.left(90)
        tur.fd(30)
        tur.backward(30)
        tur.left(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "G":
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(3)
        tur.backward(10)
        tur.pu()
        tur.left(90)
        tur.fd(35)
        tur.left(90)
        tur.pd()
        tur.fd(20)
        tur.backward(20)
        tur.right(180)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(8)
    elif letter == "H":
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.backward(25)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(25)
        tur.backward(50)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "I":
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.pu()
        tur.fd(15)
        tur.right(90)
        tur.pd()
        tur.fd(50)
        tur.pu()
        tur.backward(50)
        tur.right(270)
        tur.fd(20)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "J":
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.fd(30)
        tur.backward(15)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(10)
        tur.pu()
        tur.fd(45)
        tur.right(90)
        tur.fd(35)
    elif letter == "K":
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.backward(25)
        tur.left(50)
        tur.fd(35)
        tur.backward(35)
        tur.left(70)
        tur.fd(30)
        tur.left(60)
        tur.pu()
        tur.fd(15)
        tur.right(90)
        tur.fd(10)
    elif letter == "L"
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.backward(30)
        tur.left(90)
        tur.fd(50)
        tur.right(90)
        tur.pu()
        tur.fd(30)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.right(180)
        tur.fd(15)
        tur.right(90)
    elif letter == "M": 
        tur.width(5)
        tur.pu()
        tur.setheading(0)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.backward(50)
        tur.left(50)
        tur.fd(20)
        tur.right(280)
        tur.fd(20)
        tur.right(130)
        tur.fd(50)
        tur.backward(50)
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "N":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	tur.width(5)
    	tur.width(5)
    	tur.forward(45)
    	tur.right(150)
    	tur.forward(50)
    	tur.left(150)
    	tur.forward(45)
    	tur.penup()
    	tur.forward(5)
    	tur.right(90)
    	tur.forward(5)

    elif letter == "O":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.width(5)
    	for i in range(2):
        	tur.forward(50)
        	tur.right(90)
        	tur.forward(30)
        	tur.right(90)
    	tur.penup()
    	tur.forward(55)
    	tur.right(90)
    	tur.forward(35)

    elif letter == "P":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##Above lines are cornerpos
    	tur.width(5)
    	tur.forward(50)
    	tur.right(90)
    	tur.forward(30)
    	tur.right(90)
    	tur.forward(25)
    	tur.right(90)
    	tur.forward(30)
    	tur.right(180)
    	tur.forward(30)
    	##finishes letter
    	tur.penup()
    	tur.left(90)
    	tur.forward(30)
    	##gets to line
    	tur.right(90)
    	tur.forward(5)
			
    elif letter == "Q":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##setpos
    	tur.width(5)
    	for i in range(2):
        	tur.forward(50)
        	tur.right(90)
        	tur.forward(30)
        	tur.right(90)
    	tur.right(90)
    	tur.forward(30)
    	tur.left(135)
    	tur.forward(10)
    	tur.forward(-12)
    	tur.forward(2)
    	tur.right(135)
    	tur.left(90)
    	tur.penup()
    	tur.forward(55)
    	tur.right(90)
    	tur.forward(5)

    elif letter == "R":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##Above lines are cornerpos
    	tur.width(5)
    	tur.forward(50)
    	tur.right(90)
    	tur.forward(30)
    	tur.right(90)
    	tur.forward(25)
    	tur.right(90)
    	tur.forward(30)
    	tur.left(135)
    	tur.forward(35)
    	tur.forward(-35)
    	tur.penup()
    	tur.right(135)
    	tur.right(90)
    	tur.forward(30)
    	tur.right(90)
    	tur.forward(40)

    elif letter == "S":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.width(5)
    	tur.penup()
    	tur.forward(50)
    	tur.pendown()
    	tur.right(90)
    	tur.forward(30)
    	tur.forward(-30)
    	tur.right(90)
    	tur.forward(25)
    	tur.left(90)
    	tur.forward(30)
    	tur.right(90)
    	tur.forward(25)
    	tur.right(90)
    	tur.forward(30)
    	tur.forward(-30)
    	tur.right(90)
    	tur.penup()
    	tur.forward(55)
    	tur.right(90)
    	tur.forward(5)

    elif letter == "T":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.width(5)
    	tur.penup()
    	tur.forward(50)
    	tur.right(90)
    	tur.pendown()
    	tur.forward(30)
    	tur.forward(-15)
    	tur.right(90)
    	tur.forward(50)
    	tur.forward(-50)
    	tur.left(180)
    	tur.penup()
    	tur.forward(5)
    	tur.right(90)
    	tur.forward(20)

    elif letter == "U":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.width(5)
    	tur.forward(50)
    	tur.right(90)
    	tur.penup()
    	tur.forward(30)
    	tur.right(90)
    	tur.pendown()
    	tur.forward(50)
    	tur.right(90)
    	tur.forward(30)
    	tur.right(90)
    	tur.penup()
    	tur.forward(55)
    	tur.right(90)
    	tur.forward(35)

    elif letter == "V":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.penup()
    	tur.width(5)
    	tur.forward(50)
    	tur.right(160)
    	tur.pendown()
    	tur.forward(50)
    	tur.left(145)
    	tur.forward(50)
    	tur.left(15)
    	tur.penup()
    	tur.forward(5)
    	tur.right(90)
    	tur.forward(5)

    elif letter == "W":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
	##above lines put cursor in starting position for bottom corner of letter
    	tur.penup()
    	tur.width(5)
    	tur.forward(50)
    	tur.right(170)
    	tur.pendown()
    	tur.forward(50)
    	tur.left(160)
    	tur.forward(30)
    	tur.right(160)
    	tur.forward(30)
    	tur.left(160)
    	tur.forward(50)
    	tur.left(10)
    	tur.penup()
    	tur.forward(5)
    	tur.right(90)
    	tur.forward(5)

    elif letter == "X":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	tur.penup()
    	tur.width(5)
    	tur.forward(50)
    	tur.pendown()
    	tur.right(150)
    	tur.forward(50)
    	tur.forward(-25)
    	tur.left(120)
    	tur.forward(25)
    	tur.forward(-50)
    	tur.forward(25)
    	tur.penup()
    	tur.left(60)
    	tur.forward(25)
    	tur.right(30)
    	tur.forward(5)
    	tur.right(90)
    	tur.forward(35)

    elif letter == "Y":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.penup()
    	tur.width(5)
   	tur.forward(50)
    	tur.right(145)
    	tur.pendown()
    	tur.forward(30)
    	tur.left(120)
    	tur.forward(27)
    	tur.forward(-27)
    	tur.right(155)
    	tur.forward(25)
    	tur.forward(-25)
    	tur.right(180)
    	tur.penup()
    	tur.forward(30)
    	tur.right(90)
    	tur.forward(20)
    

    elif letter == "Z":
	tur.right(90)
    	boxy()
    	tur.width(1)
    	tur.right(90)
    	tur.penup()
    	tur.forward(60)
    	tur.left(90)
    	tur.forward(5)
    	tur.left(90)
    	tur.forward(5)
    	tur.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	tur.penup()
    	tur.width(5)
    	tur.forward(50)
    	tur.pendown()
    	tur.right(90)
    	tur.forward(30)
    	tur.right(120)
    	tur.forward(58)
    	tur.left(120)
    	tur.forward(30)
    	tur.penup()
    	tur.left(90)
    	tur.forward(55)
    	tur.right(90)
    	tur.forward(5)

		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    t = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
