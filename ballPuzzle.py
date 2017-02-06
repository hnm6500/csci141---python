
                                                                     #Hrishikesh Moholkar
"""
This  python file ballPuzzle sorts the ball as per their color.Imports special
functions from the files specified below.
"""



from rit_lib import *
from myStack import *
from myNode import *
from ballPuzzle_animate import *
"""
each can is initially an empty node.then
they are stored in a list.
"""


red_can=EMPTY_NODE
green_can=EMPTY_NODE
blue_can=EMPTY_NODE
stackList=[red_can,green_can,blue_can]

def add(x):
    """
    add function goes through the input which is a string and
    treats each character of string as object and put them
    into the can respectively.Thus the  first can now indicates non empty node.
    """
    for i in range(0,len(x)):
        stackList[0]=push(stackList[0],x[i])

def sort():
    """
    sort function sorts the ball as per their color
    into the respective can (from first to second and third.)
    Sorts green ball.
    """

    while emptyStack(stackList[0]) == False:
        obj1=top(stackList[0])
        stackList[0]=pop(stackList[0])
        if obj1=="G":

            stackList[1]=push(stackList[1],obj1)
            animate_move(stackList,0,1)
        else:
            stackList[2]=push(stackList[2],obj1)
            animate_move(stackList,0,2)

def sort1():
    """
    the sort1 function sorts the ball from third can to the first
    and second .Sorts red ball.
    """

    while emptyStack(stackList[2]) == False:
        obj1=top(stackList[2])

        stackList[2]=pop(stackList[2])
        if obj1=="R":
            stackList[0]=push(stackList[0],obj1)
            animate_move(stackList,2,0)

        else:
            stackList[1]=push(stackList[1],obj1)
            animate_move(stackList,2,1)



def finalsort():
    """
    final sort function sorts the blue ball
    :return:none
    """



    while emptyStack(stackList[1])==False and top(stackList[1])=="B":
        obj1=top(stackList[1])
        stackList[1]=pop(stackList[1])


        stackList[2]=push(stackList[2],obj1)
        animate_move(stackList,1,2)



def main():
    """
    animate_init functions starts the animation and
    animate_move performs the animation .
    animate_finish finishes the animation by closing the turtle
    window.(functions imported from ball puzzle_animate file.
    :return:
    """
    x=input("Enter three types of colour(R,G,B):")
    animate_init(x)
    add(x)
    sort()
    sort1()
    finalsort()


main()
input("PRESS ENTER TO EXIT")
animate_finish()










