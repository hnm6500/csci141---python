                       #Hrishikesh N Moholkar

import turtle
import math                    #import the mathematical functions
turtle.setup(900,100)             #sets the coordinate of window
turtle.setworldcoordinates(-10,-10,450,30)        #SETS THE START POINT AND END POINT OF WORD
def Bletter():
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.forward(5)
    turtle.left(90)
    turtle.right(90)
    turtle.forward(5)
    turtle.forward(-5)
    turtle.left(90)
    turtle.up()
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.forward(5)
    turtle.up()
    turtle.forward(-10)
    turtle.right(90)
def Aletter():
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(5)
    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.forward(5)
    turtle.left(90)
def Nletter():
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.right(45)
    turtle.forward(14)
    turtle.left(135)
    turtle.forward(10)
    turtle.up()
    turtle.forward(-10)
    turtle.left(90)
    turtle.forward(10)
    turtle.down()
    turtle.right(180)
def Rletter():
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(135)
    turtle.forward(5*math.sqrt(2))
    turtle.right(135)
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.right(180)
def Mletter():
    turtle.left(90)
    turtle.forward(10)
    turtle.right(135)
    turtle.forward(5*math.sqrt(2))
    turtle.left(90)
    turtle.forward(5*math.sqrt(2))
    turtle.right(135)
    turtle.forward(10)
    turtle.right(90)
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.left(180)
def Cletter():
    turtle.forward(10)
    turtle.forward(-10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.left(90)
def Sletter():
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(10)
    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
def Iletter():
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(5)
    turtle.forward(-5)
    turtle.right(180)
    turtle.forward(5)
    turtle.forward(-5)
    turtle.right(90)
    turtle.up()
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.forward(5)

def space():       #it is used to provide space between each letter
    turtle.up()
    turtle.forward(30)
    turtle.down()

def main():
    Bletter()
    turtle.forward(20)
    Aletter()
    space()
    Nletter()
    space()
    Aletter()
    space()
    Nletter()
    space()
    Aletter()
    space()
    Rletter()
    space()
    Aletter()
    space()
    Mletter()
    space()
    Aletter()
    turtle.up()
    turtle.forward(40)
    turtle.down()
    Cletter()
    space()
    Sletter()
    turtle.up()
    turtle.forward(40)
    turtle.down()
    Iletter()
    turtle.up()
    turtle.forward(20)
main()
input("hit enter to exit")