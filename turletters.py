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
    elif letter == "L":
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
    elif letter == "M": #END
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

    elif letter == "N":
	t.right(90)
    	t.width(1)
    	t.right(90)
    	t.penup()
    	t.forward(60)
   	t.left(90)
    	t.forward(5)
    	t.left(90)
    	t.forward(5)
    	t.pendown()
    	t.width(5)
    	t.width(5)
    	t.forward(45)
    	t.right(150)
    	t.forward(50)
    	t.left(150)
    	t.forward(45)
    	t.penup()
    	t.forward(5)
    	t.right(90)
    	t.forward(5)
    elif letter == "O":
	t.right(90)
   	t.width(1)
    	t.right(90)
    	t.penup()
    	t.forward(60)
    	t.left(90)
    	t.forward(5)
    	t.left(90)
    	t.forward(5)
    	t.pendown()
    	##above lines put cursor in starting position for bottom corner of letter
    	t.width(5)
    	for i in range(2):
        	t.forward(50)
        	t.right(90)
        	t.forward(30)
        	t.right(90)
    	t.penup()
    	t.forward(55)
    	t.right(90)
    	t.forward(35)
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
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
