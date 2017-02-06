
    #HRISHIKESH N MOHOLKAR
import turtle
def drawtriangle():      # function which draws the basic triangle
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
def settriangle():      #function which sets the triangle for drawing triangle
    turtle.left(12)
    turtle.up()
    turtle.forward(60)
    turtle.right(180)
    turtle.down()
def main():             #execution starts after this point and draws a star by calling function multiple times
    drawtriangle()
    settriangle()
    drawtriangle()
    settriangle()
    drawtriangle()
    settriangle()
    drawtriangle()
    settriangle()
    drawtriangle()
    settriangle()

main()
input("click enter key to exit")     #holds the screen till user presses the key