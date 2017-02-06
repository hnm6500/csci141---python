                             #Hrishikesh N Moholkar
import turtle
import math                       #imports mathematical function like square root
def drawsquare(length,depth):     #draws the square and this function is called again as per counter for drawing inner squares
  if depth==0:
      pass

  else:
    """pre condition :turtle facing right
       post condition:turtle facing northwest on one side of square."""
    givecolor(depth)       #this function is called to give color to the square as per counter
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(45)
    drawsquare(length/(2*math.sqrt(2)),depth-1)
    """using depth-1 it continues drawing the inner square and stops when the counter is zero .Thus
    preventing going into infinte loop."""
    turtle.right(45)
    givecolor(depth)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length/2)
    turtle.left(45)
    """
    pre condition :turtle facing down.
    post condition:turtle facing southeast.
    """

    drawsquare(length/(2*math.sqrt(2)),depth-1)
    turtle.right(45)
    givecolor(depth)
    turtle.forward(length/2)
    turtle.left(90)
def givecolor(depth):#gives color to square as per counter (depth)
   """modulus operator is used to find the even and odd number .Based on the result counter  decides the color
   of square.when counter is odd square color is green and even then square color is blue."""
   if depth%2==0:
       turtle.pencolor("blue")
   else:
       turtle.pencolor("green")

def main(length,depth):

    drawsquare(length,depth)
    givecolor(depth)
    input("hit enter to exit")
main(int(input("enter your length")),int(input("enter your depth")))



