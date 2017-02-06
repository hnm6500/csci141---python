

                             #Hrishikesh Moholkar

import turtle
import math
import random       #this contains random function library
def initialize():
    """
    sets the background of the picture
    :return:
    """
    turtle.setworldcoordinates(-400,-400,400,400)
    turtle.speed(5)

def drawarrow(num,area):
    """
      draws the arrows on layout using recursion.
    :param num:counts no .of arrows
    :param area:holds the area of each arrow printed
    :return:
    """
    if num<=0:
        return area
    elif num>500:
        print("ERROR")
    else:
        len=random.randint(1,30)
        turtle.color(random.random(),random.random(),random.random())
        turtle.begin_fill()
        turtle.forward(len)
        turtle.left(120)
        turtle.forward(len)
        turtle.left(120)
        turtle.forward(len)
        turtle.left(120)
        turtle.end_fill()
        turtle.up()
        turtle.forward(random.randint(MINSIZE(),MAXSIZE()))
        turtle.left(random.randint(-MAXANGLE(),MAXANGLE()))
        turtle.down()
        check()
        area=area+math.sqrt(3)*len*len/4
        return drawarrow(num-1,area)

def iter(num,area):
    """
     draws arrows using iteration.
    :param n:  no.of arrow
    :param area:    stores area of each arrow
    :return:
    """
    while num>0:
        len=random.randint(MINSIZE(),MAXSIZE())
        turtle.color(random.random(),random.random(),random.random())
        turtle.begin_fill()
        turtle.forward(len)
        turtle.left(120)
        turtle.forward(len)
        turtle.left(120)
        turtle.forward(len)
        turtle.left(120)
        turtle.end_fill()
        turtle.up()
        turtle.forward(random.randint(MINSIZE(),MAXSIZE()))
        turtle.left(random.randint(-MAXANGLE(),MAXANGLE()))
        turtle.down()
        check()
        area=area+math.sqrt(3)*len*len/4
        num = num - 1
    return area

def printrec(fignum):
    area = drawarrow(fignum,0)
    print("The total area is" ,area, "units")
    input("Hit enter to continue")

def printrec1(fignum):
    area = iter(fignum,0)
    print("The total area is",area,"unts")

def check():
    """
    helps in bringing the turtle in the range of printing.
    :return:
    """
    x,y=turtle.position()
    if x>360 or x<-360 or y>360 or y<-360:
        turtle.up()
        turtle.left(180)
        turtle.forward(random.randint(10,MAXSIZE()))
        turtle.down()



    else:
        return 0
def boundry():
    """
    sets the boundry conditions for movement of turtle.
    :return:
    """
    turtle.up()
    turtle.pencolor("black")
    turtle.setheading(0)
    turtle.goto(-380,-380)
    turtle.down()
    turtle.forward(760)
    turtle.left(90)
    turtle.forward(760)
    turtle.left(90)
    turtle.forward(760)
    turtle.left(90)
    turtle.forward(760)
    turtle.left(90)
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
def MAXSIZE():
    """
    max.size of length
    :return:
    """
    return 30
def MINSIZE():
    """
     min.size of length
    :return:
    """
    return 1
def MAXANGLE():
    """
    max.angle rotated
    :return:
    """
    return 30


def main():
    initialize()
    boundry()
    fignum = int(input("Arrows(0-500):"))
    printrec(fignum)
    turtle.clear()
    initialize()
    boundry()
    printrec1(fignum)

main()

input("Hit enter to close.. ")
