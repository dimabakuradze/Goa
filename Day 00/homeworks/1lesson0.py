from turtle import *


width(7)
color("black")
speed(5)
#step one 1: draw square
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square
#start of door
begin_fill()
forward(70)
color("blue")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#step of roof
penup()
goto(200, 200)  
pendown()
begin_fill() 
color("black")
right(150)
forward(200)
left(120)
forward(200)
end_fill()
 





exitonclick()
        
        