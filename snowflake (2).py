                    #hrishikesh moholkar

import turtle
def star(S,N):
    """

   :param S: lenght of snowflake
   :param N: counter (depth)
   :return:none
    """
    if N<=0:
        return 0

    turtle.forward(S)
    snowflake(S/3,N)
    turtle.back(S)
    turtle.left(60)
    turtle.forward(S)
    snowflake(S/3,N)
    turtle.back(S)
    turtle.left(60)
    turtle.forward(S)
    snowflake(S/3,N)
    turtle.back(S)
    turtle.left(60)
    turtle.forward(S)
    snowflake(S/3,N)
    turtle.back(S)
    turtle.left(60)
    turtle.forward(S)
    snowflake(S/3,N)
    turtle.back(S)
    turtle.left(60)
    turtle.forward(S)
    snowflake(S/3,N)
    turtle.back(S)
    turtle.left(60)

def snowflake(S,N):
    """
    Draws the inner branches of snowflakes

    :param S: length /3 of inner branches
    :param N: counter >1
    :return:none
    """
    if N==1:
        pass
    else:
        turtle.forward(S)
        snowflake(S/3,N-1)
        turtle.back(S)
        turtle.left(60)
        turtle.forward(S)
        snowflake(S/3,N-1)
        turtle.back(S)
        turtle.left(60)
        turtle.forward(S)
        snowflake(S/3,N-1)
        turtle.back(S)
        turtle.left(120)
        turtle.forward(S)
        snowflake(S/3,N-1)
        turtle.back(S)
        turtle.left(60)
        turtle.forward(S)
        snowflake(S/3,N-1)
        turtle.back(S)
        turtle.left(60)
def main(S,N):
    star(S,N)
    input("Enter ")
main(S=int(input("enter length:")),N=int(input("enter N:")))

