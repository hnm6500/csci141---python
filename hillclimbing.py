                                #hrishikesh moholkar
"""
#hillclimbing algorithm returns the local maximum point surrounding the location of a
#particular point (x,y)in a particular optimum range. Application of greedy algorithm.

"""
import math

from source.data.rit_lib import *#imports the structure of code for class from rit_lib

class point3d(struct):
    """
    class stores three coordinates as elements.struct is basically from rit_lib
    it has features based on which our program runs.
    """


    _slots=((float,"x"),(float,"y"),(float,"z"))



def evaluate(x,y):
    """

    :param x: value of position of neighbour on x-axis
    :param y: value of position of neighbour on y-axis
    :return:calculate and return value of z
    """
    z=math.sin(x*x)*2-y*math.cos(x*y)-x
    return z


def maxpoint(pointlist):
    """
     find and return point with max z value
     for each p in pointList, return p with max p.z
    """
    maxP = pointlist[0]
    for point in pointlist:
        if point.z>maxP.z:
            maxP=point
    return maxP




def hillclimbing(x,y,d):
    """

    :param x:starting point on x-axis
    :param y:starting point on y-axis
    :param d:step distance to generate neighbour
    :return:z with maximum value
    this algorithm searches for the neighbour with highest point till
    count is upto 300 and stops if exceeds 300 and returns the max value
    """

    p = point3d(x,y,evaluate(x,y))

    count=0
    while count<300:

        p1=point3d(p.x-d,p.y,evaluate(p.x-d,p.y))
        p2=point3d(p.x+d,p.y,evaluate(p.x+d,p.y))
        p3=point3d(p.x,p.y-d,evaluate(p.x,p.y-d))
        p4=point3d(p.x,p.y+d,evaluate(p.x,p.y+d))
        pointList = [p1,p2,p3,p4]
        myMaxPoint = maxpoint(pointList)
        if myMaxPoint.z >= p.z:
            p = myMaxPoint
        else:

            return p

        count=count+1


    print("Unable to find Maximum after 300 iterations.")


def main():

   x=float(input("enter the initial  x value:"))
   y=float(input("enter the initial  y value:"))
   d=float(input("enter step distance:"))                #when d is zero the test doesnt find local maximum
   print(point3d(x,y,evaluate(x,y)))
   print("Local Maximum is ",hillclimbing(x,y,d))


main()
input("press enter to exit")
