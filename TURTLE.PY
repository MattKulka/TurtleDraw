from turtle import * # imports turtle,
                    #* stands for all

speed(0) # sets the speed of drawing, 0 is fast
pencolor('yellow') # sets the color of the lines
bgcolor('black') # sets the color of the background

x = 0 
up() 

#fd() means forward, bk() means back
# rt() or lt() means tilt right with an angle

rt(34) 
fd(96) 
rt(200) 

down() # sets down the pen, so the drawing can occur
while x < 120: # while the value of x is lesser than 120,
                #continuously do this:
    fd(300)     
    rt(150)
    fd(300)
    rt(150)
    fd(300)
    rt(150)
    fd(300)
    rt(150)
    fd(300)
    rt(150)
    fd(300)
    rt(150)

    rt(11.1111) 
    x = x+1 # adds 1 to the value of x,
            # so its closer to 120 after every loop

exitonclick() # Exits on click

